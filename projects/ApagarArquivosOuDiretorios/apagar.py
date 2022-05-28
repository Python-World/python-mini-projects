import os
import shutil

import PySimpleGUI as sg


def erase_file(path_filename):
    try:
        os.remove(path_filename)
        sg.Print(f"Arquivo..: {path_filename} - APAGADO!!!!")
    except PermissionError as p:
        print(p)


def recursive_listing(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
        for dirs in d:
            files.append(os.path.join(r, dirs))
    list_ = list(files)
    if list_:
        return list_
    print("Pasta sem arquivo...")
    return False


class Erase:
    def __init__(self):
        self.own_directory = ""

    def secure_delete_recursive(self, folder):
        self.own_directory = folder.split("/")[-1]
        if len(os.listdir(folder)) < 1:
            try:
                self._extracted_from_secure_delete_recursive_5(folder, 'Diretório..: ')
            except PermissionError as err:
                print(f'Deu problemas na exclusão do diretório..:{err}')
        else:
            has_files = recursive_listing(folder)
            if has_files:
                for obj in has_files:
                    if os.path.isfile(obj):
                        try:
                            os.remove(obj)
                            sg.Print(f"Arquivo..: {obj} - APAGADO!!!!")
                        except PermissionError as p:
                            print(p)

                for obj in has_files:
                    if os.path.isdir(obj):
                        try:
                            shutil.rmtree(obj, ignore_errors=False, onerror=None)
                            sg.Print(f"Diretório..: {obj} - APAGADO!!!!")
                        except PermissionError as p:
                            print(p)
            try:
                self._extracted_from_secure_delete_recursive_5(folder, 'Diretório LAST..: ')
            except PermissionError as err:
                print(f'Deu problemas na exclusão do diretório..:{err}')

    # TODO Rename this here and in `secure_delete_recursive`
    def _extracted_from_secure_delete_recursive_5(self, folder, arg1):
        shutil.rmtree(folder, ignore_errors=False, onerror=None)
        folder = folder.split("/")[-1]
        sg.Print(f'{arg1}{folder} - APAGADO!!!!')


class Tela:
    def __init__(self):
        self.erase = Erase()

    def list_folder(self):
        layout = [
            [
                sg.Frame(
                    layout=[
                        [sg.T("Diretório a ser apagado:")],
                        [
                            sg.In(key="input"),
                            sg.FolderBrowse(
                                "Folder", target="input", key="folder_selected"
                            ),
                        ],
                        [sg.Button("ViewDIRS", key="viewdirs")],
                    ],
                    title="Dirs",
                    title_color="yellow",
                    relief=sg.RELIEF_SUNKEN,
                    tooltip="Use these to set flags",
                )
            ],
            [
                sg.Frame(
                    layout=[
                        [sg.Text("Arquivo que será apagado:")],
                        [
                            sg.In(key="-OUTPUT-"),
                            sg.FileBrowse(
                                "Files",
                                target="-OUTPUT-",
                                key="filename",
                                file_types=(("Text Files", "*.*"),),
                            ),
                        ],
                        [sg.Button("ViewFILES", key="viewfiles")],
                    ],
                    title="Files",
                    title_color="yellow",
                    relief=sg.RELIEF_SUNKEN,
                    tooltip="Use these to set flags",
                )
            ],
            [sg.Text("_" * 80)],
            [
                sg.Frame(
                    "Botões",
                    [[sg.Button("Submit"), sg.Exit()]],
                    background_color="lightblue",
                    title_color="red",
                )
            ],
        ]
        window = sg.Window("Gerenciador", layout, size=(430, 330))
        while True:
            event, values = window.read()
            print(values)
            if "Submit" in event:
                if values["folder_selected"]:
                    folder = values["folder_selected"]
                    self.erase.secure_delete_recursive(folder)
                else:
                    path_filename = values["filename"]
                    erase_file(path_filename)
                values = None
            if "viewfiles" in event:
                filename = values["filename"]
                with open(filename, "r", encoding="utf-8") as _f:
                    archive = _f.read()
                sg.Print(archive)
            if "viewdirs" in event:
                filename = values["folder_selected"]
                list_files_directory = []
                for (_, dirnames, filenames) in os.walk(filename):
                    if dirnames:
                        list_files_directory.append(f"DIRS..:{dirnames}")
                    if filenames:
                        list_files_directory.append(f"FILES..:{filenames}")
                        list_files_directory.append(f'{"*" * 96}')
                sg.Print(list_files_directory, size=(100, 20), sep="+")
            if event == sg.WIN_CLOSED or "Exit" in event:
                sg.popup_auto_close("Exit...", auto_close_duration=0.5)
                break
        window.close()


if __name__ == "__main__":
    tela = Tela()
    tela.list_folder()
