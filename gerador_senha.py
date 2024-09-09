
"""
Gerador de Senha Aleatória - Versão 1.97
Este programa gera uma senha aleatória com o comprimento definido pelo usuário, 
utilizando letras, números e caracteres especiais.

Autor: Prof. Sauer
Site: www.sauer.pro.br
Redes sociais:
Email: sauer@simplificatreinamentos.com.br
Instagram: https://www.instagram.com/prof.alesauer/
Facebook: https://www.facebook.com/prof.alesauer/
YouTube:  https://www.youtube.com/@prof.alesauer
LinkedIn: www.linkedin.com/in/alesauer
"""

import random
import string

def gerar_senha(comprimento):
    """
    Gera uma senha aleatória com o comprimento especificado.
    
    Parâmetros:
    comprimento (int): O comprimento da senha a ser gerada.
    
    Retorna:
    str: A senha gerada.
    """
    # Conjunto de caracteres: letras, números e pontuações.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha com o número de caracteres fornecido pelo usuário.
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha

# Solicita ao usuário o comprimento da senha.
comprimento = int(input('Digite o comprimento da senha desejada: '))

# Chama a função para gerar a senha.
senha = gerar_senha(comprimento)

# Exibe a senha gerada.
print(f'Sua senha gerada é: {senha}')
