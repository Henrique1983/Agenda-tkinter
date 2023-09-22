from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# storage in memory
agenda = []
index = 0

# Funções
def adicionarContato() -> None:
    # Pegando o valor digitado em txt_nome
    nome = txt_nome.get()
    telefone = txt_Telefone.get()
    categoria = cb_categorias.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria

    }
    agenda.append(contato)
    limparCampos()
    atualizarTabela()
    messagebox.showinfo("Sucesso!", "Contato adicionado com sucesso!")

def editarContato() -> None:
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_Telefone.get(),
        "categoria": cb_categorias.get()
    }
    atualizarTabela()
    limparCampos()
    
def deletarContato() -> None:
    agenda.remove(agenda[index])
    messagebox.showinfo("Deletado!", "Contato apagado com sucesso!")
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_Telefone.delete(0, END)
    cb_categorias.set("")

def atualizarTabela() -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert("", END, values=(contato["nome"],
                                       contato["telefone"],
                                       contato["categoria"]))

def tabelaClique(event) -> None:
    # Obtendo a linha clicada
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada[0])
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['nome'])
    txt_Telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])

# Criando a janela
janela = Tk()
janela.title("Agenda Telefonica")

# Labels
label_nome = Label(janela, text="Nome:", fg="red", font="Tahoma 14 bold")
label_nome.grid(row=0, column=0)

# Entry
txt_nome = Entry(janela, font="Tahoma 14", width=27)
txt_nome.grid(row=0, column=1)

label_Telefone = Label(janela, text="Telefone:", fg="red", font="Tahoma 14 bold")
label_Telefone.grid(row=1, column=0)

txt_Telefone = Entry(janela, font="Tahoma 14", width=27)
txt_Telefone.grid(row=1, column=1)

# Combobox
label_categorias = Label(janela, text="Categoria:", fg="red", font="Tahoma 14 bold")
label_categorias.grid(row=2, column=0)

categorias = ["Amigos", "Família", "Trabalho"]
cb_categorias = ttk.Combobox(janela, values=categorias, width=25, font="Tahoma 14")
cb_categorias.grid(row=2, column=1)

# Botão
btn_adicionar = Button(janela, text="Adicionar", fg="red", font="Tahoma 12 bold", width=8, command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text="Editar", fg="red", font="Tahoma 12 bold", width=8, command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar = Button(janela, text="Deletar", fg="red", font="Tahoma 12 bold", width=8, command=deletarContato)
btn_deletar.grid(row=3, column=2)

colunas = ["Nome", "Telefone", "Categoria"]
# Criando uma tabela/TreeView
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
tabela.heading("Nome", text="Nome")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Categoria", text="Categoria")
tabela.grid(row=4, columnspan=3)

# Criando uma bind
tabela.bind("<ButtonRelease-1>", tabelaClique)

# Executa a janela
janela.mainloop()