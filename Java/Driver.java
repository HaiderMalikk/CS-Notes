       
// Often we will have a “Driver Class” that only contains a main method. From this class, we create other objects.
// Relies on project/folder structure, all classes must be located in the same folder


class Main {
    
    public static void main(String[] args) {
        Person p1 = new Person("Haider",28,"student");
        Person p2 = new Person("Talal",25,"data scientist");

        System.out.println(p1);
        System.out.println(p2);

        p1.sleep();
        p2.sleep();

        p2.eat();
    }
}
