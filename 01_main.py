#import datetime as datetime usa a data e a hora atual
#mostrar data e hora
from datetime import datetime
import csv  


#Hora e data atual
hora_atual = datetime.now()
hora_atual =datetime.now().strftime("%d/%m/%y %H:%M")
print(hora_atual)
#inseiri meta primeiro 
meta = float(input("Inserir meta diaria: "))

# Verificar Km/litros : consumo do carro 
km1 = float(input('Digite a km inicial de hoje: '))
km2 = float(input('Digite a km final de hoje: '))
litros = float(input('Digite a quantidade de litros abastecida: '))
consumo = (km2 + km1)/litros
print(f'O consumo foi de: {consumo :.2f} km/l')

#Passo 2 Entrada dos gastos ao longo do dia
gasto_total = float(input('Digite o gasto total do dia: '))
print(f'O gasto total do dia: {gasto_total:.2f}')

#Passo 3 
#Entrada dos valores recebidos no dia
receb1 = float(input('Recebidos de hoje mãe Uber: '))
receb2 = float(input('Recebidos de hoje 99: '))
receb_total = receb1 + receb2

print(f'O recebimento total do dia: {receb_total:.2f}')


#Passo 4 Verificar se houve lucro ou prejuizo
#result2 = receb_total -gasto_total #(passo desnecessario?)
if receb_total > gasto_total:
    print(f"Hoje deu bom! Lucro de {receb_total - gasto_total}")

else:
    print(f"Hoje deu ruim! Prejuizo de {gasto_total - receb_total}")    

#Meta diária
falta = meta - receb_total
print(f'Faltam:{falta} para atingir sua meta Diária')

#ganho por km
ganho_por_km = receb_total/(km2-km1)
print(f'Ganho por km: {ganho_por_km:.2f} reais/km')

#Salvar dados em csv 
with open("dados.csv","a",newline="")as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Data","consumo","gastos","recebimentos",])
    writer.writerow([hora_atual,consumo,gasto_total,receb_total,])





























































#import datetime as date 
#from datetime import date
#hoje = date.today()
#hoje =date.today().strftime("%d/%m/%y")
#print(hoje)
#Problema1
#1. verificar Km/litros : 


