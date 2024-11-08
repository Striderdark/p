K,M = map(int,input().split(' '))

l_elements = []
sum = 0

for i in range(K):  
    l_elements.append(list(map(int,input().split(" "))))
    l_elements[i].pop(0)
    l_elements[i] = max(l_elements[i])
for i in range(K):
    sum += l_elements[i]**2
#    print(l_elements[i])
 #   print(sum)
print(l_elements)
sum = sum % M
print(sum)
