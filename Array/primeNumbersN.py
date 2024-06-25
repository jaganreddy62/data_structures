def primeNumbers(n):
    prime_list=[True]*(n+1)

    p=2
    while(p*p<=n):
        if prime_list[p]:
            for j in range(p*p,n+1,p):
                prime_list[j] = False
        p+=1
    for i in range(n):
        if prime_list[i]:
            print(i)



if __name__ =='__main__':
    primeNumbers(100)

