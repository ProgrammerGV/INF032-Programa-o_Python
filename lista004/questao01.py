pessoas_proximas = {
    "Tiago": "preta",
    "Taina": "branca",
    "Naoseionomedocolega": "azul",
    "Naoseionomedocolega1": "verde",
    "Naoseionomedocolega2": "cinza"
}

print("Dicionário completo:", pessoas_proximas)

for pessoa, cor in pessoas_proximas.items():
    print(f"{pessoa} está usando uma camisa {cor}.")