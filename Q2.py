import numpy as np

while True:
    print("=======BEM-VINDO AO MENU DE ESCOLHAS - PROBLEMA NÃO LINEAR!========")
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
        # Definição das condições de contorno
        a = 1.0
        b = 2.0
        ya = 1/2
        yb = 1/3

        def y_exata(x):
            return (x+1)**-1

        # Tamanho do passo
        h = 0.1

        # Número de pontos
        N = int((b-a)/h)

        # Funções para a equação diferencial

        def f_primeira(x, y, y_primeira):
            return y_primeira

        def f_segunda(x, y, y_primeira):
            return y**3 - y*y_primeira

        def g_primeira(x, y, y_primeira):
            return 3*y**2 - y_primeira

        def g_segunda(x, y, y_primeira):
            return -y

        # Número máximo de iterações para o método de Newton
        max_iteracoes = 10
        iteracao = 0

        # Chute inicial para a derivada da solução exata em x=a
        TK = (yb-ya)/(b-a)

        # Tolerância para o método de Newton
        tolerancia = 1e-12

        # Iteração usando o método de Newton
        while iteracao < max_iteracoes:
            iteracao += 1

            x = np.linspace(a, b, N+1)
            w1 = np.zeros(N+1)  # y
            w2 = np.zeros(N+1)  # y'
            u1 = np.zeros(N+1)
            u2 = np.zeros(N+1)

            # Condições iniciais para w1 (y)
            w1[0] = ya
            w2[0] = TK

            # Condições iniciais para u1 (derivada de y')
            u1[0] = 0.0
            u2[0] = 1.0

            # Método de Runge-Kutta de quarta ordem
            for i in range(N):
                # Solução de w1 (y)
                k1 = f_primeira(x[i], w1[i], w2[i])
                l1 = f_segunda(x[i], w1[i], w2[i])
                k2 = f_primeira(x[i]+0.5*h, w1[i]+0.5*h*k1, w2[i]+0.5*h*l1)
                l2 = f_segunda(x[i]+0.5*h, w1[i]+0.5*h*k1, w2[i]+0.5*h*l1)
                k3 = f_primeira(x[i]+0.5*h, w1[i]+0.5*h*k2, w2[i]+0.5*h*l2)
                l3 = f_segunda(x[i]+0.5*h, w1[i]+0.5*h*k2, w2[i]+0.5*h*l2)
                k4 = f_primeira(x[i]+h, w1[i]+h*k3, w2[i]+h*l3)
                l4 = f_segunda(x[i]+h, w1[i]+h*k3, w2[i]+h*l3)

                w1[i+1] = w1[i] + h/6*(k1+2*(k2+k3)+k4)
                w2[i+1] = w2[i] + h/6*(l1+2*(l2+l3)+l4)

                # Determinar dy/dx(x[i]) para usar no método de Newton

                k1 = h*u2[i]
                l1 = h*(g_primeira(x[i], w1[i], w2[i])*u1[i] +
                        g_segunda(x[i], w1[i], w2[i])*u2[i])

                k2 = h*(u2[i] + 0.5*l1)
                l2 = h*(g_primeira(x[i]+0.5*h, w1[i], w2[i])*(u1[i]+0.5*k1) +
                        g_segunda(x[i]+0.5*h, w1[i], w2[i])*(u2[i]+0.5*l1))

                k3 = h*(u2[i] + 0.5*l2)
                l3 = h*(g_primeira(x[i]+0.5*h, w1[i], w2[i])*(u1[i]+0.5*k2) +
                        g_segunda(x[i]+0.5*h, w1[i], w2[i])*(u2[i]+0.5*l2))

                k4 = h*(u2[i] + l3)
                l4 = h*(g_primeira(x[i]+h, w1[i], w2[i])*(u1[i]+k3) +
                        g_segunda(x[i]+h, w1[i], w2[i])*(u2[i]+l3))

                u1[i+1] = u1[i] + 1/6*(k1+2*(k2+k3)+k4)
                u2[i+1] = u2[i] + 1/6*(l1+2*(l2+l3)+l4)

            # Para a iteração se atingir o critério de parada
            if abs(w1[-1] - yb) < tolerancia:
                break

            # Aplicar o método de Newton
            TK = TK - (w1[-1] - yb)/u1[-1]

        # Erro relativo médio
        e_medio = np.mean([abs(w1[i]-y_exata(x[i]))/abs(y_exata(x[i]))
                           for i in range(1, N+1)])
        e_max = np.max([abs(w1[i]-y_exata(x[i]))/abs(y_exata(x[i]))
                        for i in range(1, N+1)])

        print(f'Erro relativo médio:  {e_medio:.3e}')
        print(f'Erro relativo máximo: {e_max:.3e}')
        print(" ")
        input("Pressione ENTER para continuar")

    elif opção == 2:
        a = 1.0
        b = 2.0
        ya = 1/2
        yb = 1/3

        def y_exata(x):
            return (x+1)**-1

        h = 0.1

        N = int((b-a)/h)-1

        def f(x, y, z):
            return y**3 - y*z

        def derivada_dfdy(x, y, z):
            return 3*y**2 - z

        def dfdz(x, y, z):
            return -y

        M = 10
        k = 0

        tol = 1e-12

        x = np.linspace(a, b, N+2)
        w = np.zeros(N+2)

        w[0] = ya
        w[-1] = yb

        for i in range(1, N+1):
            w[i] = ya + i*((yb-ya)/(b-a))*h

        while k < M:

            k += 1

            A = np.zeros(N+1)
            B = np.zeros(N+1)
            C = np.zeros(N+1)
            D = np.zeros(N+1)

            t = (w[2]-ya)/(2*h)
            A[1] = 2 + h**2*derivada_dfdy(x[1], w[1], t)
            B[1] = -1 + h/2*dfdz(x[1], w[1], t)
            D[1] = -(2*w[1] - w[2] - ya + h**2*f(x[1], w[1], t))

            for i in range(2, N):
                t = (w[i+1]-w[i-1])/(2*h)
                A[i] = 2 + h**2*derivada_dfdy(x[i], w[i], t)
                B[i] = -1 + h/2*dfdz(x[i], w[i], t)
                C[i] = -1 - h/2*dfdz(x[i], w[i], t)
                D[i] = -(2*w[i] - w[i+1] - w[i-1] + h**2*f(x[i], w[i], t))

            t = (yb-w[N-1])/(2*h)
            A[N] = 2 + h**2*derivada_dfdy(x[N], w[N], t)
            C[N] = -1 - h/2*dfdz(x[N], w[N], t)
            D[N] = -(2*w[N] - w[N-1] - yb + h**2*f(x[N], w[N], t))

            L = np.zeros(N+1)
            U = np.zeros(N+1)
            Z = np.zeros(N+1)

            L[1] = A[1]
            U[1] = B[1]/A[1]
            Z[1] = D[1]/L[1]

            for i in range(2, N):
                L[i] = A[i] - C[i]*U[i-1]
                U[i] = B[i]/L[i]
                Z[i] = (D[i] - C[i]*Z[i-1])/L[i]

            L[N] = A[N] - C[N]*U[N-1]
            Z[N] = (D[N] - C[N]*Z[N-1])/L[N]

            v = np.zeros(N+1)
            v[N] = Z[N]
            w[N] = w[N] + v[N]
            for i in range(N-1, 0, -1):
                v[i] = Z[i] - U[i]*v[i+1]
                w[i] = w[i] + v[i]

            if np.linalg.norm(v[1:]) < tol:
                break

        e_medio = np.mean([abs(w[i]-y_exata(x[i]))/abs(y_exata(x[i]))
                           for i in range(1, N+1)])
        e_max = np.max([abs(w[i]-y_exata(x[i]))/abs(y_exata(x[i]))
                        for i in range(1, N+1)])

        print(f'Erro médio:  {e_medio:.3e}')
        print(f'Erro máximo: {e_max:.3e}')
        print("")
        input("Pressione ENTER para continuar")

    else:
        print("Opção inválida, escolha novamente.")
