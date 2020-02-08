def testprime(n):
    c = 0
    for i in range(2,n):
        if n%i == 0 :
            c=c+1
       # print(i,n%i,c)
    if c==0:
        return True
    else:
        return False

def setnumtest(n):
    set_num = [float(n[:3])*10, float(n[:4])*100,float(n[:5])*1000]
    f_set_num = []
    for i in range(len(set_num)):
        f_set_num.append(int(set_num[i]))

    return f_set_num
while(1):
    x=input()
    if float(x) == 0.0:
        break
    x=setnumtest(x)
    c=0
    for i in x:
        if testprime(i):
            c+=1

    if c==0:
        print('FALSE')
    else:
        print('TRUE')
    
    

            
    
           
        
