f = open('names.txt','r')
w = f.read()
w = w.split('","')
w.sort()
print(w)
#print(w)
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sum41s = []

for word in w:
    sum = 0
    for letter in word:
        sum += alph.index( letter ) + 1
    sum41s.append( sum )
print( 'sum41')
print( sum41s )

print( 'sum41 multiply')
multiarray = []
for ind in range( len(sum41s)):
    multiplier = ind + 1
    multiarray.append( sum41s[ind]*multiplier )

print( multiarray )
ans = 0
for sum42 in multiarray:
    ans += sum42 
print('Ответ  :','\n',ans)   #871853874
f.close
