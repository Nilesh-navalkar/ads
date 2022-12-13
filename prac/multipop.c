#include <stdio.h>
int stack[7];
int top=-1;
void push(int ele){
    if(top>=6){
        printf("isfull\n");
    }
    else{
        stack[++top]=ele;
    }
}
int pop()
{
    if (top==-1){
        printf("isEmpty\n");
    }
    else{
        return stack[top--];
    }
    
}
void multipop(int n){
    int j;
    if (n<top+1){
        j=n;
    }
    else{
        j=top+1;
    }
    for(int i=0;i<j;i++){
        printf("%d\n",pop());
    }
}
int main()
{
    push(1);
    push(2);
        push(3);
    push(4);
        push(5);
    push(6);
        push(7);
    push(8);

    multipop(5);
    for(int i=0;i<=top;i++){
        printf("%d ",stack[i]);
    }
    return 0;
}
