def serie_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return serie_lucas(n-1) + serie_lucas(n-2)
    
print(serie_lucas(5))