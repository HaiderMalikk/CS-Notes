import java.util.Arrays;
import java.util.Scanner;

class scanner_and_conditionals{
    public static void main(String[] args){
        System.out.println("IF statements are called conditionals in java!");

        // "if" means if true or false 
        // "else if" if the if is false, else if something else if true 
        // "else" if nothing is true
        // "||" double pipes means OR ethier condition can be true, placed between conditions 
        // "&&" double and means AND all conditions have to be true, placed between conditions 
        // "!true" means false, "!true" means not true if somthing is not true its false and vise versa)
        // "!false" means true, there can only be true and false so if something is not false its true and vise versa
        // "!=" means not equal too
        // "++" means add one to a varible, EX counter++; ads 1 to a var nammed counter
        // "--" means minus one, EX counter--; munus oneto a var
        // you can also use the same signs from phython to assign a new value to var
        // "+=" means add x num and set var equal too number, "-= subtract", "*= multiply", "/= divide"
        // "counter++;" = "counter += 1;"
        // mutally exclusive conditinlasm means two or more conditionals that cannot be poosible at once 
        // mutally exclusive EX if num1 > num2  if or else if or else num1 = num2 cannot both be true

        // input 
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the weight of the luggage in lbs: ");
        int weight = input.nextInt();
        input.close();

        // firts if statement everything under this if statement only runs if the if statement is true
        // here there is a print satement under all statements
        // if statement runs if condition is met
        if (weight <= 20) {
        System.out.println("Your baggage meets weight requirements!");
            // this if statement indented in a if statement is called a nested if statement 
            // this only runs if the if stament its indented in is true so if weight is under 20 
            // you can also create just if and elifs nut yu could have to place it in order checking for 10lb before 20
            if (weight <= 10){
            System.out.println("You can get a discount!");
            }
        }
        // this else if statement only runs if the if statement is false 
        else if (weight > 21 && weight <= 50) {
        System.out.println("A surcharge for baggage will apply!");
        }
        // this is only ran if the if and else if statement fail 
        else {
        System.out.println("Your baggage is too heavy!");
        }
        
        // you can also create a int then set it equal to something later
        // create a int and its name heheheeh
        // int num1, num2;
        //System.out.print("Enter the first number: ");
        // now set num1 int equal to a value
        //num1 = scanner.nextInt();
        //System.out.print("Enter the second number: ");
        // set num 2 equal to a value
        //num2 = scanner.nextInt();

        }

}


class loops{
        public static void main(String[] args){
        // while, do while and for loops
        // with do while lopps you check condition last so you run the loop then check if its true or false
        // you use it if you want something to happen before checking if loop is true or false

        double product = 1.5;
        /*
            for (int count=1; count <=5; count++) {
              product = product*count;
              System.out.print(count + " ");
            }
            System.out.println("\n"+product);
         */ 
        
        System.out.println("------------------");
    
        int first = 43;
        int second = 10;
    
        System.out.println("While Loops");
        while (first > second) {
        System.out.println(first + " "+second);
        first -= 5;
        second +=6;
        System.out.println("first "+first);
        System.out.println("second "+second);
        }
        System.out.println(product);

        System.out.println("------------------");

        // for loops
        // for (initialization; condition; increment) { body of loop }
        // initialization: executed at the start of loop eg creating a var (int count = 1)
        // condition: this is a true or false condition that is checked before running the loop only start if true
        // condition: the loop only starts if true eg (count <= 5)
        // increment: elavuated after each execution of body eg update a var (count++) 
        // body: what happens in the loop eg (count += 1)

        // here i created a for loop where i made a int called count and set it to 1
        // i made it so the loop only runs if count is <= 5
        // after running the loop if adds 1 to count everytime until count > 5
        for (int count = 1; count <= 5; count += 1){
            // print val of count before anything is added 
            // the first time its ran it prints 1
            // the second time 1 is added from the body and increment making count = 3
            System.out.printf("Count: %d ", count);
            // add 1 to count
            count += 1;
        }
        // i can not use the var count outside of loop
        System.out.println("the loop has ended");

        // do while
        Scanner scanner = new Scanner(System.in);
        int userInput;
        
        // do: promt up "enter a number" 
        // this will keep poping up as long as the while loop it true
        // with do while loops you check condition last so do comes before while 
        // do while runs the do loop at least once and the condition is checked last
        // if the while condition in true the do loop will keep running
        do {
            System.out.print("Enter a number between 1 and 10: ");
            userInput = scanner.nextInt();
        } 
        // while the user input is a number 1-10 print number
        // || = or
        while(userInput < 1 || userInput > 10);
        
        // only runs if while loop it false
        System.out.println("You entered: " + userInput);

        scanner.close();

    }

}

       
class methods{
    public static void main(String[] args){
        // METHODS
        // methods are functions in java
        // there are many methods static methods are the ones that are like funtions 
        // here i call the method in a diffrent method the static void main
        // method exaple 
        Scanner input1 = new Scanner(System.in);

        System.out.print("Enter the base of the triangle: ");
        double base = input1.nextDouble();

        System.out.print("\nEnter the height of the triangle: ");
        double height = input1.nextDouble();
        
        input1.close();

        // here the right side is the value that is going to be defined in the function
        // you can use var before its defined
        double area = triangleArea(base, height);

        System.out.printf("\nThe area of the triangle is %.2f", area);

    } // end of method main

    // public static void is the method so this method is outside the first methods curly braces
    // you can use vars for any method to use in any method you can
    //  YOU CAN use a var before you define it 
    // public static "return type" "method name" (parameters)  
    // new method
    public static double triangleArea(double base, double height) {
        double area;
        area = base*height/2;
        return area;
        } // end of method double 

}


class strings{
    public static void main(String[] args){
        System.out.println("THIS IS A STRING");
        // strings are objects not primitive data types like int, double, boolean
        // first method to make a string
        String welcome = ("hello");
        System.out.println(welcome);
        // 2nd method to make strings
        // refrence string welcome is the refrence vars are nor objects
        String welcome2 = new String("welcome");
        System.out.println(welcome2);
        // to check if string input is equal to something 
        // if (welcome.equals("hello")) { do this }
        // there are many checker for string EX varaible.public int length(); this checks length of string
        // example code
        String str = "Knowladge is ";
        // we dont define thr var we can do that later in java 
        String s;
        s = str;
        // updating str to a diffrent string
        str = "Knowladge is power";
        // even though we changed the value of str it still printed s that was set to str before str was updated
        // str was lost when updated but i set s = to str before updating so i still have original str as s if needed
        System.out.println(s);
        // we lost the value of str as we updated it ist no longer "knowdlage is" its "knowlage is power"
        System.out.println(str);
        System.out.println(str.length());

        // lossing string refrence
        String str1 = "testing";
        String str2 = "strings";
        // by setting the str1 to a new value we have lost the original value of str1
        str1 = str1.concat(str2);
        // str1 is now longer tetsting but testing strings
        System.out.println(str1);

        // == checks memory location not value 

        // new method new creates a new string this way it will print value and not memory location
        // with this you can do compare strings if new1 = "new String"
        String new1 = new String("new String");
        System.out.println(new1);

        // new lesson / method
        // there are many string methods like taking char lenghth of string deleting spaces ETC
        // when modifing a var create a new var to assign the modified string too
        String stringa = " Hello ";
        // trim removes start and finish whitespace
        String stringb = stringa.trim();
        System.out.println(stringb);

        // finds white spaces
        for(int i =0; i < stringa.length(); i++) {
            if(stringa.charAt(i) == ' ') {
                System.out.println("space found");
            }
        }
        // substring method
        // Substring dose include the begin index but dose not include the end index rather the number before it
        // e is the third char but i use 4
        // we do this as index starts at 0
        // can also have one char at one point stringa.substring(3)
        System.out.println(stringa.substring(1, 4));

        // prints index 0, 1"i" number before 1 is 0 so only print 0 index 0 is "*"
        // then i++ so i is 2 end index 2 means 1 so prints index 0 until 1 "**"
        // it keeps doing this untill i is 6 then condition false i = 6 is index 5 the last star
        // so it prints att 5 starts going trough and adding 1 start each time 
        String stars = "*****" ;
        int i = 1;
        while (i <= stars.length()) {
        System.out.println( stars.substring(0,i));
        i = i+1;
        }
        // can also have just start no finish means it will do all char from start
        // start index is exact
        String srt = "Laptop";
        System.out.println(srt.substring(3));

        // finding a char and its index
        String phrase = "hi my name is haider thats haider !";
        // if char dose not exist = -1
        // the word haider is index 14 as it starts at 14 no end index is givin
        // if haider was written more than once it would not give two index 
        int findQ = phrase.indexOf("haider");
        System.out.println(findQ);

        System.out.println("method 1 for finding multiple char");

        // to find a word that occurs more than once
        String search = "haider";
        int position = phrase.indexOf(search);
        // skips over first occurance "position" where there is h for haider
        // it creates a substring a new string 1+ index after the first occurance index 
        // the first time haider occurs is 14 + 1 = 15 so substring starts at index 15 "a"
        // so now we make a new substring thats index is 0 at "a" where the orginal string was 15
        // then it prints out position 2 that is 12
        // this is as haiders H starts at index 12 in that substring thats index 0 is at "a" or index 15 in phrase
        String rest = phrase.substring(position+1);
        int position2 = rest.indexOf(search);
        System.out.println(position);
        System.out.println(position2);

        // method 2
        System.out.println("method 2 for finding multiple char ");
        String example = "the sea is calm tonight";
        int aIndex = example.indexOf("a");
        System.out.println(aIndex);
        String tail = example.substring(aIndex);
        System.out.println(tail);

        // replace method replaces all occurances
        String space = "hel lo";
        System.out.println(space.replace(" ", ""));


    
    }

}

class method_overloading{
    // methods with exact same name but diffrent parameters, the method is defined by its paramiters 
    // helps where we want to do same function with diffrent data types one method for int one for double 
    public static void main(String[] args) {
        // max (parameter1, parameter2)
        System.out.println(max(3,7));
        System.out.println(max(2.43,9.123));
        // decides larger number between 4 and 7
        System.out.println(Math.max(4,7));
      }

    // lets make 2 methods nammed max with data types int and double that returns maximum
    // there are 2 diffrent agruments for max one with int and one with double
    // java decides what method to use based of parameter type for int use method 1 for double use method 2
    
    public static int max(int num1, int num2) {
    if (num1 > num2) {
        return num1;
    }
    return num2;
    }
    
    public static double max(double num1, double num2) {
    if (num1 > num2) {
        return num1;
    }
    return num2;
    }

}

class array{
    // arrays are simmilar to lists in python
    // arrays have indexes, must be same data type, can have array full of primitve data types (int, etc)
    // array is a object, if something is nit primitive data type it is a object
    // once we have decided number of elements in a array its fixed 
    // you need refrence var to use arrays, ex int num = 10; (refrence var is "num")
    //
    public static void main(String[] args){
        // syntax is type[] arrayname; (type can be primitive or objects) this is the syntax of array
        // to create a array object, type[] arrayname = new type[length]; ,this is only one way 
        // there arre many other ways the one above is good if you know the length of array 
        // how we give array value, array[index] = 3
        // initallizing array int[] numbers = {23, 5, 4, 7, 8}
        int [] numbers = new int[5]; // creating array object 

        // adds a number to each index, index 0 = index+1 = 1 so index 0 id numbers = 1 index++ so we move to next index 
        // index = 1 now and value = index +1 = 2 so index 1 = 2 and so on until we reach max index length 
        for(int index = 0; index < numbers.length; index++){
            numbers[index] = index+1;
            // this creates the array but no print 

        }
        // 
        for(int i =0; i< numbers.length; i++){
            System.out.println(numbers[i]);
        }
        // no append method so you cant just app stuff as you go
        // but if you know what you want in array but dont know length 
        String[] myStrings = {"test", "test1", "test2"};
        System.out.println("array length: " + myStrings.length); // no () required 


}
}


class array_algorithms{
    // arrays are like phython lists
    // each element has a index starts with 0
    // there is no index-1 to get the last index insted you do type.length() - 1
    // you must know the elements or length of the array before you create it
    public static void main(String[] args){
    // creating a array just a array it has no legnth or elements 
    int[] array;
    Scanner input = new Scanner(System.in);

    System.out.print("how many numbers to enter? ");
    // finding the size for array
    int size = input.nextInt();

    // new creates the object
    // we give the array a length of size
    array = new int [size];

    // too add a value for each length as long as size is < length keep asking for input (size = index of array)
    for (int index = 0; index < array.length; index++) {
        System.out.print("Enter a number: ");
        // index starts at 0
        array[index] = input.nextInt();
    }
    // doing System.out.println(array); will give memory adress 
    // we have to import a pakage called import java.lang.reflect.Array; and use the tostring method prameter = array
    System.out.println(Arrays.toString(array));
    input.close();

    // max and min
    int[] array2 = {-20, 19, 1, 5, -1, 27, 19, 5};
    int max;

    // initialize the current maximum
    max = array2[0];

    for (int index=0; index < array2.length; index++){ 
      if (array2[index] > max ) {
        max = array2[ index ]; // if it is the largest so far, change max
        } // end if
    } // end loop
    // you can use equals to compare array it will cehck the elements and there positions both have to be same

}
}


class advanced_array_algorithims{
  // arrays are imalluable they are fixed you ether need to know the length or elemets before you make array
    // appending a element, adding a element to a array, appending always adds element to the end of array 
      // int newArray[4] = oldArray[index]
    public static void main(String[] args) {
      int[] numbers = {1,2,3,4,5};
  
      System.out.println(Arrays.toString(numbers));
  
      numbers = append(numbers);
  
      System.out.println(Arrays.toString(numbers));
  
      numbers = insertElement(numbers, 4);
  
      System.out.println(Arrays.toString(numbers));
  
      numbers = deleteElement(numbers, numbers.length-1);
      
      System.out.println(Arrays.toString(numbers));
  
    }
  
  
    public static int[] append(int[] array) {
      Scanner input = new Scanner(System.in);
  
      System.out.print("Enter a new element: ");
      int element = input.nextInt();
  
      int[] newArray = new int[array.length+1];
  
      // copy all the elements from the old array into the new array
      for(int index=0; index < array.length; index++) {
        newArray[index] = array[index];
      }
  
      // add the new element to the last index of new array
      newArray[newArray.length - 1] = element;
  
      return newArray;
    } 
  
    public static int[] insertElement(int[] array, int index) {
      Scanner input = new Scanner(System.in);
      
      System.out.print("Enter a new element: ");
      int element = input.nextInt();
  
      int[] newArray = new int[array.length + 1];
  
      //copy the elements from the old array into new array at the same index, stopping just before we need to add the new element at "index"
      for(int i=0; i <= index-1; i++) {
        newArray[i] = array[i];
      }
  
      newArray[index] = element; // add the new element at the specified index
  
      // continue copying the elements from the old array, but shift their indices by +1 in the new array
      for(int i=index; i < array.length; i++) {
        newArray[i+1] = array[i];
      }
  
      return newArray;
    }
  
    public static int[] deleteElement(int[] array, int index){
      int[] newArray = new int[array.length - 1];
  
      // make a copy of all the elements in the old array up to, but not including the specified index to delete
      for (int i=0; i < index; i++) {
        newArray[i] = array[i];
      }
      
      // shifts the elements in the old array backwards by 1 index to "delete" the element at the specified index
      for(int i=index; i < array.length-1; i++) {
        newArray[i] = array[i+1];
      }    
  
      return newArray;

      
       
    }
  
  
    
  }

// by using try and catch our code wont crash when a error eccors 
// we can also we can change the error message to something useful 
class errorsolving {
  public static void main(String[] args) {
    System.out.println("Hello world!");

    int numerator = 5;
    int denominator = 0;

    // with try the code inside will be tested if ok if will run
    // so here if divide works it will print divide
    try {
      int divide = numerator / denominator; // we try dividing by zero that is not possible so there will be a error
      System.out.println(divide);
    }
    // if try dose not work there is a error that error is caught 
    // the catch acts as a else while the try is a if statement the catch will run if try fails
    // as we cannot devide by zero try fails and catch runs
    // format is catch (errortype obj(refrence var to the error)) 
    // here the error is a ArithmeticException you can also use "Exception" that way it will tell you the error
    catch (ArithmeticException e) {
      // "e" is the refrence var to our error
      System.out.println(e); // prints error and not extra info on eroor keeping it simple and easy to read
      System.out.println("So sorry :("); // we can also add whatever we want to the catch Ex extar error info
    }

    System.out.println("After the try catch block"); // with try catch the code dose not crash and continous after

    String greeting = "hello";

    // here we try to print hellos index 5 that dose not exist as there is a error in this code catch will run insted
    try{
      System.out.println(greeting.charAt(5));
    }
    // due to try failing catch will run this is a StringIndexOutOfBoundsException error obj is our refrence to error
    catch(StringIndexOutOfBoundsException obj){
      System.out.println(obj.getMessage()); // get message prints the error in a good format with no extra stuff
    } 

  }
}

class twoDArrays {
// 2d arrays 
// {1,2,3} rows frist array
// {1,2,3}
// {1,21,3}
// 1s are column
// to create a 2d array we do type [][] name{}, type can be int etc first first [] for first array second [] for second array
// rows is first index column is second index int [y][x] arrayname
// index of 21 is int[2][1] [first array element 2 (array number 3)] [second array elemet 1 (elemet 1 in array 3)]

  public static void Int(String[] args) {

    int[][] numbers = {{1, 3, 5, 4}, 
                      {9, 11, 13, 14}, 
                      {17, 19, 21, 24}
                      };

    System.out.println(numbers[2][1]);
    // array length is is 4 elemets there are objects in those elemets but length of array numbers is # of rows
    System.out.println(numbers.length); // number of rows .. and number of smaller arrays stored by

    System.out.println(numbers[0].length); //number of columns

    // in the commenst below by "array" i mean the array in the array numbers think of arrays as subarrays
    // print out all elements of the array do a for loop in a for loop 
    // first for loop goes over each row adn second loop goes over each element in a the row one by one
    // first for loop selects row 1 "array 1" then second for loop starts now from the selected array "array 1 index 0" 
    // second loop cycles through the elements with the for loop printing each element. after both for loop run
    // first for loop runs again index ++ happens so now array 2 index 1 is selected and second loop prints the
    // array 2s elemets this will go on untill all arrays are done i<numlen all indexs in num are done
    // as for each arrays elemets it will print until j<numbers[0].len this works as all arrays are equal in numbers 

    for(int i=0; i < numbers.length; i++){ // loops over the rows first arrays
      System.out.println("Printing out row "+i);
      for(int j=0; j < numbers[0].length; j++) { // loops over the columns, or the values in each row (in each array)
        System.out.print(numbers[i][j]+" ");
      }
    }
  }
    //System.out.println(nums);
  /*
    for(int i=0; i<nums.length; i++) {
      System.out.println(nums[i]);
    };*/

}

class fun{
  public static void main(String[] args){
    int [] numbers = {2,5,8,3,9,4,1};
    System.out.print(numbers[1]);

  }
} 
// test

