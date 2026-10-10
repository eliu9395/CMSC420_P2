# AI Usage:
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
        # The next line is just here to make it run.
        dummy = True

    # delete_nonstandard: This is nonstandard BST deletion.
    # You'll need to figure out how it behaves (using tracefiles and ouput) and code this accordingly.
    def delete_nonstandard(self,key: int):
        # The next line is just here to make it run.
        dummy = True

    # Search for a key.
    # You'll need to figure out what it returns (using tracefiles and output) and code this accordingly.
    def search(self,key: int) -> int:
        # The next line is just here to make it run.
        # You'll need to figure out what is being returned.
        returnvalue = 0
        return returnvalue