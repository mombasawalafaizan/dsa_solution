// { Driver Code Starts
import java.util.*;

class Node
{
    int data;
    Node next;
    Node(int d) {
        data = d; 
        next = null;
    }
}


public class circular_LinkedList
{
    Node head, head1, head2;  // head of lisl
    //Node last = null;
    Node last = null;
  
    /* Linked list Node*/
   
                    
    /* Utility functions */
 
    /* Inserts a new Node at front of the list. */
     public void addToTheLast(Node node) 
     {
        
          if (head == null) 
          {
            head = node;
            
          } else 
          {
               Node temp = head;
               while (temp.next != null)
               temp = temp.next;

               temp.next = node;
          }
     }
  /* Function to print linked list */
    void printList(Node node)
    {
        Node temp = node;
        if(node != null)
        {
            do{
           System.out.print(temp.data+" ");
           temp = temp.next;
            }while (temp != node);
        }  
        System.out.println();
    }
    
    void circular()
    {
            last = head;
            while (last.next != null)
                last = last.next;
            last.next = head;
            //System.out.println(last);
    }
    
     
 
     /* Drier program to test above functions */
    public static void main(String args[])
    {
       
         
        /* Constructed Linked List is 1->2->3->4->5->6->
           7->8->8->9->null */
         Scanner sc = new Scanner(System.in);
         int t=sc.nextInt();
         while(t>0)
         {
            int n = sc.nextInt();
            circular_LinkedList llist = new circular_LinkedList();
            int a1=sc.nextInt();
            Node head= new Node(a1);
            llist.addToTheLast(head);
            for (int i = 1; i < n; i++) 
            {
            int a = sc.nextInt(); 
            llist.addToTheLast(new Node(a));
            
            
             }
             /*Node x = head;
             while(x!=null)
             {
                 System.out.print(x.data+" ");
                 x = x.next;
             }*/
            llist.circular();
          //int k=sc.nextInt();
         gfg g = new gfg();
         //System.out.println(g.getCount(llist));
         g.splitList(llist);
         llist.printList(llist.head1);
         llist.printList(llist.head2);
        //llist.printList();
        //llist.head = llist.reverse(llist.head);
        //llist.printList();
        
        
        t--;
        sc.close();
    }
}
}// } Driver Code Ends


/* Node of a linked list
 class Node {
   int data;
    Node next;
    Node(int d)  { data = d;  next = null; }
}
*/

class gfg
{
        // Function  to split a circular LinkedList
    void splitList(circular_LinkedList list)
    {
        Node true_head = list.head;
        Node slow = true_head;
        Node fast = true_head;
        while(fast.next != true_head && fast.next.next!=true_head){
            slow = slow.next;
            fast = fast.next.next;
        }
        Node new_head = slow.next;
        if(fast.next!=true_head)
            fast = fast.next;
        slow.next = true_head;
        fast.next = new_head;
        list.head1 = true_head;
        list.head2 = new_head;

    }
    
    // void printlist(Node head){
    //     if(head==null){
    //         return;
    //     }
    //     System.out.print(head.data+" ");
    //     Node temp = head.next;
    //     while(temp!=head){
    //         System.out.print(temp.data+" ");
    //         temp = temp.next;
    //     }
    // }
}