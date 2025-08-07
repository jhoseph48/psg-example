def par_impar(numeros):
    pares = []
    impares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

print(par_impar([2,3,4,5,6,8,6,5,7]))
