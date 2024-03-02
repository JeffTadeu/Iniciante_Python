lista_exemplo = ['Jeff', 'Anna', 'Alguém']

def trocar_valor_da_lista(valor_novo, valor_para_trocar, lista_desejada):
    
    contador = 0

    for elemento in lista_desejada:
        if elemento == valor_para_trocar:
            lista_desejada[contador] = valor_novo
            return lista_desejada
        elif contador < len(lista_desejada) - 1:
            contador += 1
        else:
            print('O valor procurado não possui na lista')
            return lista_desejada
        
    

print(trocar_valor_da_lista('Tadeu', 'Alguém', lista_exemplo))
