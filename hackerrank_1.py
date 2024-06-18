s1="mus"
s2="keyboard"
# if any cahrecrwe
answer=""

for char in s1:
    print(char)
    if char in s2:
        answer="YES"
        break

if not answer:
    answer="NO"

print(answer)
