import java.io.*;
import java.util.*;

public class countminsketch{
    public static int h1(int ele){
        return (5*ele+2)%7;
    }
    public static int h2(int ele){
        return (89*ele+27)%7;
    }
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        Hashtable<Integer, Integer> ht1 = new Hashtable<>(7);
        Hashtable<Integer, Integer> ht2 = new Hashtable<>(7);
        for(int i=0;i<7;i++){
            ht1.put(i,0);
            ht2.put(i,0);
            }
            
        int choice=1;
        while(true){
            if(choice==1)
            {
                System.out.print("Enter element to insert : ");
                int ele=sc.nextInt();
                int a=h1(ele);
                int b=h2(ele);
                System.out.println("hash values are : "+a+ " ," +b);
                ht1.put(a,ht1.get(a)+1);
                ht2.put(b,ht2.get(b)+1);
                System.out.println("element inserted \n");
                choice=-1;
            }
            else if(choice==2){
                System.out.println(ht1);
                System.out.println(ht2);
                choice=-1;
            }
            else if(choice ==-1){
                System.out.println("*****1==insert\t 2==print ht\t4==count\t 3==exit*****");
                System.out.print("enter choice : ");
                choice=sc.nextInt();
            }
            else if(choice==3){
                break ;
            }
            else if(choice==4){
                System.out.print("Enter element to count : ");
                int ele=sc.nextInt();
                int a=h1(ele);
                int b=h2(ele);
                System.out.println("hash values are : "+a+ " ," +b);
                System.out.println("Hashtable values at above hash values are : "+ht1.get(a)+ " ," +ht2.get(b));
                System.out.println("count of  : "+ele+ " is : " + Math.min(ht1.get(a),ht2.get(b)));
                choice=-1;
            }
            
        }
        
    }

}