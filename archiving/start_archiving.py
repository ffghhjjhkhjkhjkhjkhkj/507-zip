import os
import sys

def archiving(name_archive, namefolderforzip):
    print("Начало упаковки...")
    if ";" in name_archive:
        print("ОБНАРУЖЕНА ИНЬЕКЦИЯ КОМАНДЫ!")
        sys.exit(137)

    if ";" in namefolderforzip:
        print("ОБНАРУЖЕНА ИНЬЕКЦИЯ КОМАНДЫ!")
        sys.exit(137)

    os.system("zip -r " + name_archive + " " + namefolderforzip)
    print("УПАКОВКА ЗАВЕРШЕНА!!!!")

def archiving_tar(name_archive, namefolderforzip):
    print("Начало упаковки...")
    if ";" in name_archive:
        print("ОБНАРУЖЕНА ИНЬЕКЦИЯ КОМАНДЫ!")
        sys.exit(137)
    if ";" in namefolderforzip:
        print("ОБНАРУЖЕНА ИНЬЕКЦИЯ КОМАНДЫ!")
        sys.exit(137)
    os.system("tar czf " + name_archive + ".tar.gz" " -c " + namefolderforzip)
    print("УПАКОВКА ЗАВЕРШЕНА!!!!")
