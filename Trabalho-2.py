import os
import time

import numpy as np
from scipy.odr import ODR, Data, Model

while True:
    def main():
        print("=======BEM-VINDO AO MENU DE ESCOLHAS!========")
        print(" ")
        print("Selecione a opção desejada:")
        print(" ")
        print("0- Sair")
        print("1- Algoritmo de mínimos erros quadrados ordinário.")
        print("2- Algoritmo de mínimos erros quadrados recursivo.")
        print("3- Algoritmo de mínimos quadrados total.")
        print(" ")
        opcao = int(input(
            "Escolha um número para definir com qual variação você irá calcular: "))

        if opcao == 1:
            print(" ")
            print("Calculando...")
            time.sleep(2)
            print(" ")
            print("Seu resultado de A, B e C vale:")
            os.system("cls")
            print("Utilizando algoritmo de mínimos erros quadrados ordinário, temos:")
            print(" ")
            # Ruidos
            x = [5.06, 12.14, 12.98, 13.96, 14.14, 14.98, 15.08, 16.06, 17.12, 19.02, 21.82, 24.98, 25.0, 25.14, 26.98, 27.0, 27.92, 28.98, 31.06, 34.2, 34.94, 35.82, 35.98, 36.1, 38.88, 39.02, 40.98, 45.18, 45.2, 47.1, 52.0,
                 53.1, 54.8, 54.92, 56.18, 58.82, 61.2, 65.02, 65.88, 66.88, 67.06, 67.8, 69.8, 69.9, 73.08, 75.8, 76.02, 78.14, 84.04, 85.06, 85.2, 87.94, 90.08, 92.08, 92.12, 92.92, 94.1, 95.84, 96.14, 97.1, 98.9, 99.14, 100.06]
            y = [70.5, 330.13, 374.67, 436.89, 430.32, 496.09, 497.98, 557.94, 625.59, 774.96, 1038.24, 1327.26, 1332.57, 1329.06, 1538.65, 1542.25, 1644.54, 1772.25, 2009.07, 2411.94, 2565.0, 2696.5, 2703.61, 2696.68, 3152.71, 3162.25, 3477.54, 4184.02, 4192.21, 4554.15, 5557.89, 5769.81, 6224.82,
                 6207.27, 6443.52, 7134.42, 7629.69, 8644.38, 8908.39, 9173.88, 9180.9, 9456.6, 10018.2, 10010.19, 10879.53, 11779.29, 11786.49, 12402.55, 14370.58, 14711.31, 14714.46, 15760.2, 16468.3, 17205.36, 17210.13, 17570.62, 17960.13, 18712.45, 18712.18, 19112.88, 19903.96, 19905.04, 20296.14]

            def f(beta, x):  # Função polinômio de segundo grau
                return beta[0] * x**2 + beta[1] * x + beta[2]

            def f(beta, x):
                return beta[0]*x**2 + beta[1]*x + beta[2]

            model = Model(f)  # Modelo de mínimos quadrados

            data = Data(x, y)  # Dados para o ajuste

            # Criar objeto ODR com modelo e dados
            odr = ODR(data, model, beta0=[1, 1, 1])

            result = odr.run()  # Realizar ajuste

            # Imprimir resultados
            print("A:", result.beta[0])
            print("B:", result.beta[1])
            print("C:", result.beta[2])
            print(" ")
            input("Aperte qualquer tecla para continuar...")
            print(" ")
            os.system("cls")

        elif opcao == 2:
            print(" ")
            print("Calculando...")
            time.sleep(2)
            print(" ")
            print("Seu resultado de A, B e C vale:")
            os.system("cls")
            print("Utilizando algoritmo de mínimos erros quadrados recursivo, temos:")
            print(" ")
            # Ruidos
            x = [5.06, 12.14, 12.98, 13.96, 14.14, 14.98, 15.08, 16.06, 17.12, 19.02, 21.82, 24.98, 25.0, 25.14, 26.98, 27.0, 27.92, 28.98, 31.06, 34.2, 34.94, 35.82, 35.98, 36.1, 38.88, 39.02, 40.98, 45.18, 45.2, 47.1, 52.0,
                 53.1, 54.8, 54.92, 56.18, 58.82, 61.2, 65.02, 65.88, 66.88, 67.06, 67.8, 69.8, 69.9, 73.08, 75.8, 76.02, 78.14, 84.04, 85.06, 85.2, 87.94, 90.08, 92.08, 92.12, 92.92, 94.1, 95.84, 96.14, 97.1, 98.9, 99.14, 100.06]
            y = [70.5, 330.13, 374.67, 436.89, 430.32, 496.09, 497.98, 557.94, 625.59, 774.96, 1038.24, 1327.26, 1332.57, 1329.06, 1538.65, 1542.25, 1644.54, 1772.25, 2009.07, 2411.94, 2565.0, 2696.5, 2703.61, 2696.68, 3152.71, 3162.25, 3477.54, 4184.02, 4192.21, 4554.15, 5557.89, 5769.81, 6224.82,
                 6207.27, 6443.52, 7134.42, 7629.69, 8644.38, 8908.39, 9173.88, 9180.9, 9456.6, 10018.2, 10010.19, 10879.53, 11779.29, 11786.49, 12402.55, 14370.58, 14711.31, 14714.46, 15760.2, 16468.3, 17205.36, 17210.13, 17570.62, 17960.13, 18712.45, 18712.18, 19112.88, 19903.96, 19905.04, 20296.14]

            def recursive_least_squares(x, y, a, b, c, alpha, error=0.01):
                n = len(x)
                new_a = a
                new_b = b
                new_c = c
                i = 0
                while i < n:
                    y_pred = a * x[i]**2 + b * x[i] + c
                    error = y[i] - y_pred
                    new_a = a + (2 * alpha * error * x[i]**2)
                    new_b = b + (2 * alpha * error * x[i])
                    new_c = c + (2 * alpha * error)
                    if abs(new_a - a) < error and abs(new_b - b) < error and abs(new_c - c) < error:
                        break
                    a = new_a
                    b = new_b
                    c = new_c
                    i += 1
                return new_a, new_b, new_c

            a, b, c = 0, 0, 0
            alpha = 0.01
            a, b, c = recursive_least_squares(x, y, a, b, c, alpha)
            print("a:", a)
            print("b:", b)
            print("c:", c)
            print(" ")
            input("Aperte qualquer tecla para continuar...")
            print(" ")
            os.system("cls")

        elif opcao == 3:
            print(" ")
            print("Calculando...")
            time.sleep(2)
            print(" ")
            print("Seu resultado de A, B e C vale:")
            os.system("cls")
            print("Utilizando algoritmo de mínimos erros quadrados total, temos:")
            print(" ")
            # Ruidos
            x = [5.06, 12.14, 12.98, 13.96, 14.14, 14.98, 15.08, 16.06, 17.12, 19.02, 21.82, 24.98, 25.0, 25.14, 26.98, 27.0, 27.92, 28.98, 31.06, 34.2, 34.94, 35.82, 35.98, 36.1, 38.88, 39.02, 40.98, 45.18, 45.2, 47.1, 52.0,
                 53.1, 54.8, 54.92, 56.18, 58.82, 61.2, 65.02, 65.88, 66.88, 67.06, 67.8, 69.8, 69.9, 73.08, 75.8, 76.02, 78.14, 84.04, 85.06, 85.2, 87.94, 90.08, 92.08, 92.12, 92.92, 94.1, 95.84, 96.14, 97.1, 98.9, 99.14, 100.06]
            y = [70.5, 330.13, 374.67, 436.89, 430.32, 496.09, 497.98, 557.94, 625.59, 774.96, 1038.24, 1327.26, 1332.57, 1329.06, 1538.65, 1542.25, 1644.54, 1772.25, 2009.07, 2411.94, 2565.0, 2696.5, 2703.61, 2696.68, 3152.71, 3162.25, 3477.54, 4184.02, 4192.21, 4554.15, 5557.89, 5769.81, 6224.82,
                 6207.27, 6443.52, 7134.42, 7629.69, 8644.38, 8908.39, 9173.88, 9180.9, 9456.6, 10018.2, 10010.19, 10879.53, 11779.29, 11786.49, 12402.55, 14370.58, 14711.31, 14714.46, 15760.2, 16468.3, 17205.36, 17210.13, 17570.62, 17960.13, 18712.45, 18712.18, 19112.88, 19903.96, 19905.04, 20296.14]

            z = np.polyfit(x, y, 2)  # Polinômio de 2o grau
            # Valores de A, B e C
            A = z[0]
            B = z[1]
            C = z[2]
            print("A:", A)
            print("B:", B)
            print("C:", C)
            print(" ")
            input("Aperte qualquer tecla para continuar...")
            print(" ")
            os.system("cls")

        elif opcao == 0:
            print(" ")
            return

        else:
            return

    if __name__ == "__main__":
        main()
