import java.util.Scanner;

public class Animals {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        Scanner sc =  new Scanner(System.in);
        String input = sc.next();
        sc.close();

        Animal a = null;
        switch(input) {
            case "Butterfly":
                a = new Butterfly();
                break;
            case "Duck":
                a = new Duck();
                break;
            case "Whale":
                a = new Whale();
                break;
        }

        a.explain();
        if(a instanceof Flyable) {
            ((Flyable) a).AddAnExplanationOfFlight();
        }
        if(a instanceof Swimable) {
            ((Swimable) a).AddAnExplanationOfSwim();
        }

        System.out.println(a.comment);
    }

}

class Animal {
    String comment = "";
    int legs;

    void explain() {
        comment += "Here is a(an) " + this.getClass().getSimpleName() + ".\n";
        comment += "It has " + legs + " legs.\n";
    }
}



interface Flyable {
    static String flight = "And it can fly.\n";

    abstract void AddAnExplanationOfFlight();
}

interface Swimable {
    static String swim = "And it can swim.\n";

    abstract void AddAnExplanationOfSwim();
}

class Butterfly extends Animal implements Flyable{
    { legs = 6;
    AddAnExplanationOfFlight();}
}

class Duck extends Animal implements Swimable, Flyable {
    { legs =2; }
}

class Whale extends Animal implements Swimable{
    { legs=0; }
}

//import java.util.Scanner;
//
//public class Animals {
//    public static void main(String[] args){
//        // TODO Auto-generate method stub
//
//        Scanner sc = new Scanner(System.in);
//        String input = sc.next();
//        sc.close();
//
//        Animal a = null;
//        switch(input) {
//        case "Butterfly":
//            a = new Butterfly();
//            break;
//        case "Duck":
//            a = new Duck();
//            break;
//        case "Whale":
//            a = new Whale();
//            break;
//        }
//
//        a.explain();
//        if(a instanceof Flyable){
//            ((Flyable) a).AddAnExplanationOfFlight();
//        }
//        if(a instanceof Swimable){
//            ((Swimable) a).AddAnExplanationOfSwim();
//        }
//        System.out.println(a.comment);
//    }
//}
//
//class Animal {
//    String comment = "";
//    int legs;
//
//    void explain() {
//        comment += "Here is a(an) " + this.getClass().getSimpleName() + ".\n";
//        comment += "It has" + legs + " legs. \n";
//    }
//}
//
//interface Flyable {
//    static String flight = "And it can fly. \n";
//
//    abstract void AddAnExplanationOfFlight();
//
//}
//interface Swimable {
//    static String swim = "And it can swim.\n";
//
//    abstract void AddAnExplanationOfSwim();
//
//}
//
//class Butterfly extends Animal implements Flyable{
//    String comment = "";
//    int legs;
//
//    void explain() {
//        comment += "Here is a(an) " + this.getClass().getSimpleName() + ".\n";
//        comment += "It has" + legs + " legs. \n";
//
//    }
//}
//
////class Duck extends Animal implements Swimable, Flyable{
////    legs = 2;
////}
////
////class Whale extends Animal implements Swimable{
////    {legs = 0;}
//}