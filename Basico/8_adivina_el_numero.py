def juego(vidas):
    num_a = 5
    
    num = int(input('Ingresa un número: '))
    
    if num < 0 or num > 10:
        vidas -= 1
        print('Número invalido, pierdes una vida.')
        return vidas
    
    elif num_a > num:
        vidas -= 1
        print('El número ingresado no es valido, pierdes una vida.')
        return vidas
    elif (num_a == num):
        print('¡Es un empate!')
        
    else:
        print('¡Ganaste!')
def run():
    """
    El juego consiste en escribir un numero mayor al que genera el sistema en un rango del 1 al 10,
    tienes hasta 3 oportunidades de fallar al inicio.
    ¡Suerte!
    """
    
    vidas=3

    while(True):
        if vidas==0:
            print('Fin del juego')
        break
            
    vidas=juego(vidas)
    
    print('Te quedan '+str(vidas)+' vidas.')


if __name__=='__main__':
    run()