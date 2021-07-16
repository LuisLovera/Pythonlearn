def run():
    print(' Adivina la letra secreta (tienes 5 intentos).')
    
    intento=0
    
    while intento <5:
        letra=input('¿Cuál es la letra secreta? ')
        intento+=1
        if letra=='k':
            print('Acertaste la letra secreta, es la K.')
            break
        if intento==5:
            print('Lo siento. Perdiste')


if __name__=='__main__':
    run()