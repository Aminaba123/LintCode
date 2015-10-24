"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) . For each
element Ai in the array, count the number of element before this element Ai is smaller than it and return count number
array.

Example
For array [1,2,7,8,5], return [0,1,2,3,2]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query II and Count of Smaller Number before itself I
first.
"""
__author__ = 'Daniel'


class Node(object):
    def __init__(self, start, end):
        """Records the left subtree size"""
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.cnt_this = 0
        self.cnt_left = 0

    def __repr__(self):
        return repr("[%d, %d)" % (self.start, self.end))


class SegmentTree(object):
    def __init__(self):
        self.root = None

    def build(self, root, start, end):
        if start >= end: return
        if not root: root = Node(start, end)

        root.left = self.build(root.left, start, (end+start)/2)  # not (end-start)/2
        if root.left: root.right = self.build(root.right, (end+start)/2, end)

        return root

    def set(self, root, i, val):
        if root.start == i and root.end-1 == root.start:
            root.cnt_this += val
        elif i < (root.end+root.start)/2:
            root.cnt_left += val
            self.set(root.left, i, val)
        else:
            self.set(root.right, i, val)

    def get(self, root, i):
        if root.start == i and root.end-1 == root.start:
            return root.cnt_left
        elif i < (root.end+root.start)/2:
            return self.get(root.left, i)
        else:
            return root.cnt_left+root.cnt_this+self.get(root.right, i)


class Solution(object):
    def countOfSmallerNumberII(self, A):
        """
        Segment Tree

        :param A: A list of integer
        :return: Count the number of element before this element 'ai' is smaller than it and return count number list
        """
        if not A: return []
        st = SegmentTree()
        st.root = st.build(st.root, min(A), max(A)+1)
        ret = []
        for a in A:
            ret.append(st.get(st.root, a))
            st.set(st.root, a, 1)

        return ret

if __name__ == "__main__":
    print Solution().countOfSmallerNumberII([1, 2, 7, 8, 5])
    assert Solution().countOfSmallerNumberII(
        [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97,
         3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]) == [0, 1, 1, 3, 2, 3, 5, 0, 4, 0, 5, 1, 6, 2, 9, 2, 14, 10, 17,
                                                             14, 16, 7, 16, 7, 22, 2, 0, 25, 1, 20, 29, 15, 4, 6, 28,
                                                             20, 20, 16, 37, 18]
