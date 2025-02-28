def gerarDados(t,x_robo, y_robo,velocidade_x,velocidade_y,distancia,x_bola,y_bola,aceleracao_x, aceleracao_y): 
    
    #Arquivos contendo os dados referentes as posição do robo e bola(x_y_robo.txt):
    posicao_robo_bola = open("Dados_Grafico/Gerar_Grafico/x_y_robo_bola.txt", "a") # Abre o arquivo
    posicao_robo_bola.write("%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n" %(t,x_robo,y_robo,x_bola,y_bola))#Inserção de dados no arquivo
    posicao_robo_bola.close()#Fecha e salva as informações no arquivo


    #Arquivo contendo os dados referentes a velocidade do robo no eixo x e y (vx_vy_robo.txt):
    vx_vy_robo = open("Dados_Grafico/Gerar_Grafico/velocidade_robo.txt", "a") #Abre o arquivo
    vx_vy_robo.write("%.2f\t%.2f\t%.2f\n" %(t,velocidade_x,velocidade_y))#Inserção de dados no arquivo
    vx_vy_robo.close()#Fecha e salva as informações no arquivo


    #Arquivo contendo os dados referentes a distância entre o robo e a bola (distancia_robo_bola.txt):
    distancia_robo_bola = open("Dados_Grafico/Gerar_Grafico/distancia_robo_bola.txt", "a") # Abre o arquivo
    distancia_robo_bola.write("%.2f\t%.2f\n" %(t,distancia))#Inserção de dados no arquivo
    distancia_robo_bola.close()#Fecha e salva as informações no arquivo

    #Arquivo contendo os dados referentes a aceleração do robo no eixo x e y (cx_cy_aceleracao_robo.txt):
    aceleracao_robo = open("Dados_Grafico/Gerar_Grafico/acel_robo.txt", "a") # Abre o arquivo
    aceleracao_robo.write("%.2f\t%.2f\t%.2f\n" %(t,aceleracao_x,aceleracao_y))#Inserção de dados no arquivo
    aceleracao_robo.close()#Fecha e salva as informações no arquivo    

    