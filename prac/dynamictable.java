import java.io.*;
import java.util.*;

public class dynamictable
{
    static int top=-1; 
    public static int[] add(int x, int arr[])
    {
        if(top+1>= arr.length){
            int newarr[]=new int[2*arr.length];
            for(int i=0;i<arr.length;i++)
            {
                newarr[i]=arr[i];
            }
            arr=newarr;
        }
        arr[++top]=x;
        return arr;
   }
	public static void main(String[] args) {
	    int arr[]=new int[1];
	    arr=add(5,arr);
	    //arr=add(10,arr);
	    //arr=add(11,arr);
	    //arr=add(12,arr);
	    //arr=add(13,arr);
	    for(int i=0;i<arr.length;i++)
		System.out.print(arr[i]+"\t");
	}
}
