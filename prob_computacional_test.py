"""
    Código corrige a diferença de RPM entre os motores da direita
    e da esquerda quando o robô precisa andar em linha reta.

    ps: Código apenas para fazer testes de algoritmo
"""

# constante com o RPM total dos motores
RPM_TOTAL = 15435.2

# método main
def main():
    # recebe os sinais de controle (-100 a 100)
    esquerda = float(input("Sinal esquerda [-100, 100]: "))
    direita = float(input("Sinal direita [-100, 100]: "))

    if (esquerda == 0 and direita == 0):
        # robô parado
        print("Robô parado")

        #rotacionarMotores(ESQUERDA, esquerda)
        #rotacionarMotores(DIREITA, direita)
    elif esquerda != -direita:
        print("Robô fazendo curva")
        print("Esquerda: %d" %(esquerda))
        print("Direita: %d" %(direita))

        #rotacionarMotores(ESQUERDA, esquerda)
        #rotacionarMotores(DIREITA, direita)
    else:
        # robô andando em linha reta
        # aqui precisa da correção
        print("Robô andando em linha reta")

        # assumindo que o valor positivo é o sentido preferencial de
        # cada motor
        if direita > 0:
            # robô andando para frente, tendendo à esquerda
            # precisamos diminuir o sinal da direita, para compensar
            print("Robô andando para frente")

            rpm_direita = rpmReal(direita) # rpm real a ser aplicado
            direita = (rpm_direita / RPM_TOTAL) * 100

            print("RPM direita: %.1f" %(rpm_direita))
        else:
            # robô andando para trás, tendendo à direita
            # precisamos diminuir o sinal da esquerda, para compensar
            print("Robô andando para trás")

            rpm_esquerda = rpmReal(esquerda) # rpm real a ser aplicado
            esquerda = (rpm_esquerda / RPM_TOTAL) * 100

            print("RPM esquerda: %1.f" %(rpm_esquerda))

        # rotaciona os motores
        #rotacionarMotores(ESQUERDA, esquerda)
        #rotacionarMotores(DIREITA, direita)

        print("Sinal esquerda: %.1f" %esquerda)
        print("Sinal direita: %.1f" %direita)

"""
    Função que retorna o rpm real que deverá ser aplicado
    ao motor que rotaciona mais para compensar o menor rpm
    do motor oposto

    A entrada da função é o sinal positivo do motor que rotaciona
    mais: (0, 100]
"""
def rpmReal(sinal):
    rpm = sinal * RPM_TOTAL / 100
    percentual_total = (rpm/RPM_TOTAL)*100

    if percentual_total > 0 and percentual_total < 10:
        return rpm
    elif percentual_total >= 10 and percentual_total < 50:
        return rpm * (1 - (0.5/100))
    elif percentual_total >= 50 and percentual_total < 60:
        return rpm * (1 - (2.5/100))
    elif percentual_total >= 60 and percentual_total < 90:
        return rpm * (1 - (3.2/100))
    elif percentual_total >= 90 and percentual_total < 100:
        return rpm * (1 - (5/100))
    else: # percentual_total == 100
        return rpm * (1 - (5.9/100))

if __name__ == "__main__":
    main()
