from archiving.start_archiving import archiving, archiving_tar

def start_of_interface_in_archiving():
    print("Отлично! прошу обратить внимание что это БЕТА функция!")
    print("Напишите какое имя сделать архиву в который вы будете упаковывать файлы:")
    name_archive = input()
    print("Выберите в какой формат архива архивировать файлы:")
    print("")
    print("1: ZIP")
    print("2: TAR")
    tiparchiveforzip = input()
    if tiparchiveforzip == "1":
        print("Отлично напишите название папки которую надо упаковать:")
        namefolderforzip = input()
        archiving(name_archive, namefolderforzip)
    
    if tiparchiveforzip == "2":
        print("Отлично напишите название папки которую надо упаковать")
        namefolderforzip = input()
        archiving_tar(name_archive, namefolderforzip)
