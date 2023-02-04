import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as ss

# Leitura do arquivo CSV
data = pd.read_csv(r'CovidNumerico.csv')

print(data.columns[1])


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
    opcao = input(
        "Digite 1 para suavizar a curva de casos acumulados ou digite 0 para sair: ")
    if opcao == "0":
        break
    elif opcao in ["1"]:
        passadas = int(input("Quantas vezes voce deseja passar o filtro nos dados? "))
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
        axs[1].plot(filtrado[colunas[indice]], label="Dados suavizados")
        axs[1].legend()
        plt.show()
