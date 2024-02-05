import java.util.Scanner;

class practiceproblem {
    // election on February 27, 2007, enter date in format yyyy mm dd, if older than 18 "yes" if not "No"
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your birth date in the format yyyy mm dd:");

        String inputdatestr = input.nextLine();
        String[] parts = inputdatestr.split(" ");

        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]);
        int day = Integer.parseInt(parts[2]);

    // to visualize 
        System.out.println("Year: " + year);
        System.out.println("Month: " + month);
        System.out.println("Day: " + day);

        if(year >= 1989){
        if (month >= 02){
            if (day >= 27){
                System.out.println("Yes");
            } else {System.out.println("NO");}
        } else {System.out.println("NO");}
        } else {System.out.println("NO");}

        input.close();
                    
   }
}
