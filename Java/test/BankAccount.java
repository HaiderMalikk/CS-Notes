
// by default everything is public ex double number{} method is public but we can add private in start
// a pivate var cannot be accsessed ouside of class
package test; // pakage has to be imported
public class BankAccount {
    private double balance;
    private String firstName;
    private String lastName;
    private int accountNum;

    public BankAccount(double balance, String firstName, String lastName, int accountNum) {
        this.balance = balance;
        this.firstName = firstName;
        this.lastName = lastName;
        this.accountNum = accountNum;
    }

    public double withdraw(double amount) {
        balance -= amount;
        return balance;
    }

    public double deposit(double amount) {
        balance += amount;
        return balance;
    }

    public double getBalance() {
        return balance;
    }

    public String toString() {
        return "Balance: "+this.balance+" of "+this.firstName+" "+this.lastName+"\nAccount Number: "+this.accountNum;
    }

}