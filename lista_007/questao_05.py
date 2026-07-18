def somaImposto(taxaImposto, custo):
    """
    Altera o valor do custo para incluir o imposto sobre vendas.
    taxaImposto é a quantia de imposto sobre vendas expressa em porcentagem.
    """
    novo_custo = custo + (custo * (taxaImposto / 100))
    return novo_custo

if __name__ == '__main__':
    try:
        taxa = float(input("Digite a taxa de imposto em porcentagem (ex: 10 para 10%): "))
        custo = float(input("Digite o custo do item: "))
        
        custo_com_imposto = somaImposto(taxa, custo)
        
        print(f"O custo do item com imposto é: R$ {custo_com_imposto:.2f}")
    except ValueError:
        print("Entrada inválida. Digite valores numéricos.")
