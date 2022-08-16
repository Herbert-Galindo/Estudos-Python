#forma 1
dicionario1 = dict(chave1= "valor da chave")
dicionario1["nova_chave"] = "valor da nova chave"

#forma 2

d1 = {
    "str" : "valor",
    123: "Outro valor",
    (1,2,3,4) : "Tupla"
}
d1["naoexiste"] = "agoraexiste"
if 'naoexiste' in d1:
    print(d1["naoexiste"])
 