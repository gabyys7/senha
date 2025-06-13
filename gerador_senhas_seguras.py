
import random
import string

def gerar_senha(segura=True, tamanho=16):
    """Gera uma senha segura com letras, números e símbolos."""
    if segura:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        caracteres = string.ascii_lowercase + string.digits
    senha = ''.join(random.SystemRandom().choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("🔐 Gerador de Senhas Seguras")
    qtd = int(input("Quantas senhas deseja gerar? "))
    tam = int(input("Qual o tamanho das senhas? (Recomendado: 12-20) "))
    for i in range(qtd):
        print(f"Senha {i+1}: {gerar_senha(tamanho=tam)}")
