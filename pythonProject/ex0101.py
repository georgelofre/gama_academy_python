import datetime
def voto(x):
    atual = datetime.date.today().year
    idade = atual - x
    if idade < 16:
        return " Voto negado"
    elif 16 <= idade < 18 or idade > 65:
        return "Voto opcional"
    else: 
        return "Voto obrigatório"

ano = int(input('Qual ano você nasceu? '))
print(voto(ano))

