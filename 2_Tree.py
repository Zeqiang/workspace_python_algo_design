#!/bin/python
# -*- coding: utf8 -*-
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []
        self.stack_1 = []
        self.stack_2 = []
        self.stack_3 = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        self.stack_1.append(root.elem)
        self.front_digui(root.left)
        self.front_digui(root.right)
        return self.stack_1


    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.left)
        self.stack_2.append(root.elem)
        self.middle_digui(root.right)
        return self.stack_2


    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        self.stack_3.append(root.elem)
        return self.stack_3


    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        result = []
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                result.append(node.elem)
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right                  #开始查看它的右子树
        return result


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        result = []
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            result.append(node.elem)
            node = node.right                  #开始查看它的右子树
        return result


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        result = []
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            new_ele = myStack2.pop()
            result.append(new_ele.elem)
        return result


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        result = []

        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            result.append(node.elem)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
        return result


if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for elem in elems:                  
        tree.add(elem)           #逐个添加树的节点

    print('队列实现层次遍历:')
    print(tree.level_queue(tree.root))

    print('\n\n递归实现先序遍历:')
    print(tree.front_digui(tree.root))
    print('\n递归实现中序遍历:' )
    print(tree.middle_digui(tree.root))
    print('\n递归实现后序遍历:')
    print(tree.later_digui(tree.root))

    print('\n\n堆栈实现先序遍历:')
    print(tree.front_stack(tree.root))
    print('\n堆栈实现中序遍历:')
    print(tree.middle_stack(tree.root))
    print('\n堆栈实现后序遍历:')
    print(tree.later_stack(tree.root))
    












