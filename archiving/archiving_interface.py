from archiving.start_archiving import archiving

def start_of_interface_in_archiving():
    print("Отлично! прошу обратить внимание что это БЕТА функция!")
    print("Напишите какое имя сделать архиву в который вы будете упаковывать файлы:")
    name_archive = input()
    print("Выберите в какой формат архива архивировать файлы:")
    print("")
    print("1: ZIP")
    print("2: TAR (не работает)")
    tiparchiveforzip = input()
    if tiparchiveforzip == "1":
        print("Отлично напишите название папкии которую упаковать:")
        namefolderforzip = input()
        archiving(name_archive, namefolderforzip)