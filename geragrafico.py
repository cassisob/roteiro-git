from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt
 
def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.plot(valores)
    plt.show()

    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')

    plt.title('Gráfico de linhas')

    i = 1
    for serie in valores:
        plt.plot(serie, label='Série ' + str(i))   
        i += 1
    plt.legend(loc='upper left')

 
main()