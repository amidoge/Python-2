#Multiple Word Palindromes
#Ex 72 extended

word = input("Word: ")
new = []
o = []
r = []
#canceling out the spaces
for i in range(len(word)):
    if word[i] in ".,?!" or word[i] == ' ':
        pass
    else:
        new.append(word[i])

#original
for i in range(len(new)):
    o.append(new[i])
#reverse
for i in range(len(new)):
    r.append(new[-i - 1])

print(new)
print(o)
print(r)
same_count = 0
for i in range(len(new)):
    if o[i] == r[i]:
        same_count += 1
    else:
        pass

if same_count == len(new):
    print("Palindrome")
else:
    print("Non Palindrome")