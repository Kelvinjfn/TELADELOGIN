from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores
co0 = "#fof3f5" # Preta
co1 = "#feffff" # Branca
co2 = "#3fb5a3" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra


# Criando Janela
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a Janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando Frame Cima
l_nome = Label(frame_cima, text="LOGIN", anchor=NE, font=("Ivy 25"), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text="", width=275,  anchor=NW, font=("Ivy 1"), bg=co2, fg=co4)
l_linha.place(x=10, y=45)

credenciais = ["Kelvin", "123456789"]

def verifica_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Seja bem vindo Admin!!!")
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo("Login", "Seja bem vindo de volta " + credenciais[0])
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
        nova_janela()
    else:
        messagebox.showwarning("Erro", "Verifique o nome e a senha.")

def nova_janela():
    l_nome = Label(frame_cima, text="Usuário: " + credenciais[0], anchor=NE, font=("Ivy 20"), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text="", width=275,  anchor=NW, font=("Ivy 1"), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)
    
    l_nome = Label(frame_baixo, text="Seja bem vindo " + credenciais[0], anchor=NE, font=("Ivy 20"), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

# Configurando Frame Baixo
l_nome = Label(frame_baixo, text="Nome *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid" )
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="Senha *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify="left", show="*", font=("", 15), highlightthickness=1, relief="solid" )
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, command=verifica_senha, text="Entrar", width=39, height=2, font=("Ivy 8 bold"), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)




janela.mainloop()