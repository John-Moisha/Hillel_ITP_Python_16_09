# 0-express) Создать (и назвать) функцию, которой передает полный путь к папке
# в виде строки в формате "./path/to/folder",
# где точка означает текущую директорию.
# Функция возвращает СЛОВАРЬ в формате:
# {"files": [список ФАЙЛОВ из папки], "folders": [список ПОДПАПОК из папки]}.
# Пример использования:
# path_dict = this_function(path)
# Значение по умолчанию - текущая папка.
# Т.е. this_function() вернет словарь с файлами и подпапками из текущей папки.
import os
#
#
def f_path_to_folder(path="./"):
    files = []
    folders = []
    list_dir = sorted(os.listdir(path))
    if path:
        for item in list_dir:
            path_item = os.path.join(path, item)
            if os.path.isfile(path_item):
                files.append(item)
            else:
                folders.append(item)

    dicts = {"Files": files,
             "Folders": folders}
    return dicts
#или можно сделать корневую папку через os.path.abspath(os.curdir)
path = "./Test_file_folder"
print_f = f_path_to_folder()
print(print_f)