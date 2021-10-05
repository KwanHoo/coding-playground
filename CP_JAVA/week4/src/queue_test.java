import java.util.ArrayDeque;
import java.util.Queue;

public class queue_test {
    public static void main(String[] args){
        Queue<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < 5; i++)
            queue.offer(i);

        for (int i = 0; i < 5; i++)
            System.out.println(queue.poll());

    }
}
