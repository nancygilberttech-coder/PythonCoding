from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode(0)
        current=dummy_node
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            #sum_val=val1+val2+carry
            carry,sum_val=divmod(val1+val2+carry,10)
            #Create a new node for the Next position
            current.next=ListNode(sum_val)
            current=current.next # Move current to the node we just created

            l1=l1.next if l1 else None
            l2= l2.next if l2 else None

        return (dummy_node.next)

    def create_linked_list(self,array1 :List[int])->Optional[ListNode]:
        """Converts Python list to Linked List"""
        dummy=ListNode(0)
        ptr=dummy
        for val in array1:
            ptr.next=ListNode(val)
            ptr=ptr.next
        return dummy.next

    def print_linkedlist(self, node:Optional[ListNode]):
        """Prints Linked List in a readable format:2->3->4"""
        values=[]
        while node:
            values.append(str(node.val))
            node=node.next
        print("-->".join(values))


#HOW TO CALL IT

if __name__ == "__main__":
    # Create the two linked lists
    # Example 1: 342 + 465 = 807 (Input is reversed: [2,4,3] + [5,6,4])
    sols = Solution()
    list1 = sols.create_linked_list([9, 9, 9])
    list2 = sols.create_linked_list([9, 9, 9])

    print("List 1:")
    sols.print_linkedlist(list1)
    print("List 2:")
    sols.print_linkedlist(list2)

    # Call the solution
    result = sols.addTwoNumbers(list1, list2)

    print("Resulting Sum List:")
    sols.print_linkedlist(result)

