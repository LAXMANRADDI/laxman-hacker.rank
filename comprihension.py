You are given:
x, y, z: Dimensions of a cuboid.
n: A number that the sum (i + j + k) should not be equal to.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x + 1) #  
          for j in range(y + 1) 
          for k in range(z + 1) 
          if (i + j + k) != n]

print(result)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 to find the runner up score


    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(set(arr))[-2])


^^^^^^^^^^^^^^^^^^^^^^^^^ 
hackerrank sluotion for  finding names with same score i.e second lowest score 

    students = [] # empty list 
    for _ in range(int(input())): 
        name = input()
        score = float(input())
        students.append([name, score]) # storing nested lists  

    
    scores = [s[1] for s in students] # fetching scores of all students were at index 1
    unique_scores = sorted(set(scores)) #sorting em removing dupicate values
    second_lowest = unique_scores[1] #fetching second lowest score of athe student
    result = [s[0] for s in students if s[1] == second_lowest] 
    for name in sorted(result):
        print(name)

