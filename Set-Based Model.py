import string

# Função para converter uma descrição em um conjunto de termos, removendo pontuação
def descricao_para_conjunto(descricao):
    # Remover pontuação
    descricao_sem_pontuacao = descricao.translate(str.maketrans('', '', string.punctuation))
    # Converter para conjunto de termos
    termos_conjunto = set(descricao_sem_pontuacao.lower().split())
    # Exibir o Termset gerado com espaços adicionais
    print(f"\nTermset da descrição:\n{termos_conjunto}\n")
    return termos_conjunto

# Função para encontrar bairros que correspondam à consulta
def buscar_bairros(consulta, bairros):
    # Converter a consulta para Termset
    consulta_conjunto = descricao_para_conjunto(consulta)
    print(f"\nTermset da consulta:\n{consulta_conjunto}\n")
    
    resultados = []
    
    for bairro, descricao in bairros.items():
        # Converter a descrição do bairro para Termset
        descricao_conjunto = descricao_para_conjunto(descricao)
        print(f"Comparando com o Termset do bairro '{bairro}':\n{descricao_conjunto}\n")
        
        # Verificar se o Termset da consulta está contido no Termset do bairro
        if consulta_conjunto.issubset(descricao_conjunto):
            print(f"-> O bairro '{bairro}' atende à consulta!\n")
            resultados.append(bairro)
        else:
            print(f"-> O bairro '{bairro}' NÃO atende à consulta.\n")
    
    return resultados

# Lista de descrições de bairros
bairros = {
    "Centro": "O Centro é o coração da cidade, com muitos prédios históricos, comércio variado e restaurantes.",
    "Jardim das Flores": "Um bairro residencial tranquilo, com muitas áreas verdes, parques e boas escolas.",
    "Vila Nova": "Bairro moderno com muitos apartamentos, opções de lazer e bons restaurantes.",
    "Praia Azul": "Bairro litorâneo com belas praias, muitos restaurantes de frutos do mar e áreas de lazer.",
    "Parque das Acácias": "Um bairro arborizado com várias escolas, parques, e uma grande variedade de restaurantes.",
    "Cidade Verde": "Área residencial com muitas escolas, parques e excelentes restaurantes para todos os gostos.",
    "Bela Vista": "Bairro charmoso com escolas de renome, parques bem cuidados, e uma diversidade de restaurantes.",
    "Jardins do Lago": "Região com belos parques, escolas de qualidade, e restaurantes sofisticados para toda a família.",
    "Alto da Colina": "Bairro com vista panorâmica, escolas modernas, grandes parques e uma ampla oferta de restaurantes."
}

# Consulta do usuário
consulta = "parques escolas restaurantes"

# Buscar bairros que correspondem à consulta
resultados = buscar_bairros(consulta, bairros)

# Exibir resultados com um espaço extra
print("\n\nBairros encontrados:", resultados)
