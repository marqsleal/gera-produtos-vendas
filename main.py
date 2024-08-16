import csv
import json
import random
from datetime import datetime


def gerar_data_hora_aleatoria():
    ano = 2024
    mes = random.randint(1, 8)
    dia = random.randint(1, 28)
    hora = random.randint(9, 17)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)

    data_hora = datetime(ano, mes, dia, hora, minuto, segundo)
    return data_hora.strftime('%Y-%m-%d %H:%M:%S')


def gerar_produtos(produtos, path):
    with open(path, mode='w', newline='') as file:
        fieldnames = ['id', 'nome', 'quantidade', 'valor', 'ativo', 'categoria']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)
    print(f"Arquivo '{path}' criado com sucesso!")


def gerar_venda(id_venda, produtos):
    venda = {
        'id': id_venda,
        'produtos': [],
        'valor_total': 0.0,
        'data_hora': gerar_data_hora_aleatoria()}
    num_produtos = random.randint(1, 5)
    produtos_selecionados = random.sample(produtos, num_produtos)

    for produto in produtos_selecionados:
        quantidade = random.randint(1, 3)
        valor_produto = produto['valor']
        valor_total_produto = valor_produto * quantidade

        venda['produtos'].append({
            'id': produto['id'],
            'nome': produto['nome'],
            'quantidade': quantidade,
            'valor': valor_produto
        })

        venda['valor_total'] += valor_total_produto

    venda['valor_total'] = round(venda['valor_total'], 2)

    return venda


def gerar_vendas(vendas, path):
    with open(path, mode='w', newline='') as file:
        fieldnames = ['id', 'produtos', 'valor_total', 'data_hora']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for venda in vendas:
            venda['produtos'] = json.dumps(venda['produtos'])
            writer.writerow(venda)

    print(f"Arquivo '{path}' criado com sucesso!")


def main():
    produtos = [
        {'id': 1, 'nome': 'bis xtra chocolate ao leite 45g', 'quantidade': 27, 'valor': 2.99, 'ativo': True,
         'categoria': 'chocolate'},
        {'id': 2, 'nome': 'chocolate kit kat ao leite nestle 41', 'quantidade': 15, 'valor': 2.99, 'ativo': True,
         'categoria': 'chocolate'},
        {'id': 3, 'nome': 'chocolate garoto caribe banana 28g', 'quantidade': 32, 'valor': 3.49, 'ativo': True,
         'categoria': 'chocolate'},
        {'id': 4, 'nome': 'chocolate prestigio nestle 33g', 'quantidade': 25, 'valor': 3.49, 'ativo': True,
         'categoria': 'chocolate'},
        {'id': 5, 'nome': 'kinder bueno chocolate ao leite 2 unidades 43g', 'quantidade': 18, 'valor': 7.99,
         'ativo': True, 'categoria': 'chocolate'},
        {'id': 6, 'nome': 'chocolate amandita 200g', 'quantidade': 12, 'valor': 14.99, 'ativo': True,
         'categoria': 'chocolate'},
        {'id': 7, 'nome': 'smartphone samsung galaxy a15 256gb 8gb de ram', 'quantidade': 2, 'valor': 1169.10,
         'ativo': True, 'categoria': 'celular'},
        {'id': 8, 'nome': 'smartphone motorola moto g04s 4g 128gb 8gb ram', 'quantidade': 4, 'valor': 719.10,
         'ativo': True, 'categoria': 'celular'},
        {'id': 9, 'nome': 'smartphone samsung galaxy a05 128gb 4g wi-fi', 'quantidade': 5, 'valor': 718.20,
         'ativo': True, 'categoria': 'celular'},
        {'id': 10, 'nome': 'smartphone motorola moto g54 5g 256gb 8gb ram', 'quantidade': 4, 'valor': 1169.10,
         'ativo': True, 'categoria': 'celular'},
        {'id': 11, 'nome': 'smartphone xiaomi redmi 13c 128gb 4gb ram', 'quantidade': 5, 'valor': 1079.10,
         'ativo': True, 'categoria': 'celular'},
        {'id': 12, 'nome': 'smartphone xiaomi redmi note 13 8gb de ram', 'quantidade': 2, 'valor': 1265.65,
         'ativo': True, 'categoria': 'celular'},
        {'id': 13, 'nome': 'cooktop a gas 5 bocas itatiaia essencial', 'quantidade': 3, 'valor': 438.24, 'ativo': True,
         'categoria': 'eletrodomestico'},
        {'id': 14, 'nome': 'maquina de lavar roupas 13kg brastemp bwk13 automatica', 'quantidade': 2, 'valor': 1705.49,
         'ativo': True, 'categoria': 'eletrodomestico'},
        {'id': 15, 'nome': 'micro ondas philco pmo23bb 20 litros', 'quantidade': 5, 'valor': 461.25, 'ativo': True,
         'categoria': 'eletrodomestico'},
        {'id': 16, 'nome': 'maquina de lavar 14kg electrolux led14', 'quantidade': 2, 'valor': 1934.22, 'ativo': True,
         'categoria': 'eletrodomestico'},
        {'id': 17, 'nome': 'fogao de piso suggar 4 bocas', 'quantidade': 2, 'valor': 737.44, 'ativo': True,
         'categoria': 'eletrodomestico'},
        {'id': 18, 'nome': 'geladeira electrolux dc35a branca', 'quantidade': 3, 'valor': 2108.99, 'ativo': True,
         'categoria': 'eletrodomestico'},
        {'id': 19, 'nome': 'notebook asus vivobook 15 intel pentium gold 4gb 128 gb ssd w11', 'quantidade': 3,
         'valor': 1619.99, 'ativo': True, 'categoria': 'notebook'},
        {'id': 20, 'nome': 'notebook asus x515 celeron dual core n4020 128gb ssd 4gb w11', 'quantidade': 3,
         'valor': 1619.99, 'ativo': True, 'categoria': 'notebook'},
        {'id': 21, 'nome': 'notebook samsung galaxy book2 intel core i3 1215u 4gb 256gb ssd', 'quantidade': 2,
         'valor': 2189.00, 'ativo': True, 'categoria': 'notebook'},
        {'id': 22, 'nome': 'notebook lenovo ultrafino ideapad 3 amd ryzen 5 8gb 256gb ssd linux', 'quantidade': 2,
         'valor': 2069.10, 'ativo': True, 'categoria': 'notebook'},
        {'id': 23, 'nome': 'notebook lenovo thinkpad t480 intel core i5 8350u 8gb ddr4 256gb ssd', 'quantidade': 2,
         'valor': 2098.98, 'ativo': True, 'categoria': 'notebook'},
        {'id': 24, 'nome': 'notebook gigabyte u4 intel i5 1155g7 8gb 512gb m2', 'quantidade': 1, 'valor': 3239.91,
         'ativo': True, 'categoria': 'notebook'},
    ]
    vendas = [gerar_venda(i + 1, produtos) for i in range(24)]

    # Path dos Documentos:
    path_produtos = "dados/produtos.csv"
    path_vendas = "dados/vendas.csv"

    gerar_produtos(produtos, path_produtos)
    gerar_vendas(vendas, path_vendas)


if __name__ == '__main__':
    main()
