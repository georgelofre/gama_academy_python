arquivo = int(input('Qual o tamanho do arquivo em MB? '))
vel = int(input('Qual a velocidade em Mbps(megabits por segundo)? '))
vel_MB = vel / 8
tempo = arquivo / vel_MB
print(f'O tempo para transferir o arquivo de {arquivo}MB na velocidade de {vel}Mbps é de {tempo} segundos.')