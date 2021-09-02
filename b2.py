per_cent = {'Home Credit': 7.5, 'Сбербанк': 6.5,
            'Росбанк': 7.2, 'Совкомбанк': 7.05, 'Газпромбанк': 6.0}
deposit = []
money = int(input("Введите сумму: "))
for percent in per_cent.values():
    bet = (money * percent * 365) / 100
    bet = round(bet / 365)
    deposit.append(bet)
print(deposit)
maxValue = max(deposit)
print("Максимальная сумма, которую вы можете заработать:", maxValue)
