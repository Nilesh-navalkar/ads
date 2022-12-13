class node{
    char c;
    node next[]=new node[26];
    int end=0;
}

public class tries 
{
    static node root=new node(); 
    public static void printnode(node r){
        int i=0;
        while(i<26){
            if(r.next[i]!=null){
            System.out.println(r.next[i].c);
            r=r.next[i];
            i=0;
            }
            else
            i=i+1;
        }
        
    }
    public static node insert(String s){
        node temp=root;
        char[] ch = s.toCharArray();
        for(int i=0;i<ch.length;i++){
            int index=(int)ch[i]-97;
            //System.out.println(root.next[index]);
            
            if(root.next[index]==null){
                node k= new node();
                k.c=ch[i];
                if(i==ch.length-1){
                    k.end=1;
                }
                root.next[index]=k;
                root=root.next[index];
            }
            else{
                root=root.next[index];
            }
        }
        return temp;
    }
    public static boolean search(String s){
        node temp=root;
        char[] ch = s.toCharArray();
        for(int i=0;i<ch.length;i++){
            int index=(int)ch[i]-97;
            if(temp.next[index]!=null){
                temp=temp.next[index];
                if((i==ch.length-1) && (temp.end==1)){
                    return true;
                }
            }
            else{
                return false;
            }
        }
        return false;
    }
    public static node delete(String s){
        node temp=root;
        char[] ch = s.toCharArray();
        for(int i=0;i<ch.length;i++){
            int index=(int)ch[i]-97;
            if(root.next[index]!=null){
                root=root.next[index];
                if((i==ch.length-1) && (root.end==1)){
                    root.end=0;
                    return temp;
                }
            }
            else{
                return temp;
            }
        }
        return temp;
    }
	public static void main(String[] args) {
        String arr[]= {"hel","hello","helu","this","these"};
        
        for(int i=0;i<arr.length;i++)
        root=insert(arr[i]);
        //printnode(root);
        System.out.println(search("hel"));
        //printnode(root);
        root=delete("hel");
        System.out.println(search("hel"));
		
	}
}
