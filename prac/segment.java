class node{
    int low;
    int high;
    int val;
    node right;
    node left;
}
public class segment
{
    static node root=new node();
    public static void inorder(node root){
        if (root!=null){
            inorder(root.left);
            //System.out.print("("+root.low+","+root.high+")");
            System.out.print(root.val+" ");
            inorder(root.right);
        }
    }
    public static void build(node root,int arr[]){
        node temp=root;
        if (temp.low!=temp.high){
            temp.left=new node();
            temp.left.val=0;
            temp.right=new node();
            temp.right.val=0;
            temp.left.low=temp.low;
            temp.left.high=(int)(temp.low+temp.high)/(int)(2);
            temp.right.low=1+(int)(temp.low+temp.high)/(int)(2);
            temp.right.high=temp.high;
            build(temp.left,arr);
            build(temp.right,arr);
        }
        else{
            temp.val=arr[temp.low];
        }
    }
    public static void enumerate(node root){
        if (root.val!=0){
            int tp=0;
        }
        else if (root.left.val!=0 && root.right.val!=0){
            root.val=root.left.val+root.right.val;
            System.out.println(root.val+ " ("+root.low+" "+root.high+")");
        }
        else{
            if (root.left!=null)
            enumerate(root.left);
            if (root.right!=null)
            enumerate(root.right);
        }
    }
    public static int query(int l,int h,node root){
        
        if (root.low>=l && root.high <=h){
            //System.out.println(root.val);
            return root.val;
        }
        else if(root.low==root.high && (root.low<l || root.high >h))
        return 0;
        else
         return query(l,h,root.left)+query(l,h,root.right);
    }
	public static void main(String[] args) {
	    int arr[]={1,2,3,4,5,6,7};
	    root.low=0;
	    root.high=arr.length-1;
	    build(root,arr);
	    //System.out.println(root.val);
	    while(root.val==0){
	        enumerate(root);
	    }
	    inorder(root);
	    int ans=query(1,5,root);
	    System.out.println("\n ans : "+ans);
	    
		//System.out.println(arr);
	}
}
