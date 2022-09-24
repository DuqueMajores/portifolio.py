pessoas = list()
mulher = list()
dado = dict()
media = 0
title = 'ANÁLISE DE GRUPO'
print('=' * 30)
print(f'{title:^30}')
print('=' * 30)
while True:
    op = str(input('[ 1 ] Cadastrar\n'
                   '[ 2 ] Quantidade de Cadastros\n'
                   '[ 3 ] Média Idade do Grupo\n'
                   '[ 4 ] Lista de Mulheres\n'
                   '[ 5 ] Finalizar Programa\n'
                   '>>> '))
    print('-' * 30)
    if op not in '12345':
        print('Erro: Tente de novo...')
        print('=' * 30)
        continue
    if op in '1':
        dado['nome'] = str(input('Nome: ')).strip()
        dado['idade'] = int(input('Idade: '))
        dado['sexo'] = str(input('Sexo [M/F]: ')).strip().upper
        media += dado['idade']
        if dado['sexo'] == 'F':
            mulher.append(dado.copy())
        pessoas.append(dado.copy())
        del dado['nome']
        del dado['sexo']
        del dado['idade']
        print('=' * 30)
    if op in '2':
        if len(pessoas) < 1:
            print('Ninguem foi cadastrado;\n'
                  'Escolha [ 1 ] para cadastar...')
        elif len(pessoas) == 1:
            print('Foi cadastrado uma pessoa:')
        else:
            print(f'Foram cadatrados {len(pessoas)} pessoas: ')
        print('-' * 30)
        for c in pessoas:
            for k, v in c.items():
                print(f'{k}: {v}', end=' ')
                print()
            print('-' * 30)
        print('=' * 30)
    if op in '3':
        if len(pessoas) < 1:
            print('Não há pessoas registradas\n'
                  'Digite [ 1 ] para registrar')
            print('=' * 30)
            continue
        if len(pessoas) == 1:
            print('Preciso de mais pessoas cadastradas...')
        else:
            print(f'A média da idade de todas as pessoas\n'
                  f'registradas é de {media / len(pessoas):.2f} anos')
        print('=' * 30)
    if op in '4':
        if len(mulher) < 1:
            print('Não foi registrado nenhuma mulher\n'
                  'Digite [ 1 ] para registar...')
            print('=' * 30)
            continue
        if len(mulher) == 1:
            print('Você só registrou uma mulher')
        else:
            print('Aqui está uma lista de todas\n'
                  'as mulheres cadastradas:')
        print()
        for c in mulher:
            for k, v in c.items():
                print(f'{k}: {v}', end=' ')
                print()
            print('-' * 30)
        print('=' * 30)
    if op in '5':
        print('Finalizando Programa')
        break
