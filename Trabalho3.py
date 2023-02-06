import os
import time

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

while True:
    def main():
        print("=======BEM-VINDO AO MENU DE EXEMPLOS!========")
        print(" ")
        print("Selecione a opção desejada:")
        print(" ")
        print("0- Sair")
        print("1- Exemplo 1")
        print("2- Exemplo 2")
        print("3- Exemplo 3")
        print(" ")
        opcao = int(input(
            "Escolha um numero para definir o exemplo de gráfico de infecção por Covid-19 que você deseja visualizar: "))

        if opcao == 1:
            # Parâmetros iniciais
            beta = 0.2  # taxa de transmissão
            gamma = 0.1  # taxa de recuperação
            delta = 1/7  # taxa de incubação
            sigma = 0.01  # taxa de decadência da proteção vacinal
            N = 212_000_000  # população total do Brasil
            I0 = 1000  # número de casos iniciais

            # Equações diferenciais

            def seir(y, t, beta, gamma, delta, sigma):
                S, E, I, R = y
                dSdt = -beta * S * I / N
                dEdt = beta * S * I / N - delta * E
                dIdt = delta * E - gamma * I
                dRdt = gamma * I * (1 - sigma)
                return [dSdt, dEdt, dIdt, dRdt]

            # Solução das equações diferenciais
            t = np.linspace(0, 200, 1000)
            y0 = [N-I0, 0, I0, 0]
            sol = odeint(seir, y0, t, args=(beta, gamma, delta, sigma))
            S, E, I, R = sol.T

            # Plotagem dos resultados
            plt.plot(t, I, label='Infectados')
            plt.plot(t, R, label='Recuperados')
            plt.legend()
            plt.xlabel('Tempo (dias)')
            plt.ylabel('Número de pessoas')
            plt.title('Modelo SEIR')
            plt.show()
            os.system("cls")

        elif opcao == 2:
            # Parâmetros iniciais
            beta = 0.3  # taxa de transmissão
            gamma = 0.05  # taxa de recuperação
            delta = 1/7  # taxa de incubação
            sigma = 0.01  # taxa de decadência da proteção vacinal
            N = 212_000_000  # população total do Brasil
            I0 = 1000  # número de casos iniciais

            # Equações diferenciais

            def seir(y, t, beta, gamma, delta, sigma):
                S, E, I, R = y
                dSdt = -beta * S * I / N
                dEdt = beta * S * I / N - delta * E
                dIdt = delta * E - gamma * I
                dRdt = gamma * I * (1 - sigma)
                return [dSdt, dEdt, dIdt, dRdt]

            # Solução das equações diferenciais
            t = np.linspace(0, 200, 1000)
            y0 = [N-I0, 0, I0, 0]
            sol = odeint(seir, y0, t, args=(beta, gamma, delta, sigma))
            S, E, I, R = sol.T

            # Plotagem dos resultados
            plt.plot(t, I, label='Infectados')
            plt.plot(t, R, label='Recuperados')
            plt.legend()
            plt.xlabel('Tempo (dias)')
            plt.ylabel('Número de pessoas')
            plt.title('Modelo SEIR')
            plt.show()
            os.system("cls")

        elif opcao == 3:
            # Parâmetros iniciais
            beta = 0.2  # taxa de transmissão
            gamma = 0.1  # taxa de recuperação
            delta = 1/7  # taxa de incubação
            sigma = 0.01  # taxa de decadência da proteção vacinal
            N = 212_000_000  # população total do Brasil
            I0 = 1000  # número de casos iniciais

            # Equações diferenciais

            def seir(y, t, beta, gamma, delta, sigma):
                S, E, I, R = y
                dSdt = -beta * S * I / N
                dEdt = beta * S * I / N - delta * E
                dIdt = delta * E - gamma * I
                dRdt = gamma * I * (1 - sigma)
                return [dSdt, dEdt, dIdt, dRdt]

            # Solução das equações diferenciais
            t = np.linspace(0, 24, 1000)
            y0 = [N-I0, 0, I0, 0]
            sol = odeint(seir, y0, t, args=(beta, gamma, delta, sigma))
            S, E, I, R = sol.T

            # Plotagem dos resultados
            plt.plot(t, I, label='Infectados')
            plt.plot(t, R, label='Recuperados')
            plt.legend()
            plt.xlabel('Tempo (meses)')
            plt.ylabel('Número de pessoas')
            plt.title('Modelo SEIR')
            plt.show()
            os.system("cls")

        elif opcao == 0:
            return

        else:
            return

    if __name__ == "__main__":
        main()
