from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head=p=ListNode(0);
        q=PriorityQueue();
        i=0;
        for i,l in enumerate(lists):
            if l:
                q.put((l.val,i,l));
                
        while not q.empty():
            val,ind,point=q.get();
            #point=lists[ind];
            p.next=ListNode(val);
            p=p.next;
            point=point.next;
            if point:
                q.put((point.val,ind,point));
        return(head.next);
