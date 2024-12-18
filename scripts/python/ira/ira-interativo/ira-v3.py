def calcular_ira():
    print("Bem-vindo ao cálculo do IRA da UnB.")
    disciplinas = []  # Lista para armazenar todas as disciplinas com seus dados
    aparicoes_disciplina = {}  # Dicionário para contar as aparições de cada disciplina

    for semestre in range(1, 21):  # Loop para cada semestre (1 a 20)
        print(f"\n--- Semestre {semestre} ---")
        while True:
            print("Informe os dados da disciplina:")
            codigo = input("Código da disciplina: ")
            
            while True:
                try:
                    mencao = input("Menção obtida (SS, MS, MM, MI, II, SR): ").strip().upper()
                    valores_mencao = {"SS": 5, "MS": 4, "MM": 3, "MI": 2, "II": 1, "SR": 0}
                    E_i = valores_mencao[mencao]
                    break
                except KeyError:
                    print("Menção inválida. Insira SS, MS, MM, MI, II ou SR.")
            
            while True:
                try:
                    creditos = int(input("Número de créditos da disciplina: "))
                    if creditos > 0:
                        break
                    else:
                        print("O número de créditos deve ser positivo.")
                except ValueError:
                    print("Entrada inválida. Insira um número inteiro.")
            
            # Verifica o semestre da disciplina
            while True:
                semestre_disciplina = int(input(f"Em qual semestre a disciplina {codigo} foi cursada (1-20)? "))
                if 1 <= semestre_disciplina <= 20:
                    break
                else:
                    print("Semestre inválido. Insira um semestre entre 1 e 20.")

            # Armazena a disciplina com o semestre correto
            disciplinas.append({"codigo": codigo, "mencao": E_i, "creditos": creditos, "semestre": semestre_disciplina})

            # Atualiza a contagem de aparições da disciplina
            if codigo in aparicoes_disciplina:
                aparicoes_disciplina[codigo] += 1
            else:
                aparicoes_disciplina[codigo] = 1

            # Contabiliza apenas até 6 aparições para o cálculo do IRA
            if aparicoes_disciplina[codigo] > 6:
                print(f"A disciplina {codigo} já foi registrada 6 vezes, mas será considerada apenas até 6 aparições para o cálculo do IRA.")

            # Pergunta se quer adicionar mais disciplinas ao mesmo semestre
            mais = input("Deseja adicionar outra disciplina neste semestre? (s/n): ").strip().lower()
            if mais != 's':
                break

        # Pergunta se deseja pular para o próximo semestre
        avancar = input("Deseja passar para o próximo semestre? (s/n): ").strip().lower()
        if avancar != 's':
            break

    # Cálculo do IRA considerando as limitações de até 6 aparições
    soma_ponderada = sum(d["mencao"] * d["creditos"] * d["semestre"] for d in disciplinas[:6])  # Considera no máximo 6 registros por disciplina
    soma_creditos = sum(d["creditos"] * d["semestre"] for d in disciplinas[:6])  # Considera no máximo 6 registros por disciplina
    ira = soma_ponderada / soma_creditos if soma_creditos > 0 else 0

    print(f"\n--- Resultado ---")
    print(f"Seu IRA é: {ira:.2f}")
    return ira


# Executa o cálculo do IRA
calcular_ira()
