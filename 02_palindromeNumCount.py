'''
Find palindrome name from list "number" count
'''

l = ["pinjal","madam","abcba","naman","king","ginig"]

count = 0
for i in l:
    if i == i[::-1]:
        count+=1
print(f"Total palindrome name is {count}")

