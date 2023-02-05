import csv
import os

import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as ss

# Leitura do arquivo CSV e identificando de forma automática qual delimitador do arquivo.
data = pd.read_csv(r'CovidNumerico.csv', engine='python')

dialect = csv.Sniffer().sniff(open('CovidNumerico.csv').read(1024))
delimiter = dialect.delimiter

print("Delimiter identificado:", repr(delimiter))


data = pd.read_csv('CovidNumerico.csv', delimiter=delimiter)


# Checando valores nulos
data.isna().sum()

# Interpolação para excluir valores nulos
data_int = data.interpolate()
# Criando lista com o nome das colunas
colunas = list(data_int.columns)

# Aplicação do filtro de Savitsky-Golay
largura = 3
ordem_polinomio = 1
passadas = 10
# Coluna de dados a ser suavizada

while True:

    print("=======BEM-VINDO AO MENU DE ESCOLHAS!========")
    print(" ")
    print("Selecione a opção desejada:")
    print(" ")
    print("Opção 0 - Sair.")
    print("Opção 1 - CasosNovos.")
    print("Opção 2 - ObitosNovos.")
    print("Opção 3 - Recuperadosnovos.")
    print("Opção 4 - EmAcompanhamentoNovos.")
    print(" ")

    opcao = input(
        "Digite um número que irá definir a coluna que a ser suavizada ou 0 para sair: ")
    if opcao == "0":
        break
    elif opcao in ["1"]:
        passadas = int(
            input("Quantas vezes voce deseja passar o filtro nos dados? "))
        indice = 2
        # Aplicando o filtro
        filtrado = {}

        for i in range(2, len(colunas)):
            filtrado[colunas[i]] = ss.savgol_filter(
                data_int[colunas[i]], largura, ordem_polinomio)
        if passadas > 1:
            for i in range(2, passadas):
                for i in range(2, len(colunas)):
                    filtrado[colunas[i]] = ss.savgol_filter(
                        filtrado[colunas[i]], largura, ordem_polinomio)

        # Plotagem dos dados originais e dos dados suavizados e escolhendo o intervalo de dados a ser filtrado
        fig, axs = plt.subplots(1, 2)
        fig.suptitle('Dados originais vs Dados suavizados')
        axs[0].plot(data_int[colunas[indice]], label="Dados originais")
        axs[0].legend()
        axs[1].plot(filtrado[colunas[indice]],
                    label="Dados suavizados", color='red')
        axs[1].legend()
        plt.show()

        os.system("cls")

    elif opcao in ["2"]:
        passadas = int(
            input("Quantas vezes voce deseja passar o filtro nos dados? "))
        indice = 4
        # Aplicando o filtro
        filtrado = {}

        for i in range(2, len(colunas)):
            filtrado[colunas[i]] = ss.savgol_filter(
                data_int[colunas[i]], largura, ordem_polinomio)
        if passadas > 1:
            for i in range(2, passadas):
                for i in range(2, len(colunas)):
                    filtrado[colunas[i]] = ss.savgol_filter(
                        filtrado[colunas[i]], largura, ordem_polinomio)

        # Plotagem dos dados originais e dos dados suavizados e escolhendo o intervalo de dados a ser filtrado
        fig, axs = plt.subplots(1, 2)
        fig.suptitle('Dados originais vs Dados suavizados')
        axs[0].plot(data_int[colunas[indice]], label="Dados originais")
        axs[0].legend()
        axs[1].plot(filtrado[colunas[indice]],
                    label="Dados suavizados", color='red')
        axs[1].legend()
        plt.show()

        os.system("cls")

    elif opcao in ["3"]:
        passadas = int(
            input("Quantas vezes voce deseja passar o filtro nos dados? "))
        indice = 5
        # Aplicando o filtro
        filtrado = {}

        for i in range(2, len(colunas)):
            filtrado[colunas[i]] = ss.savgol_filter(
                data_int[colunas[i]], largura, ordem_polinomio)
        if passadas > 1:
            for i in range(2, passadas):
                for i in range(2, len(colunas)):
                    filtrado[colunas[i]] = ss.savgol_filter(
                        filtrado[colunas[i]], largura, ordem_polinomio)

        # Plotagem dos dados originais e dos dados suavizados e escolhendo o intervalo de dados a ser filtrado
        fig, axs = plt.subplots(1, 2)
        fig.suptitle('Dados originais vs Dados suavizados')
        axs[0].plot(data_int[colunas[indice]], label="Dados originais")
        axs[0].legend()
        axs[1].plot(filtrado[colunas[indice]],
                    label="Dados suavizados", color='red')
        axs[1].legend()
        plt.show()

        os.system("cls")

    elif opcao in ["4"]:
        passadas = int(
            input("Quantas vezes voce deseja passar o filtro nos dados? "))
        indice = 6
        # Aplicando o filtro
        filtrado = {}

        for i in range(2, len(colunas)):
            filtrado[colunas[i]] = ss.savgol_filter(
                data_int[colunas[i]], largura, ordem_polinomio)
        if passadas > 1:
            for i in range(2, passadas):
                for i in range(2, len(colunas)):
                    filtrado[colunas[i]] = ss.savgol_filter(
                        filtrado[colunas[i]], largura, ordem_polinomio)

        # Plotagem dos dados originais e dos dados suavizados e escolhendo o intervalo de dados a ser filtrado
        fig, axs = plt.subplots(1, 2)
        fig.suptitle('Dados originais vs Dados suavizados')
        axs[0].plot(data_int[colunas[indice]], label="Dados originais")
        axs[0].legend()
        axs[1].plot(filtrado[colunas[indice]],
                    label="Dados suavizados", color='red')
        axs[1].legend()
        plt.show()

        os.system("cls")

    else:
        break
