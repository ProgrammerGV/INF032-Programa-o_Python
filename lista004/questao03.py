filmes = {}

filmes["Matrix"] = {"vilão": "Agente Smith", "ano": 1999}
filmes["Vingadores: Guerra Infinita"] = {"vilão": "Thanos", "ano": 2018}
filmes["O Rei Leão"] = {"vilão": "Scar", "ano": 1994}
filmes["Batman: O Cavaleiro das Trevas"] = {"vilão": "Coringa", "ano": 2008}
filmes["Star Wars: O Império Contra-Ataca"] = {"vilão": "Darth Vader", "ano": 1980}

for filme, info in filmes.items():
    print(f"Filme: {filme}")
    print(f"Vilão: {info['vilão']}")
    print(f"Ano: {info['ano']}")
    print("-" * 30)