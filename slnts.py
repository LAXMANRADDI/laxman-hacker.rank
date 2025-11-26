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


2 ] Problem Statement You are given,An integer n A list of n integerYou must create a tuple from these integers and print the hash value of the tuple. 

soln :
n = int(input())
numbers = tuple(map(int, input().split())) 
print(hash(numbers))
^^^^^^^^^^^^^^^^^^^^

3] swapping case problem :

n = int(input())
numbers = tuple(map(int, input().split()))
print(hash(numbers)) 
input :   HackerRank.com presents "Pythonist 2".
output:   hACKERrANK.COM PRESENTS "pYTHONIST 2" 
or 
 def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        else:
            result += ch.lower()
    return result 
 or 

if they said (without using .upper(), .lower(), or .swapcase()).   let's us ascii values and swap chars.
def swap_case_ascii(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 97 <= ascii_val <= 122:       # lowercase a-z
            result += chr(ascii_val - 32)
        elif 65 <= ascii_val <= 90:      # uppercase A-Z
            result += chr(ascii_val + 32)
        else:
            result += ch                 # other characters unchanged
    return result
 refernce :
s = "Hello"
for ch in s:
    print(f'"{ch}" "{ord(ch)}"', end=' ')
input :
output :"H" "72" "e" "101" "l" "108" "l" "108" "o" "111"


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4 ] full nmae using f string
def print_full_name(first, last):
  print(f"Hello {first} {last}! You just delved into python." )

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



 5]We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).Let's try to understand this with an example.
 You are given an immutable string, and you want to make changes to it.
soln :

def mutate_string(string, position, character):
    return string[:position]+ character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new) 

or 
using controlled replace()   function :

def mutate_string(string, position, character):
    old = string[position]      # old character at the position
    temp = string[position:].replace(old, character, 1)
    return string[:position] + temp 

input :
abracadabra
5 k
output  :
abrackdabra

