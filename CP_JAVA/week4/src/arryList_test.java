import java.util.ArrayList;
import java.util.List;

public class arryList_test {
    public static void main(String[] args){
        List<String> list = new ArrayList<>();
        list.add("a"); list.add("b"); list.add("d"); list.add("c");

        System.out.println(list);
        list.remove("b");

        System.out.println(list);
        list.remove(0);
        System.out.println(list);

        list.add(2, "e");
        System.out.println(list);

        list.add(1, "j");
        System.out.println(list);

    }
}
