import java.util.ArrayList;
import java.util.Collections;

public class ListNode {
     int val;
     ListNode next = null;
     ListNode() {}
     ListNode(int val) {
          this.val = val;
     }
     ListNode(int val, ListNode next) {
          this.val = val;
          this.next = next;
     }
     ListNode(ArrayList<Integer> list) {
          if(list.size() < 1) return;
          this.val = list.remove(0);
          if(list.size() != 0) this.next = new ListNode(list);
     }

     ListNode reverse() {
          ListNode nodeCopy = this;
          ArrayList<Integer> values = new ArrayList<>();
          while(nodeCopy != null) {
               values.add(nodeCopy.val);
               nodeCopy = nodeCopy.next;
          }
          if(values.size() == 1) return this;

          Collections.reverse(values);

          return new ListNode(values);
     }

     @Override
     public String toString() {
          ListNode node = this;
          String separator = " --> ";
          StringBuilder result = new StringBuilder("{ ");

          while(node != null) {
               result.append(node.val);
               result.append(separator);
               node = node.next;
          }

          result.append("\b".repeat(separator.length()));
          result.append(" }");
          return result.toString();
     }
}