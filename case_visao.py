import math # uso do método atan

def main():
    #lendo a imagem de um dispositivo
    M = read_image()

    #você tem que dar o valor correto às duas variáveis abaixo.
    #cone_x e cone_y são os pontos x e y, respectivamente, do centro
    #do retângulo que encobre completamente o cone.
    cone_x, cone_y = 0, 0

    #bônus: dê valor corretamente à variável abaixo
    hor_angle = 0.0

    #----COMPLETE O CÓDIGO AQUI-----

    # Torna branco os pixels originalmente laranja e os outros ficam pretos
    M = threshold(M, 255, 97, 27)

    # atribui os pontos dos retângulos que cercam as manchas brancas da matriz M
    points = blob(M)

    for point in points:
        x, y, w, h = point

        """
        Analisando a imagem, percebemos que o cone logicamente
        tem a altura (h) maior que a base (w). Já os garis, têm a base (w)
        muito maior que a altura (h). Dessa forma, podemos diferenciá-los
        achando qual é o maior lado, a base ou a altura.
        """

        if h > w: # altura maior que a base, logo é cone.
            cone_x = x + (w/2) # eixo x é o canto superior esquerdo mais a metade da largura
            cone_y = y + (h/2) # eixo y é o canto superior esquerdo mais a metade da altura

    #---- Parte extra do algoritmo

    # encontrando o centro da imagem
    centro_x = 640/2
    centro_y = 480/2

    """
    Por relações de trigonometria, temos que a tangente do hor_angle é
    (cone_y - centro_y) / (centro_x - cone_x) levando em conta um ângulo
    positivo entre 0 e Pi/2. Dessa forma, temos que hor_angle é o arco tangente
    dessa relação.
    """

    tan = (cone_y - centro_y) / (cone_x - centro_x)

    if tan < 0: # tangente negativa
        hor_angle = math.atan(-tan)
    else:
        hor_angle = math.atan(tan)

    #-------------------------------

if __name__ == "__main__":
    main()
