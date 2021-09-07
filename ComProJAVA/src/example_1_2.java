class Car{
    String color;
    String gearType;
    int door;

    Car() {}
    Car(String c, String g, int d){
        color = c;
        gearType = g;
        door = d;
    }
    String getcolor(){return this.color;}

    void setdoor(int count) {this.door =count;}
}

public class example_1_2 {
    public static void main(String[] args){
        Car c1 = new Car();
        c1.color = "blue";
        c1.gearType = "auto";
        c1.door = 4;

        Car c2 = new Car("white", "auto", 4);
        System.out.println("c1의 color = " + c1.color + ", 기어타입 =" + c1.gearType+", 문짝수= "+c1.door);
        System.out.println("c2의 color = " + c2.color + ", 기어타입 =" + c2.gearType+", 문짝수= "+c2.door);

        Car c3 = new Car();

        c3.color = "red";
        c3.gearType = "auto";
        c3.door =2;

        System.out.println(("c3의 색깔 ="+ c3.getcolor()));
        c3.setdoor(4);
        System.out.println("c3의 color = " + c3.color + ", 기어타입 =" + c3.gearType+", 문짝수= "+c3.door);

    }
}
