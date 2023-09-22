# FINAL BOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
import tkinter as tk
import webbrowser

# Função para abrir uma URL quando um botão é clicado


def open_url(url):
    webbrowser.open(url)


def open_computer_window():  # TODO
    # Cria uma nova janela (Toplevel)
    computer_window = tk.Toplevel(root)
    computer_window.title("CODING JANELA")
# Função para abrir a segunda janela

    button3 = tk.Button(computer_window, text="SEMESTRES", command=lambda: open_url(
        "https://www.notion.so/COMPUTER-SCIENCE-2267a62638ef425b86906fef56f07d8e"))
    button3.pack(pady=10)

    button5 = tk.Button(computer_window, text="CODING",
                        command=open_coding_window)
    button5.pack(pady=10)


def open_coding_window():  # PYTHON,SQL,JAVA
    # Cria uma nova janela (Toplevel)
    coding_window = tk.Toplevel(root)
    coding_window.title("CODING JANELA")
# Função para abrir a segunda janela

    button10 = tk.Button(coding_window, text="PYTHON", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/Python-172580d6a9a4449b83d6ca72ce841015"))
    button10.pack(pady=10)

    button11 = tk.Button(coding_window, text="SQL", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/SQL-7a0b2236581d49c4b4c536a77743bfd9"))
    button11.pack(pady=10)

    button12 = tk.Button(coding_window, text="JAVA", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/JAVA-0fd1968c1df24831953e441b5d6b0b29"))
    button12.pack(pady=10)

    button13 = tk.Button(coding_window, text="GIT", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/GIT-0a41f4b82d1d4fb8af555081a5737af3e"))
    button13.pack(pady=10)

    button14 = tk.Button(coding_window, text="HTML+CSS", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/HTML-E-CSS-075c5f8a6ca4460f9535ec6471e6c255"))
    button14.pack(pady=10)


def open_notion_window():  # AUTODESENV.,STUDYPLAN,TASKS,CADERNO DE ESTUDOS
    # Cria uma nova janela (Toplevel)
    notion_window = tk.Toplevel(root)
    notion_window.title("Segunda Janela")

    # Adiciona botões à segunda janela com URLs diferentes

    button8 = tk.Button(notion_window, text="CADERNO DE ESTUDOS", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/Caderno-de-Estudos-37afdea3440742ce92149562654b0460"))
    button8.pack(pady=10)

    button6 = tk.Button(notion_window, text="STUDY PLAN", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/Painel-de-estudos-be5f1187717441dfb34e5cb6c2d25683"))
    button6.pack(pady=10)

    button7 = tk.Button(notion_window, text="TASKS", command=lambda: open_url(
        "https://www.notion.so/andrey-cruzn/Tasks-3436182303524ae79da8d82a7190bb3b"))
    button7.pack(pady=10)

    button4 = tk.Button(notion_window, text="AUTODESENV.", command=lambda: open_url(
        "https://www.notion.so/andreycomputacao/13ade7e89a5648bb946421dd1773ff47?v=a2d463ba0b754f15b16a563a0b2175e3"))
    button4.pack(pady=10)


def open_third_window():  # BOTOES INDEFINIDOS
    # Cria uma nova janela (Toplevel)
    third_window = tk.Toplevel(root)
    third_window.title("Terceira Janela")

    # Adiciona botões à terceira janela com URLs diferentes
    button6 = tk.Button(third_window, text="Botão 1",
                        command=lambda: open_url("https://www.link4.com"))
    button6.pack(pady=10)

    button7 = tk.Button(third_window, text="Botão 2",
                        command=lambda: open_url("https://www.link5.com"))
    button7.pack(pady=10)

    button8 = tk.Button(third_window, text="Botão 3",
                        command=lambda: open_url("https://www.link6.com"))
    button8.pack(pady=10)


# Cria a janela principal
root = tk.Tk()
root.title("Meu Aplicativo")

# Cria um botão na janela principal que abre a segunda janela
button = tk.Button(root, text="NOTION", command=open_notion_window)
button.pack(pady=10)

# Cria um botão na janela principal que abre a terceira janela
button2 = tk.Button(root, text="COMPUTER", command=open_computer_window)
button2.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
