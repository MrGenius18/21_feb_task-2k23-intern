'''
Remove duplicate  elements from list
'''

l1 = [12,45,23,98,45,26,78,12,89]

for i in l1:
    count = l1.count(i)
    if count>1:
        for j in range (count-1):
            l1.remove(i)
print(l1)


