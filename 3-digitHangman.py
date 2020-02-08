pb = []
guestnum = []
display = ['_','_','_','_','_','_','_','_','_','_','_','_']

wrong = []
check=0
def Show(list):
    for i in list:
        print(i,'',end='')
        print('',end='')
def check_point(list):
    point=12
    for i in list:
        if i =='_':
            point-=1
    return point


pb = input().split(maxsplit=12)
guestnum = [input() for i in range(5)]

Show(display)
print('')
for i in range(5):
    for j,it in enumerate(pb):
        if guestnum[i] == it :
            display[j]=guestnum[i]
            check=1
    Show(display)
    if check==0:
        wrong.append(guestnum[i])
    check=0
    Show(wrong)
    print('')

print(check_point(display))   
