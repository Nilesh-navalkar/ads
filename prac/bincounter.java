
public class bincounter
{
    static int counter[]=new int[8];
    public static void increment(){
        if(counter[counter.length-1]==0)
        {
            counter[counter.length-1]=1;
        }
        else{
            int j=counter.length-1;
            while(counter[j]!=0)
            {
                counter[j]=0;
                j=j-1;
            }
            counter[j]=1;
        }
    }
	public static void main(String[] args) {
	    increment();
	    increment();
	    increment();
	    increment();
	    for(int i=0;i<counter.length;i++)
		System.out.print(counter[i]+" ");
	}
}
