#!/bin/python
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd

man=np.array([['111','222','333','555','444'],              
              ['111','333','222','444','555'],
              ['555','111','333','222','444'],
              ['333','222','444','111','555'],
              ['333','111','222','444','555'],                                                                                
              ])

a=['AAA','BBB','CCC','DDD','EEE']
pdman=pd.DataFrame(man,index=a)
print(pdman)

woman=np.array([['EEE','AAA','BBB','DDD','CCC'],
               ['DDD','BBB','CCC','AAA','EEE'],
               ['DDD','CCC','BBB','EEE','AAA'],
               ['AAA','BBB','DDD','CCC','EEE'],
               ['CCC','DDD','EEE','BBB','AAA'],                                                                             
               ])    


b=['111','222','333','444','555']
pdwoman=pd.DataFrame(woman,index=b)
print(pdwoman)

def perfect_match(a,pdman,pdwoman):
    sd=pd.Series()
    while len(a)>0:
        sset=sd.index
        pp=pdman.loc[a[0]] 
        for i in list(pp):
            if i in sset:
                mmm=sd[i]
                po=pdwoman.loc[i]
                kl= list(po)
                p=kl.index(mmm)
                q=kl.index(a[0])
                if p<q:
                    continue
                else:
                    sd[i]=a[0]
                    #sd.drop(k)
                    a.remove(a[0])
                    a.append(mmm)
                    break
            else:
                sd[i]=a[0]
                a.remove(a[0])
                break
    return sd


if __name__ == '__main__':
    """主函数"""
    match=perfect_match(a,pdman,pdwoman)
    print(match)
    












