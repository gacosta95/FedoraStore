import os
install = 'S'
os.system("clear")

#Função que imprime uma linha com 109 caracteres '#'
def lin():
    print("#"*109)

#Atualizando sistema
print("Atualizando lista de pacotes, isso pode levar alguns minutos...")
os.system("dnf update -y")
os.system("clear")

#Função que mostra a tela
def tela():
    lin()
    print("||                                       fedora  Minimalist_Install                                         ||")
    lin()
    print("|| Editores de texto      || Downloads/Navegadores   || Música/Players          || Monit/Janelas           ||")
    print("|| 1 - Vim                || 1 - Transmission        || 1 - Spotify             || 1 - Htop                ||")
    print("|| 2                      || 2 - Google Chrome       ||                         || 2 - Neofetch            ||")
    print("|| 3 - NeoVim             || 3 - Opera               ||                         || 3 - Conky               ||")
    print("|| 4 - Emacs              || 4 - Tor Browser         ||                         || 4 - i3                  ||")
    print("|| 5 - Nano               ||                         ||                         || 5 - Xfce                ||")
    print("|| 6 - Gedit              ||                         ||                         || 6 -                     ||")
    print("|| 7 - VisualCode         ||                         ||                         || 7 - Kde                 ||")
    print("|| 8 - BlueFish           ||                         ||                         ||                         ||")
    print("||                        ||                         ||                         ||                         ||")
    lin()

#Laço de repetição que repete o bloco de código abaixo enquanto a opção escolhida for igual a S
while install =='S':
    
    tela()
    install = str(input("Digite o nome do programa que deseja instalar com base na lista acima, ou digite 'Todos' para instalar todos os programas listado:  "))
    
    if install == "Vim":
        os.system("dnf install vim -y")
        install = str (input('Quer continuar? [S/N]: ')).upper()
        os.system("clear")
    
    elif install == "Emacs":
        os.system("dnf install emacs -y")
        install = str (input("Quer continuar? [S/N:] ")).upper()
        os.system("clear")
    
    elif install == "NeoVim":
        os.system("dnf install neovim -y")
        install =str (input("Quer continuar? [S/N]")).upper()
        os.system("clear")

    elif install == "Nano":
        os.system("dnf install nano -y")
        install = str (input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")

    elif install == "Transmission":
        os.system("dnf install transmission-cli -y")
        install = str (input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
    
    elif install == "Htop":
        os.system("dnf install htop -y")
        install = str (input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
    
    elif install == "Conky":
        os.system("dnf install conky -y")
        
    elif install == "neofetch":
        install = str (input("Quer continuar? [S/N]: ")).upper()
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

    elif install  == "Spotify":
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo") #Adicionando o repositório
        os.system("dnf install spotify-client -y") #instalando...
        install = str (input("Quer continuar? [S/N]: ")).upper()
        os.system("clear")
    
    elif install == "Todos":
        os.system("flatpak install --user https://flathub.org/repo/appstream/nl.openoffice.bluefish.flatpakref -y")
        os.system("flatpak --user update nl.openoffice.bluefish -y")
        os.system("dnf install vim -y")
        os.system("dnf install emacs -y")
        os.system("dnf install neovim -y")
        os.system("dnf install nano -y")
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo") #Adicionando o repositório
        os.system("dnf install spotify-client -y") 
        os.system("dnf install transmission-cli -y")
        os.system("dnf install htop -y")
        os.system("dnf install neofetch -y")
        os.system("dnf install conky")
        os.system("clear")

    else:
        print("Nome invalido, por favor digite os nomes dos programas conforme descritos!")
#Author: Gabriel Alves
