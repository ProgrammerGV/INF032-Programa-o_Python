def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_hoje, mes_hoje, ano_hoje):
    idade = ano_hoje - ano_nasc
    if mes_hoje < mes_nasc or (mes_hoje == mes_nasc and dia_hoje < dia_nasc):
        idade -= 1
    return idade

def gerar_idades(arq_entrada, arq_saida, data_hoje):
    try:
        dia_hoje, mes_hoje, ano_hoje = map(int, data_hoje.split())
        
        with open(arq_entrada, 'r', encoding='utf-8') as f_in, \
             open(arq_saida, 'w', encoding='utf-8') as f_out:
            for linha in f_in:
                partes = linha.strip().split()
                if len(partes) >= 4:
                    ano_nasc = int(partes[-1])
                    mes_nasc = int(partes[-2])
                    dia_nasc = int(partes[-3])
                    nome = " ".join(partes[:-3])
                    
                    idade = calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_hoje, mes_hoje, ano_hoje)
                    f_out.write(f"{nome} - {idade} anos\n")
        return True
    except FileNotFoundError:
        return False
    except ValueError:
        print("Erro de formato na data ou arquivo inválido.")
        return False

if __name__ == '__main__':
    entrada = input("Digite o nome do arquivo de entrada: ")
    saida = input("Digite o nome do arquivo de saída: ")
    data_hoje = input("Digite a data de hoje (DD MM AAAA): ")
    
    if gerar_idades(entrada, saida, data_hoje):
        print("Arquivo de idades gerado com sucesso!")
    else:
        print("Falha ao processar.")
