class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 栈辅助法
# class Solution:
#     def reversePrint(self, head: ListNode):
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next
#         return res[::-1]


# 递归法
class Solution:
    def reversePrint(self, head: ListNode):
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]
