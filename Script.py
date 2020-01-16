import os
os.system("pip install pyfiglet")
os.system("pip install prettytable")


import pyfiglet
import prettytable


print("Atualizando...")
os.system("dnf update -y")
install = "S"
os.system("clear")


def title():
    titulo = pyfiglet.figlet_format("FedoraStore")
    Pretty = prettytable.PrettyTable()
    print(titulo)


def tela():
    table = prettytable.PrettyTable()
    table.add_column("N ", ["1", "2", "3", "4", "5", "6", "7","8","9","10"])
    table.add_column("Texto", ["Vim", "NeoVim", "Emacs", "Nano", "Gedit", "VisualCode", "BlueFish", "","",""])
    table.add_column("Monit/Janelas", ["Htop", "Neofetch", "Conky", "i3", "Kde","",  "","","",""])
    table.add_column("Downloads/Navegadores", ["Transmission","Google Chrome", "Opera", "Tor", "Firefox Dev","Iceweasel",
                    "Icecat", "Slinjet", "konqueror", "Maxthon"])
    table.add_column("Musica",["Spotify","","","","","","","","",""])
    table.add_column("Video", ["Vlc player","","","","","","","","", ""])
    print(table)


title()
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

    elif install == "Firefox Dev":
        os.system("wget https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=pt-BR -O firefox-developer.tar.bz2")
        os.system("tar -jxvf  firefox-developer.tar.bz2 -C /opt/")
        os.system("sudo mv /opt/firefox*/ /opt/firefox-developer")
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
        os.system("clear")

    elif install == "VisualCode":
        os.system("dnf install snapd -y && clear")
        title()
        tela()
        os.system("ln -s /var/lib/snapd/snap /snap")
        os.system("snap install code --classic")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
        title()
        tela()
    
    elif install == "neofetch":
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
   
    elif install == "NeoFetch":
        os.system("dnf install neofetch -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
    
    elif install =="Opera":
        os.system("wget https://download4.operacdn.com/pub/opera/desktop/63.0.3368.43/linux/opera-stable_63.0.3368.43_amd64.rpm -O opera.rpm")
        os.system("sudo dnf install opera.rpm -y")
        install = str(input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Vlc player":
        os.system("sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E% fedora) .noarch.rpm -y")
        os.system("dnf install vlc")
        install = str(input("Quer continuar? [S/N] ")).upper()
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
        title()
        tela()
        os.system("dnf install vim -y")
        os.system("clear")
        title()
        tela()
        os.system("sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E% fedora) .noarch.rpm -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install vlc -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install emacs -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install neovim -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install nano -y")
        os.system("clear")
        title()
        tela()
        os.system("wget https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=pt-BR -O firefox-developer.tar.bz2")
        os.system("tar -jxvf  firefox-developer.tar.bz2 -C /opt/")
        os.system("sudo mv /opt/firefox*/ /opt/firefox-developer")
        os.system("clear")
        title()
        tela()
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo")  # Adicionando o repositório
        os.system("dnf install spotify-client -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install transmission-cli -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install htop -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install neofetch -y")
        os.system("clear")
        title()
        tela()
        os.system("dnf install conky")
        os.system("clear")
        
    else:
        print("Nome invalido, por favor digite os nomes dos programas conforme descritos!")

# Author: Gabriel Alves
