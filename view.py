import customtkinter as ctk
from controller import Controller
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class View:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("FitCluster")
        self.root.geometry("520x660")
        
        self.controller = Controller(self)
        
        self.cor_verde = "#a4d65e"
        self.cor_branco = "#ffffff"
        self.cor_cinza_claro = "#f0f0f0"
        
        self.criar_header()

        self.container_principal = ctk.CTkFrame(self.root, fg_color=self.cor_branco)
        self.container_principal.pack(fill="both", expand=True, padx=0, pady=0)
        
        self.mostrar_tela_cadastro()
    
    def criar_header(self):
        header = ctk.CTkFrame(self.root, fg_color=self.cor_verde, height=70)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        frame_logo = ctk.CTkFrame(header, fg_color=self.cor_verde)
        frame_logo.pack(side="left", padx=20)
        
        label_logo = ctk.CTkLabel(frame_logo, text="FC", font=("Arial", 20, "bold"), 
                                  text_color="white", fg_color="#8bc53f", 
                                  width=40, height=40, corner_radius=5)
        label_logo.pack(side="left", padx=(0, 10))
        
        label_titulo = ctk.CTkLabel(frame_logo, text="FitCluster", 
                                    font=("Arial", 20, "bold"), text_color="white")
        label_titulo.pack(side="left")
        
        frame_botoes = ctk.CTkFrame(header, fg_color=self.cor_verde)
        frame_botoes.pack(side="right", padx=20)
        
        btn_cadastro = ctk.CTkButton(frame_botoes, text="Cadastro", 
                                     command=self.mostrar_tela_cadastro,
                                     fg_color="white", text_color="black",
                                     hover_color=self.cor_cinza_claro,
                                     width=100, height=35)
        btn_cadastro.pack(side="left", padx=5)
        
        btn_perfis = ctk.CTkButton(frame_botoes, text="Perfis",
                                   command=self.mostrar_tela_perfis,
                                   fg_color="white", text_color="black",
                                   hover_color=self.cor_cinza_claro,
                                   width=100, height=35)
        btn_perfis.pack(side="left", padx=5)
    
    def limpar_container(self):
        for widget in self.container_principal.winfo_children():
            widget.destroy()
    
    def mostrar_tela_cadastro(self):
        self.limpar_container()
        
        frame_tela = ctk.CTkFrame(self.container_principal, fg_color=self.cor_branco)
        frame_tela.pack(fill="both", expand=True, padx=40, pady=30)
        
        label_titulo = ctk.CTkLabel(frame_tela, text="Cadastro de usuario",
                                    font=("Arial", 24, "bold"), text_color="black")
        label_titulo.pack(anchor="w", pady=(0, 30))
        
        form_frame = ctk.CTkFrame(frame_tela, fg_color=self.cor_branco)
        form_frame.pack(fill="both", expand=True)
        
        label_nome = ctk.CTkLabel(form_frame, text="Nome Completo", 
                                  font=("Arial", 14), text_color="gray")
        label_nome.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.entry_nome = ctk.CTkEntry(form_frame, width=400, height=35,
                                       placeholder_text="Digite seu nome completo")
        self.entry_nome.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 20))
        
        label_peso = ctk.CTkLabel(form_frame, text="Peso (kg)",
                                  font=("Arial", 14), text_color="gray")
        label_peso.grid(row=2, column=0, sticky="w", pady=(0, 5), padx=(0, 20))
        
        label_altura = ctk.CTkLabel(form_frame, text="Altura (cm)",
                                    font=("Arial", 14), text_color="gray")
        label_altura.grid(row=2, column=1, sticky="w", pady=(0, 5))
        
        self.entry_peso = ctk.CTkEntry(form_frame, width=190, height=35,
                                       placeholder_text="Ex: 75.5")
        self.entry_peso.grid(row=3, column=0, sticky="w", pady=(0, 20), padx=(0, 20))
        
        self.entry_altura = ctk.CTkEntry(form_frame, width=190, height=35,
                                         placeholder_text="Ex: 175")
        self.entry_altura.grid(row=3, column=1, sticky="w", pady=(0, 20))
        
        label_arremesso = ctk.CTkLabel(form_frame, text="Arremesso (m)",
                                       font=("Arial", 14), text_color="gray")
        label_arremesso.grid(row=4, column=0, sticky="w", pady=(0, 5), padx=(0, 20))
        
        label_flex = ctk.CTkLabel(form_frame, text="Flexibilidade (cm)",
                                  font=("Arial", 14), text_color="gray")
        label_flex.grid(row=4, column=1, sticky="w", pady=(0, 5))
        
        self.entry_arremesso = ctk.CTkEntry(form_frame, width=190, height=35,
                                            placeholder_text="Ex: 5.2")
        self.entry_arremesso.grid(row=5, column=0, sticky="w", pady=(0, 20), padx=(0, 20))
        
        self.entry_flex = ctk.CTkEntry(form_frame, width=190, height=35,
                                       placeholder_text="Ex: 45")
        self.entry_flex.grid(row=5, column=1, sticky="w", pady=(0, 20))
        
        label_abd = ctk.CTkLabel(form_frame, text="Abdominais (reps)",
                                 font=("Arial", 14), text_color="gray")
        label_abd.grid(row=6, column=0, sticky="w", pady=(0, 5), padx=(0, 20))
        
        label_salto = ctk.CTkLabel(form_frame, text="Salto horizontal (cm)",
                                   font=("Arial", 14), text_color="gray")
        label_salto.grid(row=6, column=1, sticky="w", pady=(0, 5))
        
        self.entry_abd = ctk.CTkEntry(form_frame, width=190, height=35,
                                      placeholder_text="Ex: 45")
        self.entry_abd.grid(row=7, column=0, sticky="w", pady=(0, 30), padx=(0, 20))
        
        self.entry_salto = ctk.CTkEntry(form_frame, width=190, height=35,
                                        placeholder_text="Ex: 220")
        self.entry_salto.grid(row=7, column=1, sticky="w", pady=(0, 30))
        
        btn_cadastrar = ctk.CTkButton(form_frame, text="Cadastrar usuario",
                                      command=self.processar_cadastro,
                                      fg_color=self.cor_verde,
                                      hover_color="#8bc53f",
                                      text_color="white",
                                      font=("Arial", 14, "bold"),
                                      width=200, height=40)
        btn_cadastrar.grid(row=8, column=0, columnspan=2, pady=20)
    
    def processar_cadastro(self):
        nome = self.entry_nome.get()
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        arremesso = float(self.entry_arremesso.get())
        flexibilidade = float(self.entry_flex.get())
        abdominal = float(self.entry_abd.get())
        salto = float(self.entry_salto.get())
        
        dados_usuario = {
            'nome': nome,
            'peso': peso,
            'altura': altura,
            'arremessoMB': arremesso,
            'flexibilidade': flexibilidade,
            'abdominal': abdominal,
            'salto_horizontal': salto
        }
        
        resultado = self.controller.cadastrar_usuario(dados_usuario)
        
        self.entry_nome.delete(0, 'end')
        self.entry_peso.delete(0, 'end')
        self.entry_altura.delete(0, 'end')
        self.entry_arremesso.delete(0, 'end')
        self.entry_flex.delete(0, 'end')
        self.entry_abd.delete(0, 'end')
        self.entry_salto.delete(0, 'end')
        
        print("usuario cadastrado:", resultado)
    
    def mostrar_tela_perfis(self):
        self.limpar_container()
        
        frame_tela = ctk.CTkFrame(self.container_principal, fg_color=self.cor_branco)
        frame_tela.pack(fill="both", expand=True, padx=40, pady=30)
        
        label_titulo = ctk.CTkLabel(frame_tela, text="Usuarios Cadastrados",
                                    font=("Arial", 24, "bold"), text_color="black")
        label_titulo.pack(anchor="w", pady=(0, 30))
        
        scroll_frame = ctk.CTkScrollableFrame(frame_tela, fg_color=self.cor_branco,
                                              width=420, height=450)
        scroll_frame.pack(fill="both", expand=True)
        
        usuarios = self.controller.listar_usuarios()
        
        if not usuarios:
            label_vazio = ctk.CTkLabel(scroll_frame, text="Nenhum usuario cadastrado ainda.",
                                       font=("Arial", 14), text_color="gray")
            label_vazio.pack(pady=50)
        else:
            for usuario in usuarios:
                self.criar_card_usuario(scroll_frame, usuario)
    
    def criar_card_usuario(self, frame_pai, usuario):
        card = ctk.CTkFrame(frame_pai, fg_color=self.cor_cinza_claro,
                           corner_radius=10, height=100)
        card.pack(fill="x", pady=10, padx=5)
        
        frame_conteudo = ctk.CTkFrame(card, fg_color=self.cor_cinza_claro)
        frame_conteudo.pack(fill="both", expand=True, padx=15, pady=15)
        
        nome = usuario.get('nome', 'Sem nome')
        label_nome = ctk.CTkLabel(frame_conteudo, text=nome,
                                  font=("Arial", 16, "bold"), text_color="black")
        label_nome.pack(anchor="w")
        
        imc = usuario.get('imc', 0)
        perfil = usuario.get('perfil', 'Desconhecido')
        info_texto = "IMC: " + str(imc) + " - Perfil: " + perfil
        label_info = ctk.CTkLabel(frame_conteudo, text=info_texto,
                                  font=("Arial", 12), text_color="gray")
        label_info.pack(anchor="w", pady=(5, 5))
        
        recomendacao = usuario.get('recomendacao', 'Nenhuma')
        label_rec = ctk.CTkLabel(frame_conteudo, text="Recomendado: " + recomendacao,
                                font=("Arial", 12), text_color="green")
        label_rec.pack(anchor="w")
        
        frame_botoes = ctk.CTkFrame(card, fg_color=self.cor_cinza_claro)
        frame_botoes.pack(side="right", padx=15)
        
        btn_ver = ctk.CTkButton(frame_botoes, text="Ver Perfil",
                               command=lambda: self.mostrar_perfil_individual(usuario),
                               fg_color=self.cor_verde,
                               hover_color="#8bc53f",
                               width=80, height=30)
        btn_ver.pack(side="left", padx=5)
        
        usuario_id = str(usuario['_id'])
        btn_deletar = ctk.CTkButton(frame_botoes, text="X",
                                    command=lambda: self.deletar_usuario(usuario_id),
                                    fg_color="red",
                                    hover_color="#c0392b",
                                    width=30, height=30)
        btn_deletar.pack(side="left", padx=5)
    
    def mostrar_perfil_individual(self, usuario):
        self.limpar_container()
        frame_tela = ctk.CTkFrame(self.container_principal, fg_color=self.cor_branco)
        frame_tela.pack(fill="both", expand=True, padx=40, pady=30)
        
        nome = usuario.get('nome', 'Usuário')
        label_titulo = ctk.CTkLabel(frame_tela, text="Perfil: " + nome,
                                    font=("Arial", 20, "bold"), text_color="black")
        label_titulo.pack(anchor="w", pady=(0, 20))
        
        frame_dados = ctk.CTkFrame(frame_tela, fg_color=self.cor_cinza_claro, corner_radius=10)
        frame_dados.pack(fill="x", pady=(0, 20))
        
        label_secao1 = ctk.CTkLabel(frame_dados, text="Dados Pessoais",
                                    font=("Arial", 14, "bold"), text_color="black")
        label_secao1.pack(anchor="w", padx=15, pady=(10, 5))
        
        imc = usuario.get('imc', 0)
        perfil = usuario.get('perfil', 'Desconhecido')
        
        texto_dados = "IMC: " + str(imc) + "\nPerfil Atlético: " + perfil
        label_dados = ctk.CTkLabel(frame_dados, text=texto_dados,
                                   font=("Arial", 12), text_color="gray",
                                   justify="left")
        label_dados.pack(anchor="w", padx=15, pady=(0, 10))
        
        frame_fisicos = ctk.CTkFrame(frame_tela, fg_color=self.cor_cinza_claro, corner_radius=10)
        frame_fisicos.pack(fill="x", pady=(0, 20))
        
        label_secao2 = ctk.CTkLabel(frame_fisicos, text="Dados Físicos",
                                    font=("Arial", 14, "bold"), text_color="black")
        label_secao2.pack(anchor="w", padx=15, pady=(10, 5))
        
        frame_metricas = ctk.CTkFrame(frame_fisicos, fg_color=self.cor_cinza_claro)
        frame_metricas.pack(fill="x", padx=15, pady=(0, 10))
        
        peso = usuario.get('peso', 0)
        altura = usuario.get('altura', 0)
        arremesso = usuario.get('arremessoMB', 0)
        
        texto_col1 = "Peso: " + str(peso) + "kg\nAltura: " + str(altura) + "cm\nArremesso: " + str(arremesso) + "m"
        label_col1 = ctk.CTkLabel(frame_metricas, text=texto_col1,
                                 font=("Arial", 12), text_color="gray",
                                 justify="left")
        label_col1.pack(side="left", anchor="w")
        
        flexibilidade = usuario.get('flexibilidade', 0)
        abdominal = usuario.get('abdominal', 0)
        salto = usuario.get('salto_horizontal', 0)
        
        texto_col2 = "Flexibilidade: " + str(flexibilidade) + "cm\nAbdominais: " + str(abdominal) + " reps\nSalto Horizontal: " + str(salto) + "cm"
        label_col2 = ctk.CTkLabel(frame_metricas, text=texto_col2,
                                 font=("Arial", 12), text_color="gray",
                                 justify="left")
        label_col2.pack(side="left", anchor="w", padx=(40, 0))
        
        frame_radar = ctk.CTkFrame(frame_tela, fg_color=self.cor_cinza_claro,
                                  corner_radius=10, height=250)
        frame_radar.pack(fill="x", pady=(0, 10))
        frame_radar.pack_propagate(False)
        
        self.gerar_radar_chart(frame_radar, usuario)
        
        frame_rec = ctk.CTkFrame(frame_tela, fg_color="#68816e", corner_radius=10)
        frame_rec.pack(fill="x")
        
        recomendacao = usuario.get('recomendacao', 'Nenhuma')
        label_rec_titulo = ctk.CTkLabel(frame_rec, text="Recomendação:",
                                       font=("Arial", 12, "bold"), text_color="#155724")
        label_rec_titulo.pack(anchor="w", padx=15, pady=(10, 2))
        
        label_rec_texto = ctk.CTkLabel(frame_rec, text=recomendacao,
                                      font=("Arial", 14), text_color="#155724")
        label_rec_texto.pack(anchor="w", padx=15, pady=(0, 10))

    def gerar_radar_chart(self, frame_pai, usuario):
        categorias, valores, angles = self.controller.get_dados_radar(usuario)

        fig, ax = plt.subplots(figsize=(5, 4), subplot_kw=dict(projection='polar'))
        ax.plot(angles, valores, 'o-', linewidth=2, color='#27ae60')
        ax.fill(angles, valores, alpha=0.25, color='#27ae60')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categorias)
        
        canvas = FigureCanvasTkAgg(fig, master=frame_pai)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def deletar_usuario(self, usuario_id):
        self.controller.deletar_usuario(usuario_id)
        self.mostrar_tela_perfis()
    
    def run(self):
        self.root.mainloop()