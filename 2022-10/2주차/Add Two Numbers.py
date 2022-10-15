# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        answer = [0]
        answer_lst = ListNode()
        curr_answer = answer_lst

        curr_l1 = l1
        curr_l2 = l2

        l1_end = False
        l2_end = False

        while True:
            if not curr_l1 and not curr_l2:
                break

            _sum = curr_answer.val
            # _sum = answer[-1]

            if curr_l1:
                _sum += curr_l1.val
                curr_l1 = curr_l1.next

            if curr_l2:
                _sum += curr_l2.val
                curr_l2 = curr_l2.next

            remainder = _sum % 10
            share = _sum // 10

            curr_answer.val = remainder

            if share or curr_l1 or curr_l2:
                curr_answer.next = ListNode(share)
                curr_answer = curr_answer.next

            # answer[-1] = remainder
            # answer.append(share)

        print(answer_lst)

        return answer_lst
