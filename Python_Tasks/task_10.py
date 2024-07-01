list=[5,8,12,15,20]
i=0
while i < len(list):
    square=list[i]**2
    print(f'Square of {list[i]} is {square}')
    i+=1
for j in list:
    cube=j**3
    print(f'cube of {j}is {cube}')
print("Odd numbers from 1 to 1000 : ")
for num in range(1,1000,2):
    print(num,end="")
    print("\n")
