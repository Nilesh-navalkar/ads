class node{
    int low;
    int high;
    int max;
    node left;
    node right;
}
public class Main
{
    static node root= new node();
    public static node insert(int l,int h,node root){
                if (root == null) {
                    node n=new node();
                    n.low=l;
                    n.high=h;
                    n.max=h;
            return n;
        }
        if (l < root.low) {
            root.left = insert(l,h,root.left);
        }
        else {
            root.right = insert(l,h,root.right);
        }

        if (root.max < h) {
            root.max = h;
        }
        return root;
        
        
        
    }
    public static void search(int l,int h,node root){
        if (root == null) {
            // return a dummy interval range
            System.out.println("doesnt lie ");
            return;
        }
            if ((l> root.low && l < root.high) || (h > root.low && h < root.high)) {
            System.out.println("lies in :"+root.low+" "+root.high);
            return;
        }
            else if (root.left != null && root.left.max > l) {
            // the overlapping node may be present in left
            // child
            search(l,h,root.left);
        }
            else {
            search(l,h,root.right);
        }
    }
        public static void inOrder(node root)
    {
        if (root == null) {
            return;
        }
        inOrder(root.left);
        System.out.println(root.low+","+root.high+","+root.max);
        inOrder(root.right);
    }
	public static void main(String[] args) {
        root.low=15;
        root.high=20;
        root.max=20;
        root = insert(10, 30,root);
        root = insert(17, 19,root);
        root = insert(5, 20,root);
        root = insert(12, 15,root);
        root = insert(30, 40,root);
        inOrder(root);
        search(0,1,root);
        search(6,7,root);
		//System.out.println(root.left);
	}
}
