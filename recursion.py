############# Simple recursion(Top down approach) #######################

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


# a = fibo(5)
# print(a)


########### use concept of memoization(Top down approach) ############ 


def fibo1(n):
    dp = [-1]*(n+1)
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]


# a = fibo1(40)
# print(a)


################# Tabulation Method(bottom up approach) #################

def fibo2(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    print(dp)


# a = fibo2(100)
# print(a)



################## Space optimization in Tabulation method if possible #######################


def fibo3(n):
    # dp = [-1]*(n+1)
    prev2 = 0
    prev1 = 1
    
    for _ in range(2,n+1):
        print(prev1,prev2) 
        cur = prev1 + prev2
        prev2 = prev1 
        prev1 = cur
           
    return prev1

a = fibo3(5)
print(a)
