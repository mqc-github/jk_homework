"""
作业题1：加一
原理：字符转换
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         str_dit=[]
         for i in digits:
             str_dit.append(str(i))
         k=str(int("".join(str_dit))+1)
         result=list(map(int,k))
         return result
        

"""
作业题2：合并两个有序列表
原理：递归
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2