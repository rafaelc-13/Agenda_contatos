class Contato():
    def __init__ (self, nome, sobrenome, cel, mail):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cel = cel
        self.mail = mail

class Agenda():
    def __init__(self):
        self.contatos = []

    @staticmethod
    def validarNumeroCel(cel):
        if cel.isdigit() and len(cel) == 10:
            return True
        else:
            return False

    def adicionarContato(self,nome, sobrenome, cel, mail):
        if validarNumeroCel(cel):
            contato = Contato(nome,sobrenome, cel, mail)
            self.contatos.append(contato)
            print("Contato adicionado com sucesso!")
        else:
            print("Numero de celular inválido. Certifique-se de inserir 10 digitos numericos.")

    def removerContato(self,nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                certeza = input(f"Você tem certeza que deseja remover {contato.nome} (S/N)?  ").upper()
                if certeza == "N":
                    print("Operação cancelada.")
                elif certeza == 'S':
                    print(f"Contato {contato.nome} removido")
                    self.contatos.remove(contato)
                    break
        else:
            print("Não identificamos essa pessoa.")

    def listarContato(self):
        for x,contato in list(self.contatos):
            print(f"{x}º - {contato.nome}. cel ({contato.cel})")

    def pesquisaContatos(self,nome):
        for x,contato in enumerate(self.contatos):
            if nome.lower() in contato.nome.lower():
                print(f'Seu contato é {self.contatos[x]} e se encontra no índice {x} da lista.')
        else:
            print("Conato não encontrado")

    def editarContato(self, indice, nome, sobrenome, cel, mail):
        if 0 <= indice < len(self.contatos):
            contato.nome = nome
            contato.sobrenome = sobrenome
            contato.cel = cel
            contato.mail = mail
            print("Contato atualizado com sucesso")
        else:
            print('Indice inválido! ')
