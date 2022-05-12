from random import randint

sum = 0

for i in range(10):
    for j in range (10): 
        rand = randint(0, 9)
        sum += rand
        print (rand, end = ' ')
    print("\n")
print(sum)