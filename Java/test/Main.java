package test;
public class Main {
    public static void main(String[] args) {

        BankAccount account1 = new BankAccount(100.0, "Rachel","Luo",1);


        System.out.println(account1.getBalance());
        System.out.println(account1.toString());

        account1.withdraw(50.0);

        System.out.println(account1.toString());

        account1.deposit(12.75);
        System.out.println(account1.toString());

    }
}