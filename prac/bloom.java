import java.io.*;
import java.util.*;

public class bloom{
    public static int h1(int ele){
        return (5*ele+2)%7;
    }
    public static int h2(int ele){
        return (89*ele+27)%7;
    }
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        Hashtable<Integer, Integer> ht = new Hashtable<>(7);
        for(int i=0;i<7;i++){
            ht.put(i,0);
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
                
                if((ht.get(a)==1) && (ht.get(b)==1)){
                    System.out.println("element already exists \n");
                }
                else{
                    ht.put(a,1);
                    ht.put(b,1);
                    System.out.println("element inserted \n");
                }
                choice=-1;
                
                
            }
            else if(choice==2){
                System.out.println(ht);
                choice=-1;
            }
            else if(choice ==-1){
                System.out.println("*****1==insert or search\t 2==print ht\t 3==exit*****");
                System.out.print("enter choice : ");
                choice=sc.nextInt();
            }
            else if(choice==3){
                break ;
            }
            
        }
        
    }

}