import requests
import json
url = "http://177.101.203.139/edecio/filmes.json"


def titulo(msg, traco="-", tam=50):
    print()
    print(msg)
    print(traco*tam)

def listar_serv():
    titulo(msg="Lista dos dados do servidor", tam=98)

    response = requests.get(url)

    dados = json.loads(response.text)

    print("Cód. Título............................: Gênero.....: Distribuição......: Ano.....: Público no Ano.:")

    for i, dado in enumerate(dados):
        print(
            f"{dado['id']:4d} {dado['titulo'][0:35]:35s} {dado['genero']:12s} {dado['empresa_distribuidora'][0:20]:20s} {dado['ano_exibicao']} {dado['publico_ano_exibicao']:15d} ")
        if i == 200:
            break

def filtrar_Produtor():
    titulo(msg="Filtrar por País Produtor da Obra", tam=98)

    pais = input("Informe a Pais: ")

    response = requests.get(url)
    dados = json.loads(response.text)

    print("Cód. Título............................: Gênero.....: Distribuição......: Ano.....: Público no Ano.:")

    contador = 0

    for dado in dados:
        if dado["pais_produtor_obra"] == pais:
            print(
                f"{dado['id']:4d} {dado['titulo'][0:35]:35s} {dado['genero']:12s} {dado['empresa_distribuidora'][0:20]:20s} {dado['ano_exibicao']} {dado['publico_ano_exibicao']:15d} ")
            contador += 1

    if contador == 0:
        print("* Obs.: Não Foram Encontrados Resultados Para Sua Pesquisa!!!")

def salvar():
    titulo("Salvar Dados na Máquina Local")

    print("Aguarde...")

    response = requests.get(url)

    data = json.loads(response.text)

    dados = []
    contador = 0
    for i, dado in enumerate(data):
        if dado["publico_ano_exibicao"] >= 100000:
            novo = {"id": dado['id'], "titulo": dado['titulo'][0:35], "genero": dado['genero'], "empresa_distribuidora": dado['empresa_distribuidora'],
                    "ano_exibicao": dado['ano_exibicao'], "publico_ano_exibicao": dado['publico_ano_exibicao']}
            contador += 1
            print(f"Salvando: {dado['titulo']}")
            dados.append(novo)
            if i == 200:
                break

    with open("dados.json", "w") as arq:
        json.dump(dados, arq, indent=4)

def listar_local():
    titulo(msg="Listagem de dados locais", tam=98)

    with open("dados.json", "r") as arq:
        dados = json.load(arq)

    print("Cód. Título............................: Gênero.....: Distribuição......: Ano.....: Público no Ano.:")

    for dado in dados:
        print(
            f"{dado['id']:4d} {dado['titulo'][0:35]:35s} {dado['genero']:12s} {dado['empresa_distribuidora'][0:20]:20s} {dado['ano_exibicao']} {dado['publico_ano_exibicao']:15d}")

def salvarTudo():

    response = requests.get(url)
    data = json.loads(response.text)
    dados = []

    for i, dado in enumerate(data):
        novo = {"id": dado['id'], "titulo": dado['titulo'][0:35], "genero": dado['genero'], "empresa_distribuidora": dado['empresa_distribuidora'],
                "ano_exibicao": dado['ano_exibicao'], "publico_ano_exibicao": dado['publico_ano_exibicao']}
        dados.append(novo)
        if i == 200:
            break

    with open("dadosGerais.json", "w") as arq:
        json.dump(dados, arq, indent=4)

def estatistica():
    titulo("Estatística do Cadastro")

    with open("dadosGerais.json", "r") as arq:
        dados = json.load(arq)

    num = len(dados)
    soma = 0
    zerados = 0

    ano2018 = []
    ano2019 = []
    contador = 0
    for i, dado in enumerate(dados):
        if dado["ano_exibicao"] == 2018:
            ano18 = {"id": dado['id'], "ano_exibicao": dado['ano_exibicao']}
            contador += 1
            ano2018.append(ano18)
            if i == 200:
                break
        if dado["ano_exibicao"] == 2019:
            ano19 = {"id": dado['id'], "ano_exibicao": dado['ano_exibicao']}
            contador += 1
            ano2019.append(ano19)
            if i == 200:
                break

    for filmes in dados:
        soma += filmes['publico_ano_exibicao']
        if filmes['publico_ano_exibicao'] == 0:
            zerados += 1

    num = len(dados)
    media = soma / num

    print(f"Nº de Filmes Cadastrados..: {num}")
    print(f"Nº de filmes exibidos em 2018..: {len(ano2018)}")
    print(f"Nº de filmes exibidos em 2019..: {len(ano2019)}")
    print(f"Público médio dos filmes....: {media}")

def agrupar():
    titulo("Nº de Filmes por Genero")

    with open("dadosGerais.json", "r") as arq:
        dados = json.load(arq)

    genero = {}

    for filmes in dados:
        if filmes['genero'] in genero:
            genero[filmes['genero']] += 1
        else:
            genero[filmes['genero']] = 1

    for data in genero.items():
        print(f"{data[0]}: {data[1]}")

def listaSimples():
    titulo(msg="Lista de Filmes Simplificada", tam=98)

    response = requests.get(url)

    dados = json.loads(response.text)

    print("Cód. Título............................: Pais......: ")

    for i, dado in enumerate(dados):
        print(
            f"{dado['id']:4d} {dado['titulo'][0:35]:35s} {dado['pais_produtor_obra'].split()[0]}")
        if i == 200:
            break

def salvaBr():
    titulo("Salvar Dados na Máquina Local")

    print("Aguarde...")

    response = requests.get(url)

    data = json.loads(response.text)

    dados = []
    contador = 0
    for i, dado in enumerate(data):
        if dado["nacionalidade"] == "Brasileira":
            novo = {"id": dado['id'], "titulo": dado['titulo'][0:35], "genero": dado['genero'], "empresa_distribuidora": dado['empresa_distribuidora'],
                    "ano_exibicao": dado['ano_exibicao'], "publico_ano_exibicao": dado['publico_ano_exibicao']}
            contador += 1
            dados.append(novo)
            if i == 200:
                break

    with open("filmes_brasileiros.json", "w") as arq:
        print(f"Salvando {len(dado)} Filmes Brasileiros!")
        json.dump(dados, arq, indent=4)

def listaBr():
    titulo(msg="Listagem de Filmes Brasileiros", tam=98)

    with open("filmes_brasileiros.json", "r") as arq:
        dados = json.load(arq)

    print("Cód. Título............................: Gênero.....: Distribuição......: Ano.....: Público no Ano.:")

    for dado in dados:
        print(
            f"{dado['id']:4d} {dado['titulo'][0:35]:35s} {dado['genero']:12s} {dado['empresa_distribuidora'][0:20]:20s} {dado['ano_exibicao']} {dado['publico_ano_exibicao']:15d}")

salvarTudo()

salvaBr()

while True:
    titulo("Manipulação de Dados", "=")
    print("1. Listar dados do servidor")
    print("2. Filtrar por País Produtor da Obra")
    print("3. Salvar dados (+ de 100K views)")
    print("4. Listar dados locais")
    print("5. Estatisticas")
    print("6. Agrupar por Genero")
    print("7. Lista Simples")
    print("8. Listar Filmes Brasileiros")
    print("0. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_serv()
    elif opcao == 2:
        filtrar_Produtor()
    elif opcao == 3:
        salvar()
    elif opcao == 4:
        listar_local()
    elif opcao == 5:
        estatistica()
    elif opcao == 6:
        agrupar()
    elif opcao == 7:
        listaSimples()
    elif opcao == 8:
        listaBr()
    else:
        break
