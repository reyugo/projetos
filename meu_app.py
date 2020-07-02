from tkinter import *

janela = Tk()

class AppLocation():
    def __init__(self):
        self.janela = janela
        self.Tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        janela.mainloop()


    def Tela(self):
        self.janela.title('CADASTRO DE CLIENTES')
        self.janela.configure(background='#8FBC8F')
        self.janela.geometry('800x600')
        self.janela.resizable(False, False)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=400, height=300)
        
    def frames_de_tela(self):
        self.frame_1 = Frame(self.janela, bd= 4, bg= '#B0C4DE', 
                            highlightbackground= '#4682B4', highlightthickness= 3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame_2 = Frame(self.janela, bd= 4, bg= '#B0C4DE', 
                            highlightbackground= '#4682B4', highlightthickness= 3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
    
    def widgets_frame_1(self):
        #Criaçao de Botoes
        self.bt_limpar = Button(self.frame_1, text='Limpar')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text='Buscar')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text='Novo')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text='Alterar')
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text='Apagar')
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
         
         
         #Criaçao de entrada de codigo e Label
        self.lb_codigo = Label(self.frame_1, text='Codigo')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #Criaçao de entrada de nome e Label
        self.lb_nome = Label(self.frame_1, text='Nome')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.codigo_nome = Entry(self.frame_1)
        self.codigo_nome.place(relx=0.05, rely=0.45, relwidth=0.7)


AppLocation()
