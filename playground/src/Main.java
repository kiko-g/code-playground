import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ListNode node = new ListNode(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(node.reverse());
    }
}
