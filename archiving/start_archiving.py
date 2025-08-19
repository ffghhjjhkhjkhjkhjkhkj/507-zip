import os

def archiving(name_archive, namefolderforzip):
    print("Начало упаковки...")
    os.system("zip -r " + name_archive + " " + namefolderforzip)
    print("УПАКОВКА ЗАВЕРШЕНА!!!!")
