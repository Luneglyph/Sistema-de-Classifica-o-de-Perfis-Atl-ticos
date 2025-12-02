# main.py
# arquivo principal que inicializa o sistema

from view import View

def main():
    # cria apenas a view
    # a view cria o controller
    # o controller cria o model
    view = View()
    view.run()

if __name__ == "__main__":
    main()