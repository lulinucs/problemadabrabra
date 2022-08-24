Palmeiras = {'Nome': 'Palmeiras', 'Pontos': 49, 'Vitórias': 14, 'Gols': 38, 'Saldo': 23, 'Cartões': 5}
Fluminense = {'Nome': 'Fluminense', 'Pontos': 41, 'Vitórias': 12, 'Gols': 37, 'Saldo': 10, 'Cartões': 4}
Flamengo = {'Nome': 'Flamengo', 'Pontos': 40, 'Vitórias': 12, 'Gols': 38, 'Saldo': 18, 'Cartões': 3}
Corinthians = {'Nome': 'Corinthians', 'Pontos': 39, 'Vitórias': 11, 'Gols': 26, 'Saldo': 4, 'Cartões': 2}
Internacional = {'Nome': 'Internacional', 'Pontos': 39, 'Vitórias': 11, 'Gols': 26, 'Saldo': 4, 'Cartões': 1}

classificacao = [Corinthians, Flamengo, Fluminense, Internacional, Palmeiras]
classificacao = sorted(classificacao, key=lambda k: k['Cartões'])
classificacao = sorted(classificacao, key=lambda k: k['Saldo'], reverse=True)
classificacao = sorted(classificacao, key=lambda k: k['Gols'], reverse=True)
classificacao = sorted(classificacao, key=lambda k: k['Vitórias'], reverse=True)
classificacao = sorted(classificacao, key=lambda k: k['Pontos'], reverse=True)

for time in classificacao:
    print(time)
