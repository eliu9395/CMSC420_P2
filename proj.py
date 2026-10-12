# AI Usage:
# used AI to help figure out the pattern for insert_nonstandard and del
# Write details about how you used AI for this project.

from __future__ import annotations
from typing import List
import json

# The class for a particular node in the tree.
# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key        : int  = None,
                  leftchild  : Node = None,
                  rightchild : Node = None):
        self.key        = key
        self.leftchild  = leftchild
        self.rightchild = rightchild

# The class for a BST.
class BST():
    # NO NOT MODIFY!
    def __init__(self,
                 root : Node = None):
        self.root = root

    # Dump the tree as a string.
    # DO NOT MODIFY!
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            return {
                "K": node.key,
                "L": (_to_dict(node.leftchild) if node.leftchild is not None else None),
                "R": (_to_dict(node.rightchild) if node.rightchild is not None else None)
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent = 2)

    # insert_standard: This is standard BST insertion.
    # This is only here so that nonstandard deletion and search can be tested independently of the nonstandard insertion.
    # That way if you can't figure out insert_nonstandard you can still get points for delete_nonstandard and search.
    # DO NOT MODIFY!
    def insert_standard(self,key: int):
        def _insert(root: Node, key: int) -> Node:
            if root == None:
                return Node(key = key)
            if key < root.key:
                root.leftchild = _insert(root.leftchild, key)
            elif key > root.key:
                root.rightchild = _insert(root.rightchild, key)
            return root
        # End of def _insert
        if self.root == None:
            self.root = Node(key = key)
        else:
            self.root = _insert(self.root,key)


    # insert_nonstandard: This is nonstandard BST insertion.
    # You'll need to figure out how it behaves (using tracefiles and ouput) and code this accordingly.
    def insert_nonstandard(self,key: int):
        if self.root == None:
            self.root = Node(key=key)
            return
        
        path = []
        n = self.root

        while n != None:
            if key == n.key:
                return
            path.append(n)
            n = n.leftchild if key < n.key else n.rightchild
            
        pred = max((p.key for p in path if p.key < key), default=None)
        succ = min((p.key for p in path if p.key > key), default=None)

        newNode = Node(key=key)
        if key < path[-1].key:
            path[-1].leftchild = newNode
        else:
            path[-1].rightchild = newNode

        above = {x for x in (pred, succ) if x is not None}
        
        last = None
        dir = None
        while above:
            parent = path.pop()
            above.discard(parent.key)
            if parent.leftchild is newNode:
                parent.leftchild = newNode.rightchild
                newNode.rightchild = parent
                dir = 'R'
            else:
                parent.rightchild = newNode.leftchild
                newNode.leftchild = parent
                dir = 'L'
            last = parent
            if path:
                gp = path[-1]
                if gp.leftchild is parent:
                    gp.leftchild = newNode
                else:
                    gp.rightchild = newNode
            else:
                self.root = newNode

        if dir == 'R':
            far = 'rightchild'
            near = 'leftchild'
        else:
            far = 'leftchild'
            near = 'rightchild'
        p_node = newNode
        dist = far
        x = last
        while x is not None:
            if far == 'rightchild':
                c = x.rightchild
            else:
                c = x.leftchild

            while c is not None:
                if near == 'leftchild':
                    if c.leftchild is None:
                        break
                else:
                    if c.rightchild is None:
                        break

                if far == 'rightchild':
                    x.rightchild = c.leftchild
                else:
                    x.leftchild = c.rightchild

                if near == 'leftchild':
                    c.leftchild = x
                else:
                    c.rightchild = x
    
                if dist == 'rightchild':
                    p_node.rightchild = c
                else:
                    p_node.leftchild = c
    
                p_node = c
                dist = near
                if far == 'rightchild':
                    c = x.rightchild
                else:
                    c = x.leftchild

            p_node = x
            dist = far

            if far == 'rightchild':
                x = x.rightchild
            else:
                x = x.leftchild

    # delete_nonstandard: This is nonstandard BST deletion.
    # You'll need to figure out how it behaves (using tracefiles and ouput) and code this accordingly.
    def delete_nonstandard(self,key: int):
        def size(n):
            return 0 if n is None else 1 + size(n.leftchild) + size(n.rightchild)

        n = self.root
        parent = None

        while n is not None and n.key != key:
            parent = n
            n = n.leftchild if key < n.key else n.rightchild
        if n is None:
            return

        if n.leftchild is None or n.rightchild is None:
            child = n.leftchild if n.leftchild is not None else n.rightchild
            if parent is None:
                self.root = child
            elif parent.leftchild is n:
                parent.leftchild = child
            else:
                parent.rightchild = child
            return

        if size(n.leftchild) >= size(n.rightchild):
            dn_parent = n
            x = n.leftchild
            while x.rightchild is not None:
                dn_parent = x
                x = x.rightchild
            n.key = x.key

            if dn_parent is n:
                dn_parent.leftchild = x.leftchild
            else:
                dn_parent.rightchild = x.leftchild
        else:
            dn_parent = n
            x = n.rightchild
            while x.leftchild is not None:
                dn_parent = x
                x = x.leftchild
            n.key = x.key

            if dn_parent is n:
                dn_parent.rightchild = x.rightchild
            else:
                dn_parent.leftchild = x.rightchild

    # Search for a key.
    # You'll need to figure out what it returns (using tracefiles and output) and code this accordingly.
    def search(self,key: int) -> int:
        n = self.root
        returnvalue = 0
        while n is not None:
            if key == n.key:
                return returnvalue
            if key < n.key:
                returnvalue += 1
                n = n.leftchild
            else:
                returnvalue -= 1
                n = n.rightchild
        return returnvalue