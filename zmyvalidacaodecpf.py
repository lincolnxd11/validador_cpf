while True:

    # Entrada do CPF
    cpf = input('Digite o CPF para validação: ')

    # Verifica se todos os caracteres são números
    try:
        int(cpf)
    except ValueError:
        print('Digite apenas os números do CPF.')
        continue

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        print('CPF deve ter 11 dígitos.')
        continue

    # Verifica se todos os números são iguais
    cpf_repetido = cpf[0] * len(cpf)

    if cpf == cpf_repetido:
        print('CPF inválido')
        continue

    # Cálculo do primeiro dígito
    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    soma_1 = 0

    for i in nove_digitos:
        soma_1 += contador_regressivo_1 * int(i)
        contador_regressivo_1 -= 1

    primeiro_digito = (soma_1 * 10) % 11
    primeiro_digito = 0 if primeiro_digito > 9 else primeiro_digito

    # Cálculo do segundo dígito
    dez_digitos = nove_digitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    soma_2 = 0

    for i in dez_digitos:
        soma_2 += contador_regressivo_2 * int(i)
        contador_regressivo_2 -= 1

    segundo_digito = (soma_2 * 10) % 11
    segundo_digito = 0 if segundo_digito > 9 else segundo_digito

    # Validação final
    cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    if cpf == cpf_gerado_pelo_calculo:
        print(f'O CPF {cpf} é válido.')
    else:
        print(f'O CPF {cpf} é inválido.')

    # Pergunta se o usuário quer continuar
    while True:

        opcao = input('Você deseja validar mais algum CPF? [SIM] [NAO]: ').lower().replace('ã', 'a')

        if opcao == 'sim':
            break
        elif opcao == 'nao':
            print('PROGRAMA FINALIZADO!')
            exit()
        else:
            print('Digite apenas [SIM] ou [NAO]')