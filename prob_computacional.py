"""
    Código corrige a diferença de RPM entre os motores da direita
    e da esquerda quando o robô precisa andar em linha reta.
"""

# constante com o RPM total dos motores
RPM_TOTAL = 15435.2

# método main
def main():
    while True: # inicia laço que só acaba quando o sistema é desligado
        # recebe os sinais de controle (-100 a 100)
        esquerda = receberSinalControle(ESQUERDA)
        direita = receberSinalControle(DIREITA)

        if (esquerda == 0 and direita == 0):
            # caso de robô parado
            rotacionarMotores(ESQUERDA, esquerda)
            rotacionarMotores(DIREITA, direita)
        elif esquerda != -direita:
            # caso de robô fazendo curva
            rotacionarMotores(ESQUERDA, esquerda)
            rotacionarMotores(DIREITA, direita)
        else:
            # robô andando em linha reta
            # aqui precisa da correção

            # assumindo que o valor positivo é o sentido preferencial de
            # cada motor
            if direita > 0:
                # robô andando para frente, tendendo à esquerda
                # precisamos diminuir o sinal da direita, para compensar
                rpm_direita = rpmReal(direita) # rpm real a ser aplicado
                direita = (rpm_direita / RPM_TOTAL) * 100
            else:
                # robô andando para trás, tendendo à direita
                # precisamos diminuir o sinal da esquerda, para compensar
                rpm_esquerda = rpmReal(esquerda) # rpm real a ser aplicado
                esquerda = (rpm_esquerda / RPM_TOTAL) * 100

            # rotaciona os motores
            rotacionarMotores(ESQUERDA, esquerda)
            rotacionarMotores(DIREITA, direita)

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
