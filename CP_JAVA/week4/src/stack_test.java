import java.util.Stack;

public class stack_test {
    public static void main(String[] args){
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < 5; i++)
            stack.push(i);

        for (int i = 0; i < 5; i++)
            System.out.println(stack.pop());

    }
}

