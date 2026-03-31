from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        dq = deque()
        curr = head

        while curr:
            dq.append(curr)
            curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        left_turn = True

        while dq:
            if left_turn:
                node = dq.popleft()
            else:
                node = dq.pop()

            tail.next = node
            tail = tail.next
            left_turn = not left_turn

        tail.next = None  # 🔥 critical

        head = dummy.next
