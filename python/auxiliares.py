#Inicialização
import numpy as np
import math
import random

# --- Funções Auxiliares Necessárias ---

def extended_gcd(a, b):
    """Implementa o Algoritmo de Euclides Estendido."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Calcula o inverso modular a^-1 mod m ."""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        # O inverso não existe se gcd(a, m) != 1
        return None 
    # Garante que o resultado seja positivo
    return (x % m + m) % m

def is_prime(n):
    """Teste de primalidade simplificado (para demonstração)."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits):
    """Gera um número primo com o número de bits especificado."""
    # Define o intervalo para o número primo
    lower_bound = 2**(bits - 1)
    upper_bound = 2**bits - 1
    
    # Gera um número ímpar aleatório
    p = random.randrange(lower_bound, upper_bound) | 1 
    
    while not is_prime(p):
        p += 2 # Testa o próximo ímpar
    return p



