#I should get the original string and a reversed string.
#Then I will compare the two.

word = input("Word: ")
o = []
r = []
for i in range(len(word)):
    o.append(word[i])
for i in range(len(word)):
    r.append(word[-i - 1]) #So that it would be -1, -2, and so on.

same_count = 0
print(o)
print(r)
for i in range(len(word)):
    if o[i] == r[i]:
        same_count += 1

if same_count == len(word):
    print("Palindrome")
else:
    print("Non Palindrome")