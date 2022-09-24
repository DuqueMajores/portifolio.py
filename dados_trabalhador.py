from datetime import datetime

print('=' * 30)
print(' = CADASTRO DO TRABALHADOR =')
print('=' * 30)
cadastros = []
while True:
    op = int(input('[ 1 ] Cadastrar\n'
                   '[ 2 ] Mostrar Cadastros\n'
                   '[ 3 ] Sair\n'
                   '>>> '))
    print('-' * 30)
    if op == 1:
        dados = {'nome': str(input('Nome: ')),
                 'idade': int(input('Ano de Nascimento: ')),
                 'ctps': int(input('Carteira de Trabalho: '))}
        if dados['ctps'] == 0:
            print('=' * 30)
            idade = datetime.now().year - dados['idade']
            print(f'O nome é: {dados["nome"]}\n'
                  f'Com idade de {idade} anos\n'
                  f'Ctps com valor 0')
            dados['idade'] = idade
            cadastros.append(dados.copy())
        if dados['ctps'] > 0:
            idade = datetime.now().year - dados['idade']
            dados['contrato'] = int(input('Ano de contratação: '))
            dados['salario'] = int(input('Salário: '))
            apo = (dados['contrato'] + 35) - dados['idade']
            dados['Aposentadoria'] = dados['contrato'] + 35
            print('=' * 30)
            print(f'O nome é: {dados["nome"]}\n'
                  f'Com idade de {idade} anos\n'
                  f'Ctps de número: {dados["ctps"]}\n'
                  f'Começou a trabalhar em {dados["contrato"]}\n'
                  f'Ganha um salário de R${dados["salario"]}\n'
                  f'E vai se aposentar com {apo} anos')
            dados['idade'] = idade
            cadastros.append(dados.copy())
        del dados
        print('=' * 30)
    if op == 2:
        if len(cadastros) == 0:
            print('Você ainda não cadastrou ninguem')
        else:
            for c in cadastros:
                for k, v in c.items():
                    print(f'{k}: {v}', end=' ')
                    print()
                print('-' * 30)
    if op == 3:
        print('Sando do Programa')
        break
