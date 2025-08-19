import os
import sys
import time
start_time = time.time()
def global_exception_handler(exc_type, exc_value, exc_traceback):
         e_id = "? (НЕИЗВЕСТНАЯ ОШИБКА)"
         print("")
         print("")
         print("")
         print("Ой. Извините но 507-zip словил неисправимую ошибку!")
         print("Пожалуйста сообщите об этом в issues на гитхабе")
         e = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
         print("")
         print("Возможная проблема:")
         if "'utf-8' codec can't decode byte" in e:
            print("Проблема с кодировкой возможно вы ввели НЕ UTF-8 символ")
            e_id = "108ФФ (ПРОБЛЕМА С КОДИРОВКОЙ)"
         if "EOFError" in e:
            print("Закрытый терминал")
            e_id = "186ЛК (ЗАКРЫТЫЙ ТЕРМИНАЛ)"
         if "KeyboardInterrupt" in e:
            print("Вы нажали Ctrl + C")
            e_id = "114ДЕ (НАЖАТИЕ CTRL + C)"
         print("")
         print("---------------------------------------") 
         print("Ошибка:")
         traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)
         print("---------------------------------------")
         print("")
         print("ВСЕ что идет после ЭТОГО сообщения пожалуйста отправьте в issues")
         print("")
         print("---------------------------------------")
         print("")
         print("ID ОШИБКИ: " + e_id)
         print("")
         print("ОС:")
         os.system("uname -a")
         print("")
         print("TRACEBACK:")
         print(e)
         print("")
         print("Версия 507-zip: 1.5")
         print(f"Время работы 507-zip: {time.time() - start_time:.2f} сек")
         print("---------------------------------------")
         print("Пока!")
sys.excepthook = global_exception_handler
import traceback
import resource
from archiving.archiving_interface import start_of_interface_in_archiving

resource.setrlimit(resource.RLIMIT_AS, (1_000_000_000, 1_000_000_000))  # 1 ГБ RAM



print("Добро пожаловать в инструмент для управления архивами 507-zip! от 507-team Кстати привет BISKAST!")
print("")
print("Выберите действие:")
print("1: Разархивировать архив")
print("2: Упаковать папку (BETA)")
print("")
choice = input()
if choice == "1":
    print("Выберите тип архива")
    print("1: ZIP")
    print("2: TAR")
    print("")
    print("(Что бы узнать тип архива посмотрите на конец файла .tar это TAR .zip это ZIP)")
    print("")
    tiparchiveforextract = input()
    if tiparchiveforextract == "1":
        print("Напишите название файла архива:")
        print("ВНИМАНИЕ!: ПОСЛЕ ЭТОГО ЕСЛИ В АРХИВЕ БЫЛИ ФАЙЛЫ КОТОРЫЕ НАЗЫВАЛИСЬ ТАКЖЕ КАК И В ЭТОЙ ДИРЕКТОРИИ ОНИ БУДУТ ПЕРЕЗАПИСАНЫ!")
        namearchiveforextract = input()
        print(namearchiveforextract)
        print("")
        print("Список файлов в архиве:")

        if  ";" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)

        if  "&&" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)


        if  "|" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)


        print("------------------------------------------------------")
        os.system("unzip -l " + namearchiveforextract)
        print("------------------------------------------------------")
        print("")
        if not os.path.exists(namearchiveforextract):
            print("Стоп а точно ли ты правильно ввел название? а то архива то такого тут нет!")
            print("Выход. Код: 2")
            sys.exit(2)
        print("И последнее... Создать подпапку? Y/N")
        cozdatpodpapkyforextract = input()
        podpapkaforextract = namearchiveforextract.replace(".zip", "")
        
        if cozdatpodpapkyforextract == "y":
            print("Создаю...")
            os.system("mkdir " + podpapkaforextract)
            print("Папка " + podpapkaforextract + " создана!")
            print("Распаковываю....")
            print("Нажмите Ctrl+C для отмены")
            outputofcommandinextracttwithcozdatpodpapky = os.popen("unzip -o " + namearchiveforextract + " -d " + podpapkaforextract + " 2>&1").read()
            if "bad zipfile offset" in outputofcommandinextracttwithcozdatpodpapky:
                print("Ой.... архив поврежден!")
                print("")
                print("Лог (для анализа):")
                print("----------------------------------------------------")
                print(outputofcommandinextracttwithcozdatpodpapky)
                print("----------------------------------------------------")
                print("")
                print("Выход")
                print("Выход. Код: 3")
                sys.exit(3)
            print("Распаковка завершена!")
            print("")
            print("--------------------------------------------------------")
            print("Список файлов/каталогов:")
            os.system("dir " + podpapkaforextract)
            print("--------------------------------------------------------")
            print("")
            print("Удачи!")


        if cozdatpodpapkyforextract == "n":
            print("Окей! папку создавать не буду буду сюда распаковывать")
            print("Распаковываю....")
            outputofcommandinextractt = os.popen("unzip -o " + namearchiveforextract + " 2>&1").read()
            if "bad zipfile offset" in outputofcommandinextractt:
                print("Ой.... архив поврежден!")
                print("")
                print("Лог (для анализа):")
                print("----------------------------------------------------")
                print(outputofcommandinextractt)
                print("----------------------------------------------------")
                print("")
                print("Выход")
                print("Выход. Код: 3")
                sys.exit(3)
            print("Распаковка завершена!")
            print("")
            print("Удачи!")

    if tiparchiveforextract == "2":
        print("Напишите название файла архива:")
        print("ВНИМАНИЕ!: ПОСЛЕ ЭТОГО ЕСЛИ В АРХИВЕ БЫЛИ ФАЙЛЫ КОТОРЫЕ НАЗЫВАЛИСЬ ТАКЖЕ КАК И В ЭТОЙ ДИРЕКТОРИИ ОНИ БУДУТ ПЕРЕЗАПИСАНЫ!")
        namearchiveforextract = input()
        print(namearchiveforextract)
        print("")
        print("Список файлов в архиве:")

        if  ";" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)

        if  "&&" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)


        if  "|" in (repr(namearchiveforextract)):
            print("СТОП! ОБНАРУЖЕНА ВОЗМОЖНАЯ ПОПЫТКА ИНЬЕКЦИИ КОМАНДЫ!")
            print("Выход. Код: 137")
            sys.exit(137)


        print("------------------------------------------------------")
        os.system("tar tvf " + namearchiveforextract)
        print("------------------------------------------------------")
        print("")
        if not os.path.exists(namearchiveforextract):
            print("Стоп а точно ли ты правильно ввел название? а то архива то такого тут нет!")
            print("Выход. Код: 2")
            sys.exit(2)
        print("И последнее... Создать подпапку? Y/N")
        cozdatpodpapkyforextract = input()
        podpapkaforextract = namearchiveforextract.replace(".tar", "")
        
        if cozdatpodpapkyforextract == "y":
            print("Создаю...")
            os.system("mkdir " + podpapkaforextract)
            print("Папка " + podpapkaforextract + " создана!")
            print("Распаковываю....")
            print("Нажмите Ctrl+C для отмены")
            outputofcommandinextracttwithcozdatpodpapky = os.popen("tar xvf " + namearchiveforextract + " --directory " + podpapkaforextract + " 2>&1").read()
            print("Распаковка завершена!")
            print("")
            print("--------------------------------------------------------")
            print("Список файлов/каталогов:")
            os.system("dir " + podpapkaforextract)
            print("--------------------------------------------------------")
            print("")
            print("Удачи!")


        if cozdatpodpapkyforextract == "n":
            print("Окей! папку создавать не буду буду сюда распаковывать")
            print("Распаковываю....")
            outputofcommandinextractt = os.popen("tar xvf " + namearchiveforextract + " 2>&1").read()
            if "bad zipfile offset" in outputofcommandinextractt:
                print("Ой.... архив поврежден!")
                print("")
                print("Лог (для анализа):")
                print("----------------------------------------------------")
                print(outputofcommandinextractt)
                print("----------------------------------------------------")
                print("")
                print("Выход")
                print("Выход. Код: 3")
                sys.exit(3)
            print("Распаковка завершена!")
            print("")
            print("Удачи!")

if choice == "2":
    start_of_interface_in_archiving()
