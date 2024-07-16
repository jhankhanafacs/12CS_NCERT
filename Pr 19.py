#19.	Write a Python program to implement a stack using list. 


def isempty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
    if len(stk)==0:
        top=None
    else:
        top=len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print('stack is empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-top')
        for i in range(top-1,-1,-1):
            print(stk[i])

#Driver Code
            
def main():    
    stk=[]
    top=None
    while True:
        print('''stack operation
                 1.push
                 2.pop
                 3.peek
                 4.display
                 5.exit''')
        choice=int (input('enter choice:'))
        if choice==1:
            item=int(input('enter item:'))
            push(stk,item)
        elif choice==2:
            item=pop(stk)
            if item=="underflow":
                print('stack is underflow')
            else:
                print('poped')
        elif choice==3:
            item=peek(stk)
            if item=="underflow":
                print('stack is underflow')
            else:
                print('top most item is:',item)
        elif choice==4:
            display(stk)
        elif choice==5:
            break
        else:
            print('invalid')
            exit()
main()
 
