
x = int(input())
text=[]
for i in range(x):
    t = input()
    text.append(t)

words = []
w = ''
for t in text :

    x = t.split(' ')


    for i in x :
        if i[0].isdigit() :
            w = w + i[0]
        elif i[0].isupper():
            w = w + i[0]
    words.append(w)

    w=''
def s(e):
    return len(e)
words.sort()
words.sort(reverse=True,key=s)

for i in words :
    print(i)
    
