# def fact(n:int):
#     '''
#     fact(5) = 5 * 4 * 3 * 2 * 1
#             = n * fact(n-1) * fact((n-1)-1)
#     '''

#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
    
#     return n*fact(n-1)

# print(fact(1000))



# def fact(n:int):
#     '''
#     fact(5) = 5 * 4 * 3 * 2 * 1
#             = n * fact(n-1) * fact((n-1)-1)
#     '''
#     memo = {1:1,2:2}
#     if n  in memo:
#         return memo[n]
    
#     memo[n] = n*fact(n-1)
#     return memo[n]

# print(fact(10))



def fact(n:int):
    '''
    fact(5) = 5 * 4 * 3 * 2 * 1
            = n * fact(n-1) * fact((n-1)-1)
    '''
    if n == 0 or n == 1:
        return 1
    
    dp = [1] * (n + 1)  # Initialize an array to store factorials
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i  # Compute factorial iteratively
    
    return dp[n]

print(fact(100))
