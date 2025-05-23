# -*- coding: utf-8 -*-
"""aula6_facul.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NRf-nzq_eWgTXo22fSKewmWOU_qJubD1
"""

from scipy.stats import norm

mu = 100  # média
sigma = 15  # letra grega para desvio padrão

# 100% => 1
# 68%  => 0,68
# 0.0912 => 9,12%

# O CDF CALCULA A PROBABILIDADE ACUMULADA
prob_normal = 1 - norm.cdf(120, mu, sigma) # PROBABILIDADE ACUMULADA
print(f"Probabilidade de comprimento > 120 mm: {prob_normal:.4f}")

# Parâmetros da distribuição
mu = 5       # média
sigma = 0.2  # desvio padrão
x = 5.3      # valor para calcular a probabilidade

# Calcula a probabilidade de X > 5.3
prob = norm.sf(x, mu, sigma)  # sf = survival function = 1 - cdf

print(f"A probabilidade de um tubo ter diâmetro maior que {x} cm é aproximadamente {prob:.4f} ou {prob*100:.2f}%")

mu = 5       # média
sigma = 0.2  # desvio padrão
x1 = 4.5
x2 = 5.5

# Probabilidade de X < 4.5
p1 = norm.cdf(x1, mu, sigma)

# Probabilidade de X > 5.5
p2 = norm.sf(x2, mu, sigma)

# Soma das duas regiões
total_prob = p1 + p2

print(f"Probabilidade de diâmetro < {x1} cm ou > {x2} cm: {total_prob:.4f} ou {total_prob*100:.2f}%")

# Parâmetros
mu = 500     # média
sigma = 10   # desvio padrão

# Cálculo dos limites inferior e superior (95%)
limite_inferior = norm.ppf(0.025, mu, sigma)
limite_superior = norm.ppf(0.975, mu, sigma)

print(f"Limite inferior: {limite_inferior:.2f} mg")
print(f"Limite superior: {limite_superior:.2f} mg")

mu = 5
sigma = 0.2

# Limites do intervalo de confiança de 90%
limite_inferior = norm.ppf(0.05, mu, sigma)
limite_superior = norm.ppf(0.95, mu, sigma)

print(f"Limite inferior: {limite_inferior:.4f}")
print(f"Limite superior: {limite_superior:.4f}")