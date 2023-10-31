from Agenda_de_contatos import Contato, Agenda:
def menu(self):
    agenda = Agenda[]
    while True:
        print('''Selecione uma opção:
        1- Adicionar Contato
        2- Remover Contato
        3- Lista de Contatos
        4- Pesquisar conatato
        5- Editar contato''')

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            cel = int(input("Cel: "))
            mail = input("E-mail: ")
            Agenda.adicionarContato(nome,sobrenome,cel,mail)
        elif escolha == 2:
            nome = input("Digite corretamente quem você deseja remover: ").lower
            Agenda.removerContato(nome)
        elif escolha == 3:
            Agenda.listarContato()
        elif escolha == 4:
            pesquisa = input('Nome para pequisa: ')
            Agenda.pesquisaContatos(pesquisa)
        elif escolha == 5:
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            cel = int(input("Cel: "))
            mail = input("E-mail: ")
            indice = input("Posição na agenda (procurar na lista): ")
            Agenda.editarContato(indice, nome, sobrenome, cel, mail)





