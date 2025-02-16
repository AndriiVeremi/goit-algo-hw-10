import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2

N = 10000  
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand <= f(x_rand)
monte_carlo_result = (b - a) * f(b) * np.sum(under_curve) / N

quad_result, error = spi.quad(f, a, b)

x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', alpha=0.3, s=1)
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Метод Монте-Карло для інтегрування f(x) = x^2')
plt.grid()
plt.show()


print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")
print(f"Інтеграл методом quad: {quad_result} (похибка {error})")