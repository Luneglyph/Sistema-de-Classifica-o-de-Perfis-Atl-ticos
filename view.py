# view.py
# camada de interface grafica do sistema

import customtkinter as ctk
from controller import Controller

class View:
    def __init__(self):
        # cria a janela principal
        self.root = ctk.CTk()
        self.root.title("FitCluster")
        self.root.geometry("900x700")
        
        # cria o controller passando self
        self.controller = Controller(self)
        
        # cores do sistema
        self.cor_verde = "#a4d65e"
        self.cor_branco = "#ffffff"
        self.cor_cinza_claro = "#f0f0f0"
        
        # cria o header com os botoes de navegacao
        self.criar_header()
        
        # container principal onde as telas vao aparecer
        self.container_principal = ctk.CTkFrame(self.root, fg_color=self.cor_branco)
        self.container_principal.pack(fill="both", expand=True, padx=0, pady=0)
        
        # mostra a tela de cadastro inicialmente
        self.mostrar_tela_cadastro()
    
    def criar_header(self):
        # cria o header verde com os botoes de navegacao
        header = ctk.CTkFrame(self.root, fg_color=self.cor_verde, height=70)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # frame para o logo e titulo
        frame_logo = ctk.CTkFrame(header, fg_color=self.cor_verde)
        frame_logo.pack(side="left", padx=20)
        
        # logo FC
        label_logo = ctk.CTkLabel(frame_logo, text="FC", font=("Arial", 20, "bold"), 
                                  text_color="white", fg_color="#8bc53f", 
                                  width=40, height=40, corner_radius=5)
        label_logo.pack(side="left", padx=(0, 10))
        
        # titulo
        label_titulo = ctk.CTkLabel(frame_logo, text="FitCluster", 
                                    font=("Arial", 20, "bold"), text_color="white")
        label_titulo.pack(side="left")
        
        # frame para os botoes de navegacao
        frame_botoes = ctk.CTkFrame(header, fg_color=self.cor_verde)
        frame_botoes.pack(side="right", padx=20)
        
        # botoes de navegacao
        btn_cadastro = ctk.CTkButton(frame_botoes, text="Cadastro", 
                                     command=self.mostrar_tela_cadastro,
                                     fg_color="white", text_color="black",
                                     hover_color=self.cor_cinza_claro,
                                     width=100, height=35)
        btn_cadastro.pack(side="left", padx=5)
        
        btn_graficos = ctk.CTkButton(frame_botoes, text="Gráficos",
                                     command=self.mostrar_tela_graficos,
                                     fg_color="white", text_color="black",
                                     hover_color=self.cor_cinza_claro,
                                     width=100, height=35)
        btn_graficos.pack(side="left", padx=5)
        
        btn_perfis = ctk.CTkButton(frame_botoes, text="Perfis",
                                   command=self.mostrar_tela_perfis,
                                   fg_color="white", text_color="black",
                                   hover_color=self.cor_cinza_claro,
                                   width=100, height=35)
        btn_perfis.pack(side="left", padx=5)
    
    def limpar_container(self):
        # limpa o container principal para trocar de tela
        for widget in self.container_principal.winfo_children():
            widget.destroy()
    
    def mostrar_tela_cadastro(self):
    # limpa e mostra a tela de cadastro
        self.limpar_container()
    
    # frame principal da tela
        frame_tela = ctk.CTkFrame(self.container_principal, fg_color=self.cor_branco)
        frame_tela.pack(fill="both", expand=True, padx=40, pady=30)
    
    # titulo da tela
        label_titulo = ctk.CTkLabel(frame_tela, text="Cadastro de Usuário",
                                font=("Arial", 24, "bold"), text_color="black")
        label_titulo.pack(anchor="w", pady=(0, 20))
    
    # linha verde abaixo do titulo
        linha = ctk.CTkFrame(frame_tela, fg_color=self.cor_verde, height=3)
        linha.pack(fill="x", pady=(0, 30))
    
    # frame para o formulario
        form_frame = ctk.CTkFrame(frame_tela, fg_color=self.cor_branco)
        form_frame.pack(fill="both", expand=True)
    
    # nome completo
        label_nome = ctk.CTkLabel(form_frame, text="Nome Completo", 
                              font=("Arial", 14), text_color="gray")
        label_nome.grid(row=0, column=0, sticky="w", pady=(0, 5))
    
        self.entry_nome = ctk.CTkEntry(form_frame, width=400, height=35,
                                   placeholder_text="Digite o nome completo")
        self.entry_nome.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 20))
    
    # peso e altura na mesma linha
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
    
    # arremesso e flexibilidade na mesma linha
        label_arremesso = ctk.CTkLabel(form_frame, text="Arremesso MB (m)",
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
    
    # abdominal e salto na mesma linha
        label_abd = ctk.CTkLabel(form_frame, text="Abdominais (reps)",
                             font=("Arial", 14), text_color="gray")
        label_abd.grid(row=6, column=0, sticky="w", pady=(0, 5), padx=(0, 20))
    
        label_salto = ctk.CTkLabel(form_frame, text="Salto Horizontal (cm)",
                               font=("Arial", 14), text_color="gray")
        label_salto.grid(row=6, column=1, sticky="w", pady=(0, 5))
    
        self.entry_abd = ctk.CTkEntry(form_frame, width=190, height=35,
                                  placeholder_text="Ex: 45")
        self.entry_abd.grid(row=7, column=0, sticky="w", pady=(0, 30), padx=(0, 20))
    
        self.entry_salto = ctk.CTkEntry(form_frame, width=190, height=35,
                                    placeholder_text="Ex: 220")
        self.entry_salto.grid(row=7, column=1, sticky="w", pady=(0, 30))
    
    # botao de cadastrar
        btn_cadastrar = ctk.CTkButton(form_frame, text="Cadastrar Usuário",
                                  command=self.processar_cadastro,
                                  fg_color=self.cor_verde,
                                  hover_color="#8bc53f",
                                  text_color="white",
                                  font=("Arial", 14, "bold"),
                                  width=200, height=40)
        btn_cadastrar.grid(row=8, column=0, columnspan=2, pady=20)
    
    def mostrar_tela_graficos(self):
    # limpa e mostra a tela de graficos
        self.limpar_container()
    
        # frame principal da tela
        frame_tela = ctk.CTkFrame(self.container_principal, fg_color=self.cor_branco)
        frame_tela.pack(fill="both", expand=True, padx=40, pady=30)
    
        # titulo da tela
        label_titulo = ctk.CTkLabel(frame_tela, text="Análise e Clustering",
                                font=("Arial", 24, "bold"), text_color="black")
        label_titulo.pack(anchor="w", pady=(0, 20))
    
        # linha verde abaixo do titulo
        linha = ctk.CTkFrame(frame_tela, fg_color=self.cor_verde, height=3)
        linha.pack(fill="x", pady=(0, 30))
    
        # frame para o grafico
        frame_grafico = ctk.CTkFrame(frame_tela, fg_color=self.cor_cinza_claro,
                                 width=800, height=400, corner_radius=10)
        frame_grafico.pack(pady=(0, 30))
        frame_grafico.pack_propagate(False)
    
        # gera o grafico
        self.gerar_grafico_clusters(frame_grafico)
    
        # frame para os contadores de perfis
        frame_contadores = ctk.CTkFrame(frame_tela, fg_color=self.cor_branco)
        frame_contadores.pack(fill="x")
    
        # pega os usuarios cadastrados para contar
        usuarios = self.controller.listar_usuarios()
    
        # conta quantos usuarios tem em cada perfil
        contadores = {"Força": 0, "Explosivo": 0, "Atlético": 0, "Flexível": 0}
        for usuario in usuarios:
            perfil = usuario.get('perfil', 'Desconhecido')
            if perfil in contadores:
                contadores[perfil] += 1
    
        # cores dos perfis
        cores_perfis = {
        "Força": "#e74c3c",
        "Explosivo": "#f39c12",
        "Atlético": "#27ae60",
        "Flexível": "#9b59b6"
        }
    
    # cria os cards de contadores
        perfis = ["Força", "Explosivo", "Atlético", "Flexível"]
        for i, perfil in enumerate(perfis):
            card = ctk.CTkFrame(frame_contadores, fg_color=cores_perfis[perfil],
                           width=180, height=80, corner_radius=10)
            card.grid(row=0, column=i, padx=10)
            card.pack_propagate(False)
        
            label_perfil = ctk.CTkLabel(card, text="Perfil " + perfil,
                                   font=("Arial", 14, "bold"),
                                   text_color="white")
            label_perfil.pack(pady=(15, 5))
        
            label_count = ctk.CTkLabel(card, text=str(contadores[perfil]) + " usuários",
                                  font=("Arial", 12),
                                  text_color="white")
            label_count.pack()
    
    def mostrar_tela_perfis(self):
        # limpa e mostra a tela de perfis
        self.limpar_container()
        print("mostrando tela de perfis")
        # vamos implementar isso depois
    
    def run(self):
        # inicia o loop da interface
        self.root.mainloop()
    
    def processar_cadastro(self):
    # pega os dados dos campos
        nome = self.entry_nome.get()
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        arremesso = float(self.entry_arremesso.get())
        flexibilidade = float(self.entry_flex.get())
        abdominal = float(self.entry_abd.get())
        salto = float(self.entry_salto.get())
    
    # monta o dicionario de dados
        dados_usuario = {
            'nome': nome,
            'peso': peso,
            'altura': altura,
            'arremessoMB': arremesso,
            'flexibilidade': flexibilidade,
            'abdominal': abdominal,
            'salto_horizontal': salto
    }
    
    # envia para o controller processar
        resultado = self.controller.cadastrar_usuario(dados_usuario)
    
    # limpa os campos apos cadastrar
        self.entry_nome.delete(0, 'end')
        self.entry_peso.delete(0, 'end')
        self.entry_altura.delete(0, 'end')
        self.entry_arremesso.delete(0, 'end')
        self.entry_flex.delete(0, 'end')
        self.entry_abd.delete(0, 'end')
        self.entry_salto.delete(0, 'end')
    
        print("usuario cadastrado:", resultado)
    
    def gerar_grafico_clusters(self, frame_pai):
    # importa matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    
    # pega os dados ja preparados do controller
        dados_por_cluster, usuarios_dados = self.controller.get_dados_para_grafico()
    
    # cria a figura do matplotlib
        fig, ax = plt.subplots(figsize=(9, 5))
    
    # cores para cada cluster
        cores = ['#e74c3c', '#f39c12', '#27ae60', '#9b59b6']
    
    # plota os dados de treino
        for cluster in range(4):
            dados = dados_por_cluster[cluster]
            ax.scatter(dados['saltos'], dados['abdominais'], c=cores[cluster], 
                    label=f'Cluster {cluster}', alpha=0.6, s=100)
    
    # plota os usuarios cadastrados
        for usuario in usuarios_dados:
            cluster = usuario['cluster']
            ax.scatter(usuario['salto'], usuario['abdominal'], c=cores[cluster], 
                  marker='*', s=300, edgecolors='black', linewidths=2)
    
        ax.set_xlabel('Salto Horizontal (cm)', fontsize=12)
        ax.set_ylabel('Abdominais (reps)', fontsize=12)
        ax.set_title('Gráfico de Dispersão dos Clusters\n(Usuários cadastrados + dados de treinamento)',
                fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    # incorpora o grafico no frame do tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame_pai)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)