import numpy as np

while True:
    print("=======BEM-VINDO AO MENU DE ESCOLHAS - PROBLEMA LINEAR!========")
    print(" ")
    print("Selecione a opção desejada:")
    print(" ")
    print("0- Sair")
    print("1- Resolução por método do disparo. ")
    print("2- Resolução por método de diferenças finitas.")
    print(" ")
    opção = int(input(
        "Escolha a opção desejada: "))
    print("")
    if opção == 0:
        print("Saindo do programa...")
        break
    elif opção == 1:
        a = 0.0
        b = 1.0
        ya = 0.0
        yb = 2.0

        def solucao_exata(x):
            return np.exp(2)/(np.exp(4)-1)*(np.exp(2*x)-np.exp(-2*x))+x

        def equacao_diferencial_1(x, y, z):
            return z

        def equacao_diferencial_2(x, y, z):
            return 4*(y-x)

        h = 0.1
        N = int((b-a)/h)

        def sistema_1(x, y, z):
            return z

        def sistema_2(x, y, z):
            return 4*(y-x)

        def sistema_complementar_1(x, y, z):
            return z

        def sistema_complementar_2(x, y, z):
            return 4*y

        x = np.linspace(a, b, N+1)
        solucao_1 = np.zeros(N+1)
        derivada_1 = np.zeros(N+1)
        solucao_2 = np.zeros(N+1)
        derivada_2 = np.zeros(N+1)
        solucao_aproximada = np.zeros(N+1)
        derivada_aproximada = np.zeros(N+1)

        solucao_1[0] = ya
        derivada_1[0] = 0.0

        solucao_2[0] = 0.0
        derivada_2[0] = 1.0

        # Método de Runge-Kutta
        for i in range(N):
            # Solução
            k1 = sistema_1(x[i], solucao_1[i], derivada_1[i])
            l1 = sistema_2(x[i], solucao_1[i], derivada_1[i])
            k2 = sistema_1(x[i]+0.5*h, solucao_1[i]+0.5 *
                           h*k1, derivada_1[i]+0.5*h*l1)
            l2 = sistema_2(x[i]+0.5*h, solucao_1[i]+0.5 *
                           h*k1, derivada_1[i]+0.5*h*l1)
            k3 = sistema_1(x[i]+0.5*h, solucao_1[i]+0.5 *
                           h*k2, derivada_1[i]+0.5*h*l2)
            l3 = sistema_2(x[i]+0.5*h, solucao_1[i]+0.5 *
                           h*k2, derivada_1[i]+0.5*h*l2)
            k4 = sistema_1(x[i]+h, solucao_1[i]+h*k3, derivada_1[i]+h*l3)
            l4 = sistema_2(x[i]+h, solucao_1[i]+h*k3, derivada_1[i]+h*l3)

            solucao_1[i+1] = solucao_1[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
            derivada_1[i+1] = derivada_1[i] + (h/6)*(l1 + 2*l2 + 2*l3 + l4)

            k1 = sistema_complementar_1(x[i], solucao_2[i], derivada_2[i])
            l1 = sistema_complementar_2(x[i], solucao_2[i], derivada_2[i])
            k2 = sistema_complementar_1(
                x[i]+0.5*h, solucao_2[i]+0.5*h*k1, derivada_2[i]+0.5*h*l1)
            l2 = sistema_complementar_2(
                x[i]+0.5*h, solucao_2[i]+0.5*h*k1, derivada_2[i]+0.5*h*l1)
            k3 = sistema_complementar_1(
                x[i]+0.5*h, solucao_2[i]+0.5*h*k2, derivada_2[i]+0.5*h*l2)
            l3 = sistema_complementar_2(
                x[i]+0.5*h, solucao_2[i]+0.5*h*k2, derivada_2[i]+0.5*h*l2)
            k4 = sistema_complementar_1(
                x[i]+h, solucao_2[i]+h*k3, derivada_2[i]+h*l3)
            l4 = sistema_complementar_2(
                x[i]+h, solucao_2[i]+h*k3, derivada_2[i]+h*l3)

            solucao_2[i+1] = solucao_2[i] + h/6*(k1+2*(k2+k3)+k4)
            derivada_2[i+1] = derivada_2[i] + h/6*(l1+2*(l2+l3)+l4)

        solucao_aproximada[0] = ya
        derivada_aproximada[0] = (yb-solucao_1[-1])/solucao_2[-1]

        for i in range(1, N+1):
            solucao_aproximada[i] = solucao_1[i] + \
                derivada_aproximada[0]*solucao_2[i]
            derivada_aproximada[i] = derivada_1[i] + \
                derivada_aproximada[0]*derivada_2[i]

        # Erro relativo
        e_medio = np.mean([abs(solucao_aproximada[i]-solucao_exata(x[i])) /
                           abs(solucao_exata(x[i])) for i in range(1, N)])
        e_max = np.max([abs(solucao_aproximada[i]-solucao_exata(x[i])) /
                        abs(solucao_exata(x[i])) for i in range(1, N)])

        print(f'Erro médio:  {e_medio:.3e}')
        print(f'Erro máximo: {e_max:.3e}')
        print(" ")
        input("Pressione ENTER para continuar")

    elif opção == 2:
        # Tamanho do passo
        step_size = 0.1

        # Número de subintervalos
        subintervals = int((b-a)/step_size)-1

        # Coeficiente de y'
        def p_coeff(x):
            return 0

        # Coeficiente de y
        def q_coeff(x):
            return 4

        # Termo não homogêneo
        def r_coeff(x):
            return 4*x

        x_vals = np.linspace(a, b, subintervals+2)
        w_vals = np.zeros(subintervals+2)
        A_coeffs = np.zeros(subintervals+1)
        B_coeffs = np.zeros(subintervals+1)
        C_coeffs = np.zeros(subintervals+1)
        D_coeffs = np.zeros(subintervals+1)

        # Sistema trigiagonal
        A_coeffs[1] = 2 + step_size**2 * q_coeff(x_vals[1])
        B_coeffs[1] = -1 + step_size/2 * p_coeff(x_vals[1])
        D_coeffs[1] = -step_size**2 * \
            r_coeff(x_vals[1]) + (1 + step_size/2 * p_coeff(x_vals[1])) * ya

        for i in range(2, subintervals):
            A_coeffs[i] = 2 + step_size**2 * q_coeff(x_vals[i])
            B_coeffs[i] = -1 + step_size/2 * p_coeff(x_vals[i])
            C_coeffs[i] = -1 - step_size/2 * p_coeff(x_vals[i])
            D_coeffs[i] = -step_size**2 * r_coeff(x_vals[i])

        A_coeffs[subintervals] = 2 + step_size**2 * \
            q_coeff(x_vals[subintervals])
        C_coeffs[subintervals] = -1 - step_size / \
            2 * p_coeff(x_vals[subintervals])
        D_coeffs[subintervals] = -step_size**2 * r_coeff(x_vals[subintervals]) + (
            1 - step_size/2 * p_coeff(x_vals[subintervals])) * yb

        # Matriz tridiagonal
        L_coeffs = np.zeros(subintervals+1)
        U_coeffs = np.zeros(subintervals+1)
        Z_coeffs = np.zeros(subintervals+1)

        L_coeffs[1] = A_coeffs[1]
        U_coeffs[1] = B_coeffs[1]/A_coeffs[1]
        Z_coeffs[1] = D_coeffs[1]/L_coeffs[1]

        for i in range(2, subintervals):
            L_coeffs[i] = A_coeffs[i] - C_coeffs[i]*U_coeffs[i-1]
            U_coeffs[i] = B_coeffs[i]/L_coeffs[i]
            Z_coeffs[i] = (D_coeffs[i] - C_coeffs[i]*Z_coeffs[i-1])/L_coeffs[i]

        L_coeffs[subintervals] = A_coeffs[subintervals] - \
            C_coeffs[subintervals]*U_coeffs[subintervals-1]
        Z_coeffs[subintervals] = (D_coeffs[subintervals] - C_coeffs[subintervals]
                                  * Z_coeffs[subintervals-1])/L_coeffs[subintervals]

        # Solução do sistema linear
        w_vals[0] = ya
        w_vals[-1] = yb
        w_vals[-2] = Z_coeffs[subintervals]
        for i in range(subintervals-1, 0, -1):
            w_vals[i] = Z_coeffs[i] - U_coeffs[i]*w_vals[i+1]

        # Erro relativo
        e_medio = np.mean([abs(w_vals[i]-solucao_exata(x[i])) /
                          abs(solucao_exata(x[i])) for i in range(1, subintervals+1)])
        e_max = np.max([abs(w_vals[i]-solucao_exata(x[i])) /
                       abs(solucao_exata(x[i])) for i in range(1, subintervals+1)])

        print(f'Erro médio:  {e_medio:.3e}')
        print(f'Erro máximo: {e_max:.3e}')
        print("")
        input("Pressione ENTER para continuar")

    else:
        print("Opção inválida, escolha novamente.")
