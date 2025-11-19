from auxiliares import *

def rsa_key_gen(l=1024):
    """
    Gera o par de chaves RSA conforme o Algoritmo 1.1 do livro "Guide to Elliptic Curve Cryptograph".
    :param l: O parâmetro de segurança (bitlength do módulo n).
    """
    # Configura o bitlength para os primos p e q
    bitlength_pq = l // 2

    print(f"--- Gerando chaves RSA com N de {l} bits (Primos de {bitlength_pq} bits) ---")

    # 1. Seleciona aleatoriamente dois primos p e q.
    p = generate_prime(bitlength_pq)
    q = generate_prime(bitlength_pq)
    
    while p == q: # Garante que os primos são distintos
        q = generate_prime(bitlength_pq) 

    print(f"1. Primos (p, q) selecionados: ({p}, {q})")
    
    # 2. Calcula N = pq e phi = (p-1)(q-1).
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"2. Módulo n (Chave Pública): {n}")
    print(f"2. Totiente phi: {phi}")

    # 3. Seleciona um inteiro e arbitrário com 1 < e < phi e mdc(e, phi) = 1.
    e = 65537  # O valor mais comum para e
    
    if e >= phi or math.gcd(e, phi) != 1:
        # Fallback se phi for muito pequeno para o 65537 (apenas para demonstração)
        e = 3
        while math.gcd(e, phi) != 1 and e < phi:
            e += 2
        if e >= phi:
            raise ValueError("Não foi possível encontrar um expoente e válido.")

    print(f"3. Expoente Público e: {e}")

    # 4. Calcula o inteiro d que satisfaz 1 < d < phi e ed = 1 (mod phi).
    d = mod_inverse(e, phi)
    
    if d is None:
        raise ValueError("O inverso modular d não pôde ser calculado. Cheque phi.")

    print(f"4. Expoente Privado d: {d}")

    # 5. Retorna (n, e, d).
    return n, e, d