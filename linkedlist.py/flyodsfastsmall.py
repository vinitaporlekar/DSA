class Solution:
    def fastSmall (slef, head : ListNode)->bool:
        slow, fast = head, head

        while fast and fast.next:
            small = small.next
            fast = fast.next.next
            if small == fast:
                return True
        return False
    

        