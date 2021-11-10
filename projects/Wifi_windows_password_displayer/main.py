import glob
import os
import subprocess
import xml.etree.ElementTree as ET

class PwdDisplay:
    def __init__(self):
        # Définition du répertoire courant
        os.chdir("./")
        # Création du dossier mot de passe
        if not os.path.exists("passwords"):
            os.system("mkdir passwords")

        self.export_xml(command="netsh wlan export profile interface=wi-fi key=clear folder=passwords")
        self.display_password()

    def export_xml(self, command=None):
        with open("tmp.txt", "w") as tmp:
            export_command = command.split(' ')
            subprocess.run(export_command,stdout=tmp)
        os.remove("tmp.txt")

    def file_path(self) -> list[str]:
        # Obtention du chemin des fichiers xml
        chemin_fichiers = glob.glob("passwords/"+"*xml")
        return chemin_fichiers

    def get_ssid_pwd(self) -> list:
        ssid_pwd = {}
        for i in self.file_path():
            tree = ET.parse(i)
            root = tree.getroot()
            ssid = root[1][0][1].text # ssid
            pwd = root[4][0][1][2].text #pwd
            ssid_pwd[ssid] = pwd
        return ssid_pwd

    def display_password(self):
        index=1
        info = self.get_ssid_pwd()
        list_ssid, list_pwd = [], []
        print("Here is the list of Wi-Fi networks registered on this device : \n")
        for i in info:
            print(f"[{index}] {i}")
            list_ssid.append(i)
            list_pwd.append(info[i])
            index+=1

        nb = int(input("Please choose a number : "))
        print(f"SSID : {list_ssid[nb-1]}\nPassword : {list_pwd[nb-1]}\n")

    def __del__(self):
        print("Thanks for using my tool :)")
        # Supression des fichiers
        for i in self.file_path():
            if os.path.exists(i):
                os.remove(i)


if __name__ == '__main__':
    instance = PwdDisplay
    instance()
