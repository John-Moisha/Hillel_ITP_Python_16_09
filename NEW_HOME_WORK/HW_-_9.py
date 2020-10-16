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

def f_path_to_folder(path='./'):
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

path = "../../Hillel_ITP_Python_16_09"
print_f = f_path_to_folder(path)
print(print_f)

# Дан файл authors.txt
# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
# 1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата и указание на чей-то день рождения или смерти.
# Например 8th February 1828 и слова birthday или death.
#
# 2) Для каждой строки полученной в пункте 1, вернуть словарь в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# 3) Из словарей, полученных в пункте 2, создать список словарей.
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
#
# 4) Из словарей, полученных в пункте 2, создать список словарей с днем рождения и смерти (если есть).
# Например [{"name": "Charles Dickens", "b_date": "07/02/1812", "d_date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "b_date": "01/01/1919"}]
