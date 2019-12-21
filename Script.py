import prettytable
import os

install = "S"
Pretty = prettytable.PrettyTable()
def tela():
    table = prettytable.PrettyTable()
    table.add_column("N ", ["1", "2", "3", "4", "5", "6", "7","8","9","10"])
    table.add_column("Texto", ["Vim", "NeoVim", "Emacs", "Nano", "Gedit", "Visual Code", "BlueFish", "","",""])
    table.add_column("Monit/Janelas", ["Htop", "Neofetch", "Conky", "i3", "Xfce", "Kde", "","","",""])
    table.add_column("Downloads/Navegadores", ["Transmission","Google Chrome", "Opera", "Tor", "Firefox Dev","Iceweasel",
                    "Icecat", "Slinjet", "konqueror", "Maxthon"])
    table.add_column("Musica",["Spotify","","","","","","","","",""])
    table.add_column("Video", ["Vlc player","","","","","","","","", ""])
    print(table)


print("Atualizando lista de pacotes e instalando dependencias, isso pode levar alguns minutos...")

os.system("dnf update -y")
os.system("clear")
print("instalando pip e baixando biblioteca necessária!")
os.system("dnf install pip -y")
os.system("pip install prettytable -y")
os.system("clear")

print("FedoraStore...\n\n")
while install == "S":
    tela()
    install = (input("Digite o nome do programa que deseja instalar,\nconforme descrito na tabela ou 'Todos' para instalar todos: "))
    if install == "Vim":
        os.system("dnf install vim -y")
        install = str(input('Quer continuar? [S/N]: ')).upper()
        os.system("clear")

    elif install == "Emacs":
        os.system("dnf install emacs -y")
        install = str(input("Quer continuar? [S/N:] ")).upper()
        os.system("clear")
    
    elif install == "NeoVim":
        os.system("dnf install neovim -y")
        install = str(input("Quer continuar? [S/N]")).upper()
        os.system("clear")

    elif install == "Nano":
        os.system("dnf install nano -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Transmission":
        os.system("dnf install transmission-cli -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Htop":
        os.system("dnf install htop -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
        
    elif install == "Conky":
        os.system("dnf install conky -y")

    elif install == "VisualCode":
        os.system("cd /etc/yum.repos.d && touch vscode.repo")
        os.system("echo Testando o diretorio criado! >> vscode.repo")

    elif install == "neofetch":
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "NeoFetch":
        os.system("dnf install neofetch -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "i3":
        os.system("dnf install i3")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "BlueFish":
        os.system("flatpak install --user https://flathub.org/repo/appstream/nl.openoffice.bluefish.flatpakref -y")
        os.system("flatpak --user update nl.openoffice.bluefish -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Spotify":
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo")  # Adicionando o repositório
        os.system("dnf install spotify-client -y")  # instalando...
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Todos":
        os.system("flatpak install --user https://flathub.org/repo/appstream/nl.openoffice.bluefish.flatpakref -y")
        os.system("flatpak --user update nl.openoffice.bluefish -y")
        os.system("clear")
        tela()
        os.system("dnf install vim -y")
        os.system("clear")
        tela()
        os.system("dnf install emacs -y")
        os.system("clear")
        tela()
        os.system("dnf install neovim -y")
        os.system("clear")
        tela()
        os.system("dnf install nano -y")
        os.system("clear")
        tela()
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo")  # Adicionando o repositório
        os.system("dnf install spotify-client -y")
        os.system("clear")
        tela()
        os.system("dnf install transmission-cli -y")
        os.system("clear")
        tela()
        os.system("dnf install htop -y")
        os.system("clear")
        tela()
        os.system("dnf install neofetch -y")
        os.system("clear")
        tela()
        os.system("dnf install conky")
        os.system("clear")
        
    else:
        print("Nome invalido, por favor digite os nomes dos programas conforme descritos!")
# Author: Gabriel Alves
