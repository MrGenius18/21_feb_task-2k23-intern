'''
Find palindrome name from list and store it into another list
'''

l = ["pinjal","madam","abcba","naman","king","ginig"]

newL = []

for i in l:
    if i == i [::-1]:
        newL.append(i)
print(f"New palindrome list is ==> {newL}")

