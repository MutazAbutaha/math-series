def fibo(n):
    '''  this function calculates the fibo for a number.
        :param => n:int
        :return => int
    '''
    if n == 0 or n==1 :
        return n
    if n > 1 :
        return fibo(n-1) + fibo(n-2)
    

def lucas(n):
    '''  this function calculates the lucas for a number.
        :param => n:int
        :return => int
    '''
    if n == 0 :
        return 2
    if n == 1 :
        return 1
    if n > 1 :
        return lucas(n-1) + lucas(n-2)
    

def sum_series(n, x = 0, y = 1):
    '''  this function calculates the sum series for a number.
        :params => n:int(required), x:int(optional), y:int(optional)
        :return => int
    '''
    if n == 0 :
        return x
    if n == 1 :
        return y
    if n > 1 :
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)