# Замість коду на C тут код на Python

import math

def step(xx, nn):
    if nn == 0:
        return 1
    s = 1
    for _ in range(nn):
        s *= xx
    return s

# Цільова функція Розенброка
def F(X):
    return step((1 - X[0]), 2) + 100.0 * step((X[1] - X[0] ** 2), 2)

def Investigating_Search_Full(X0, X1, deltaX, eps, q, n):
    for i in range(n + 1):
        X1[i] = X0[i]
    for i in range(n + 1):
        while deltaX[i] > eps:
            X1[i] = X0[i] + deltaX[i]
            if F(X1) < F(X0):
                break
            else:
                X1[i] = X0[i] - deltaX[i]
                if F(X1) < F(X0):
                    break
                else:
                    deltaX[i] /= q
                    X1[i] = X0[i]

def Investigating_Search_Simple(X0, X1, deltaX, n):
    for i in range(n + 1):
        X1[i] = X0[i]
    for i in range(n + 1):
        X1[i] = X0[i] + deltaX[i]
        if F(X1) < F(X0):
            continue
        else:
            X1[i] = X0[i] - deltaX[i]
            if F(X1) >= F(X0):
                X1[i] = X0[i]

def Difference(X, Y, eps, n):
    max_diff = max(abs(Y[i] - X[i]) for i in range(n + 1))
    return max_diff < eps

def Sample_Search(X0, X1, X2p, p, n):
    for i in range(n + 1):
        X2p[i] = X0[i] + p * (X1[i] - X0[i])

def main():
    output = open("output.txt", "w")
    k = 0
    kmax = 1000  # Обмежена максимальна кількість ітерацій
    eps1 = 1e-5  # Налаштовано значення для точності
    eps2 = 1e-5
    q = 2
    p = 2
    n = 1
    
    deltaX = [0.01] * (n + 1)
    X0 = [0.0] * (n + 1)
    X1 = X0[:]
    X2p = [0.0] * (n + 1)
    X2 = [0.0] * (n + 1)
    
    while k < kmax:
        k += 1
        X0, deltaX = X1[:], [0.01] * (n + 1)
        
        Investigating_Search_Full(X0, X1, deltaX, eps1, q, n)

        # Записувати тільки унікальні точки
        if not Difference(X0, X1, eps2, n):
            output.write(f"{X1}\n")

        if Difference(X0, X1, eps2, n):
            break

    output.close()
    print(f"Кількість кроків: {k}")

main()


