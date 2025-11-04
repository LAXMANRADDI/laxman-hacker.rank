You are given:
x, y, z: Dimensions of a cuboid.
n: A number that the sum (i + j + k) should not be equal to.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if (i + j + k) != n]

print(result)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 to find the runner up score


    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(set(arr))[-2])

