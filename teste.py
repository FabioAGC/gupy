1-)def fibonacci(n):
    fib_sequence = [0, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > n:
            break
        fib_sequence.append(next_value)
    return fib_sequence

def verifica_fibonacci(num):
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)
"""
2-)

def verifica_letra_a(texto):
    # Convertendo o texto para minúsculas para facilitar a verificação
    texto = texto.lower()
    contagem = texto_lower.count('a')
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."

texto_input = input("Informe uma string: ")
resultado = verifica_letra_a(texto_input)
print(resultado)

3-)78

4-)9
128
49
100
13
20

5-)

Ligue o primeiro interruptor por 20 minutos
depois dos 20 minutis desligar o primeiro interruptor e ligar o segundo interruptor.

Primeira sala: se a lampada estiver quente e apagada é a controlada pelo primeiro interruptor , se estiver acessa é a controlada pelo segundo e se 
estiver apagada e fria é do controlada pelo terceiro interruptor

Segunda sala: mesmo processo da primeira , definindo 2 lampadas a da terceira sala se descobre por eliminação 

"""