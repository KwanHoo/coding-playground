 import java.util.*;  // util 패키지 임포트

//public class exam011 {
//    public static void main(String[] args){
//        System.out.println("Hello World!");
//
//    }
//}
class FormatSample{
    public static void main(String[] args){
        int a =10;
        double b =3.4;
        System.out.printf("%10d\n",a);
        System.out.printf("X %8.5f\n", b);
        System.out.printf("-----------\n");
        System.out.printf("%10f\n\n", a * b);
    }
}

class Number{
    public static void main(String[] args){
        int[] a = {1, 2, 3, 4};
        System.out.println((a[0]));
        System.out.println(a[3]);
    }
}

public class exam01{
    public static void main(String[] args){
        int num = 0;
        System.out.print("*을 출력할 라인의 수를 입력하세요.>");

        Scanner scanner = new Scanner(System.in);
        String tmp = scanner.nextLine();
        num = Integer.parseInt(tmp);

        for(int i=0; i<num; i++){
            for(int j=0; j<=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

