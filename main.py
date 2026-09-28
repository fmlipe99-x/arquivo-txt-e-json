import json
from datetime import datetime



with open("dados.txt", "w", encoding="utf-8") as arquivo: # o parametro "w" é para escrever algo no arquivo txt
    arquivo.write("escrevendo um arquivo em python!!!")



with open ("dados.txt", "r") as arquivo:  # o parametro "r" é para ler o que esta escrito no arquivo txt
    texto = arquivo.read()
    print(texto)




with open ("dados.txt", "a", encoding="utf-8") as arquivo: # o parametro "a" é para add coisas no arquivo txt
    arquivo.write("\n")
    arquivo.write("adicionando mais coisas!")



config = {
    "nome": "Sistema Escolar", 
    "tema": "escuro", 
    "volume": 75,
    "atualizado": True
}

with open("config.json", "w", encoding="utf-8") as arquivo:
    json.dump(config, arquivo, indent=4)   # dump = open, dump é para json, enquanto para txt é open


with open("config.json", "r", encoding="utf-8") as arquivo:
    config = json.load(arquivo)


print("config: ", config)
print("tema: ", config["tema"])
print("volume: ", config["volume"])




agora = datetime.now()
print(agora)
