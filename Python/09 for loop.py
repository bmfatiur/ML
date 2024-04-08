exp=[2340,2500,2100,3100,2980]
total=0
for i in exp:
    total+=i
print(total)

# another way
total=0
for i in range(len(exp)):
    total+=exp[i]
print(total)

# using while loop
i=0
while i<5:
    print(i+1)
    i+=1
