# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians',
         'Fortaleza', 'Internacional', 'Fluminense', 'América-MG', 'Ceará SC',
         'Athletico-PR', 'Santos', 'Cuiabá', 'Atlético-GO', 'São Paulo',
         'Bahia', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print('-=-' * 20)
print(f"A lista de times da série A do brasileirão: {times}")
print('-=-' * 20)
print(f"Os 5 primeiros colocados da tabela são: {times[:5]}")
print('-=-' * 20)
print(f"Os 4 últimos da tabela são: {times[-4:]}")
print('-=-' * 20)
print(f"Os times em ordem alfabética são: {sorted(times)}")
print('-=-' * 20)
print(f"O Chapecoense está na {times.index('Chapecoense')+1}° posição!")
print('-=-' * 20)