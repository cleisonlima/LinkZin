import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

# Função para encurtar link
def encurtar_link():
    url_original = entrada.get()
    
    if not url_original.strip():
        messagebox.showwarning("Aviso", "Digite um link para encurtar.")
        return

    try:
        api_url = f"https://tinyurl.com/api-create.php?url={url_original}"
        resposta = requests.get(api_url)
        
        if resposta.status_code == 200:
            link_encurtado = resposta.text
            resultado.config(state="normal")
            resultado.delete(0, tk.END)
            resultado.insert(0, link_encurtado)
            resultado.config(state="readonly")
        else:
            messagebox.showerror("Erro", "Não foi possível encurtar o link.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao encurtar link: {e}")

# Função para copiar link
def copiar_link():
    link = resultado.get()
    if link:
        pyperclip.copy(link)
        messagebox.showinfo("Copiado", "Link copiado para a área de transferência!")

# Janela principal
janela = tk.Tk()
janela.title("LinkZin")
janela.geometry("500x350")
janela.config(bg="#141414")

# Estilo
fonte_titulo = ("Comic Sans MS", 28, "bold")
fonte_normal = ("Arial", 12)
cor_botao = "#6A5ACD"       # Roxo estiloso
cor_botao_hover = "#836FFF" # Mais claro
cor_texto = "white"

# Função para hover nos botões
def on_enter(e, cor):
    e.widget.config(bg=cor_botao_hover)

def on_leave(e, cor):
    e.widget.config(bg=cor)

# Nome do App
tk.Label(
    janela, 
    text="✨ LinkZin ✨", 
    font=fonte_titulo, 
    bg="#141414", 
    fg="#00FFAA"
).pack(pady=15)

# Campo para digitar link
tk.Label(janela, text="Digite o link:", font=fonte_normal, bg="#141414", fg=cor_texto).pack()
entrada = tk.Entry(
    janela, width=50, font=fonte_normal, relief="flat", 
    bg="#2e2e3e", fg=cor_texto, insertbackground="white"
)
entrada.pack(pady=5)

# Botão encurtar
btn_encurtar = tk.Button(
    janela, text="Encurtar", font=fonte_normal, 
    bg=cor_botao, fg="white", relief="flat", command=encurtar_link
)
btn_encurtar.pack(pady=5)
btn_encurtar.bind("<Enter>", lambda e: on_enter(e, cor_botao))
btn_encurtar.bind("<Leave>", lambda e: on_leave(e, cor_botao))

# Resultado
tk.Label(janela, text="Link encurtado:", font=fonte_normal, bg="#141414", fg=cor_texto).pack()
resultado = tk.Entry(
    janela, width=50, font=fonte_normal, relief="flat", 
    bg="#2e2e3e", fg=cor_texto, 
    readonlybackground="#2e2e3e", state="readonly", insertbackground="white"
)
resultado.pack(pady=5)

# Botão copiar
btn_copiar = tk.Button(
    janela, text="Copiar", font=fonte_normal, 
    bg="#FF6347", fg="white", relief="flat", command=copiar_link
)
btn_copiar.pack(pady=5)
btn_copiar.bind("<Enter>", lambda e: on_enter(e, "#FF7F50"))
btn_copiar.bind("<Leave>", lambda e: on_leave(e, "#FF6347"))

# Rodapé com direito autoral
tk.Label(
    janela, 
    text="© 2025 José Cleison de Lima", 
    font=("Arial", 9, "italic"), 
    bg="#141414", 
    fg="#aaaaaa"
).pack(side="bottom", pady=10)

janela.mainloop()
