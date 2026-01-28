arquivo = "agenda.csv"

nomes = []
telefones = []
enderecos = []
notas = []
favoritos = []  


def carregar(nomes, telefones, enderecos, notas, favoritos):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                n, t, e, no, fav = linha.strip().split(";")
                nomes.append(n)
                telefones.append(t)
                enderecos.append(e)
                notas.append(no)
                favoritos.append(int(fav))
    except FileNotFoundError:
        open(arquivo, "w", encoding="utf-8").close()


def salvar(nomes, telefones, enderecos, notas, favoritos):
    with open(arquivo, "w", encoding="utf-8") as f:
        for i in range(len(nomes)):
            f.write(
                nomes[i] + ";" +
                telefones[i] + ";" +
                enderecos[i] + ";" +
                notas[i] + ";" +
                str(favoritos[i]) + "\n"
            )


def mostrar(nomes, telefones, enderecos, notas, favoritos):
    if len(nomes) == 0:
        print("Agenda vazia")
    else:
        for i in range(len(nomes)):
            estrela = "#" if favoritos[i] == 1 else " "
            print(f"{i} - {estrela} {nomes[i]} | {telefones[i]} | {enderecos[i]} | {notas[i]}")


def cadastrar(nomes, telefones, enderecos, notas, favoritos):
    nome = input("Nome: ")
    tel = input("Telefone: ")
    end = input("Endereço: ")
    nota = input("Nota/Observação: ")

    nomes.append(nome)
    telefones.append(tel)
    enderecos.append(end)
    notas.append(nota)
    favoritos.append(0)

    salvar(nomes, telefones, enderecos, notas, favoritos)
    print("Contato cadastrado!")


def alterar(nomes, telefones, enderecos, notas, favoritos):
    mostrar(nomes, telefones, enderecos, notas, favoritos)
    try:
        pos = int(input("Qual contato alterar: "))
        alt_nome = input("Deseja alterar nome? (s/n) ")
        if alt_nome == 's' or 'S':
            nomes[pos] = input("Insira o novo nome: ")
        else:
            i += 0
        telefones[pos] = input("Novo telefone: ")
        enderecos[pos] = input("Novo endereço: ")
        notas[pos] = input("Nova nota: ")
        salvar(nomes, telefones, enderecos, notas, favoritos)
        print("Contato alterado!")
    except (ValueError, IndexError):
        print("Erro ao alterar contato")


def excluir(nomes, telefones, enderecos, notas, favoritos):
    mostrar(nomes, telefones, enderecos, notas, favoritos)
    try:
        pos = int(input("Qual contato excluir: "))
        nomes.pop(pos)
        telefones.pop(pos)
        enderecos.pop(pos)
        notas.pop(pos)
        favoritos.pop(pos)
        salvar(nomes, telefones, enderecos, notas, favoritos)
        print("Contato excluído!")
    except (ValueError, IndexError):
        print("Erro ao excluir contato")


def buscar(nomes, telefones, enderecos, notas, favoritos):
    termo = input("Buscar nome: ").lower()
    achou = False
    for i in range(len(nomes)):
        if termo in nomes[i].lower():
            estrela = "#" if favoritos[i] == 1 else " "
            print(f"{estrela} {nomes[i]} - {telefones[i]} | {enderecos[i]} | {notas[i]}")
            achou = True
    if not achou:
        print("Contato não encontrado")


def favoritar(nomes, favoritos):
    mostrar(nomes, telefones, enderecos, notas, favoritos)
    try:
        pos = int(input("Qual contato favoritar: "))
        favoritos[pos] = 1
        salvar(nomes, telefones, enderecos, notas, favoritos)
        print("Contato favoritado!")
    except (ValueError, IndexError):
        print("Erro ao favoritar")

def desfavoritar(nomes, telefones, enderecos, notas, favoritos):
    if len(nomes) == 0:
        print("Agenda vazia.")
        return

    mostrar(nomes, telefones, enderecos, notas, favoritos)

    try:
        pos = int(input("Digite o índice do contato para desfavoritar: "))


        if favoritos[pos] == 0:
            print("Esse contato já não é favorito.")
            return

        favoritos[pos] = 0
        salvar(nomes, telefones, enderecos, notas, favoritos)
        print(f"Contato '{nomes[pos]}' foi removido dos favoritos.")

    except ValueError:
        print("Digite apenas números.")




def menu():
    print("\n1 - Mostrar contatos")
    print("2 - Cadastrar")
    print("3 - Alterar")
    print("4 - Excluir")
    print("5 - Buscar")
    print("6 - Favoritar")
    print("7 - Desfavoritar")
    print("8 - Sair")
    return int(input("Escolha: "))

carregar(nomes, telefones, enderecos, notas, favoritos)

while True:
    op = menu()

    if op == 1:
        mostrar(nomes, telefones, enderecos, notas, favoritos)
    elif op == 2:
        cadastrar(nomes, telefones, enderecos, notas, favoritos)
    elif op == 3:
        alterar(nomes, telefones, enderecos, notas, favoritos)
    elif op == 4:
        excluir(nomes, telefones, enderecos, notas, favoritos)
    elif op == 5:
        buscar(nomes, telefones, enderecos, notas, favoritos)
    elif op == 6:
        favoritar(nomes, favoritos)
    elif op == 7:
        desfavoritar(nomes, telefones, enderecos, notas, favoritos)
    elif op == 8:
        print("Fim do programa...")
        break
    else:
        print("Opção inválida")