 Command     Action                         
 insert i e  Insert `e` at index `i`        
print       Print the list                 
 remove e    Remove first occurrence of `e` 
append e   Add element at end            
 sort       Sort list                      
 pop         Pop last element               
 reverse     Reverse the list          
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 soln:
if __name__ == '__main__':
    lst =[]
    N = int(input())
for i in range(N):
    command = input().split()
    op = command[0]
    
    if op == "insert":
        lst.insert(int (command[1] ) , int (command[2]))
        print (lst) 
    elif op ==  "remove" :
        lst.remove(int("command[1]"))
    elif op == "append" :
        lst.append(command[1])
    elif op =="sort":
        lst.sort()
    elif op =="pop"               :
        lst.pop()
    elif op == "reverse":
        lst.reverse()
