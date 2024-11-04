import math
import matplotlib.pyplot as plt
import numpy as np

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

def Difference(X, Y, eps, n):
    max_diff = max(abs(Y[i] - X[i]) for i in range(n + 1))
    return max_diff < eps

def main():
    k = 0
    kmax = 1000  # Обмежена максимальна кількість ітерацій
    eps1 = 1e-5  # Налаштовано значення для точності
    eps2 = 1e-5
    q = 2
    n = 1
    
    deltaX = [0.01] * (n + 1)
    X0 = [0.0] * (n + 1)
    X1 = X0[:]
    points = []  # Список для зберігання точок

    with open("output.txt", "w") as output:
        while k < kmax:
            k += 1
            X0, deltaX = X1[:], [0.01] * (n + 1)
            
            Investigating_Search_Full(X0, X1, deltaX, eps1, q, n)
            points.append(X1[:])  # Зберігаємо кожну точку

            # Записуємо координати у файл
            output.write(f"{X1}\n")

            if Difference(X0, X1, eps2, n):
                break

    # Побудова графіку
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-1, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = (1 - X) ** 2 + 100 * (Y - X ** 2) ** 2

    plt.figure(figsize=(10, 6))
    plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 35), cmap="viridis")
    points = np.array(points)
    plt.plot(points[:, 0], points[:, 1], 'ro-', markersize=4, label="Прохід алгоритму")
    plt.plot(1, 1, 'b*', markersize=10, label="Мінімум (1, 1)")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Прохід алгоритму оптимізації Розенброка")
    plt.legend()
    plt.show()

main()
