def reps(lista):
    contagens = {}
    for elemento in lista:
        if elemento in contagens:
            contagens[elemento] += 1
        else:
            contagens[elemento] = 1
            
    # Filtra apenas os que têm contagem >= 2
    resultado = [elemento for elemento, count in contagens.items() if count >= 2]
    # Retorna ordenado para ficar parecido com o exemplo
    return sorted(resultado)

if __name__ == '__main__':
    # Teste conforme exemplo do enunciado
    lista_exemplo = [1, 4, 2, 3, 4, 2, 3, 4]
    resultado = reps(lista_exemplo)
    print(f"reps({lista_exemplo}) -> {resultado}")
