import random 

def gerar_usuario():
    new_user = []

    letra_maiuscula = chr(random.randint(65, 90))
    new_user.append(letra_maiuscula)
    qtd_letras = 0
    
    while True:
        if qtd_letras < 4:
            letra_minusucla = chr(random.randint(97, 122))
            new_user.append(letra_minusucla)
            qtd_letras += 1
        else:
            break

    numero = chr(random.randint(48,57))
    new_user.append(numero)

    return "".join(new_user)
new_user = gerar_usuario()

def gerar_senha():
    
    senha = []
    
    letra_maiuscula = chr(random.randint(65, 90))
    senha.append(letra_maiuscula)
    
    qtd_letras = 0
    
    while True:
        if qtd_letras < 4:
            letra_minusucla = chr(random.randint(97, 122))
            senha.append(letra_minusucla)
            qtd_letras += 1
        else:
            break
    
    numero = chr(random.randint(48, 57))
    senha.append(numero)
    
    caractere_especial = random.choice("!#$&_")
    senha.append(caractere_especial)

    return "".join(senha)
senha = gerar_senha()

print('\nUSUARIO:', new_user)
print('SENHA:', senha) 
print('esse é um usuario e senha \033[1m temporarios\033[0m troque assim que puder! \n')

