import random
import string
import json
import csv

# Создать класс FileWriter.
# При инициализации передается обязательный параметр filename с путем, именем и расширением создаваемого файла.
# И необязательный параметр file_data - для txt файла - строка, для json файла - словарь,
# для csv файла - список списков чисел. Если file_data отсутствует - класс генерирует данные самостоятельно.
#
# Единственный метод, который доступен пользователю - write().
# До его вызова класс ничего записывать не должен.
#
# пример использования:
# my_writer = FileWriter("./test_tmp/test.txt")
# my_writer.write()
#
# За основу для генерирования данных взять решение ДЗ № 10

class FileWriter:
    def __init__(self, __path_data, __file_data=None):
        self.__path_data = __path_data
        self.__type_f = self.__path_data.rsplit(".")[-1]
        if not __file_data:
            if self.__type_f == "txt":
                self.__file_data = self.__gen_txt()
            elif self.__type_f == "json":
                self.__file_data = self.__gen_json()
            elif self.__type_f == "csv":
                self.__file_data = self.__gen_csv()
            else:
                raise Exception("Unsupported file format!")
        else:
            self.__file_data = __file_data
        print(f"{self.__type_f} Записан в: {self.__path_data}, \nС Данными: \n----------\n{self.__file_data}\n")

        # Gen TXT
    def __gen_txt(self ,min_len=100, max_len=1000) -> str:
        alphavit = str(string.ascii_letters + string.digits + ' ' + '.' + ',' + ';')
        stroka100_1000 = (''.join(random.choice(alphavit) for _ in range(random.randint(min_len, max_len))))
        inxs_random = list(set([random.randint(1, len(stroka100_1000) - 1) for _ in range(9)]))
        list_s_100_1000 = list(stroka100_1000)
        for index, value in enumerate(list_s_100_1000):
            for i in inxs_random:
                if index == i:
                    list_s_100_1000.remove(value)
                    list_s_100_1000.insert(i, '\n')
                else:
                    pass

        return "".join(list_s_100_1000)

    #Gen JSON
    @staticmethod
    def __rand_chois_val(__val):
        if __val == 1:
            t_or_f = [True, False]
            __val = random.choice(t_or_f)
        if __val == 2:
            __val = random.randint(-100, 100)
        if __val == 3:
            __val = random.uniform(0, 1)
        return __val

    def __gen_json(self, min_key=5, max_key=20):
        alphavit = str(string.ascii_letters + string.punctuation)
        return {(''.join(random.choice(alphavit) for _ in range(5))): self.__rand_chois_val(random.randint(1, 3)) for key in
                range(random.randint(min_key, max_key))}

    #Gen CSV
    def __gen_csv(self, n_min=3, m_max=10):
        n_stroka = random.randint(n_min, m_max)
        m_stolb = random.randint(n_min, m_max)
        tabl_out = [[random.randint(0, 1) for _ in range(m_stolb)] for _ in range(n_stroka)]
        return tabl_out

    def write(self):
        __type_f = self.__type_f
        __data_f = self.__file_data
        __path_d = self.__path_data
        if __type_f == "txt":
            with open(__path_d, 'w') as file:
                file.write(__data_f)
        elif __type_f == "json":
            with open(__path_d, 'w') as file:
                json.dump(__data_f, file, indent=2)
        elif __type_f == "csv":
            with open(__path_d, 'w') as file:
                writer = csv.writer(file, dialect='excel')
                writer.writerows(__data_f)

        else:
            raise Exception("Unsupported file format!")


my_writer_TXT = FileWriter("./text.txt")
my_writer_TXT.write()

my_writer_CSV = FileWriter("./text.csv")
my_writer_CSV.write()

my_writer_JSON = FileWriter("./text.json", "privet")
my_writer_JSON.write()
