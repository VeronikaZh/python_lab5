import csv
import glob


class Post(object):
    """
    Класс объекта Post
    """
    def __init__(self, post, comm, date, time, text, like):
        self.post = post
        self.comm = comm
        self.date = date
        self.time = time
        self.text = text
        self.like = like

    def __setattr__(self, attr, value):
        if attr == 'post':
            self.__dict__[attr] = value
        elif attr == 'comm':
            self.__dict__[attr] = value
        elif attr == 'date':
            self.__dict__[attr] = value
        elif attr == 'time':
            self.__dict__[attr] = value
        elif attr == 'text':
            self.__dict__[attr] = value
        elif attr == 'like':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def __repr__(self):
        return "post: " + self.post.join(("'", "'")) + " comm: " + self.comm.join(("'", "'")) + " date: " + \
               self.date.join(("'", "'")) + " time: " + self.time.join(("'", "'")) + " text: " + self.text.join(
               ("'", "'")) + " like: " + self.like.join(("'", "'"))


class FileWriter:
    """
    Класс, содержащий статические методы
    """
    @staticmethod
    def count_file():
        """
        Статический метод count_file выполняет подсчёт файлов в директории temp
        """
        print(len(glob.glob('/temp/*.txt')))

    @staticmethod
    def read_file():
        """
        Считывает строки из файла и записывает данные в лист data
        :return dic список объектов
        """
        dic = []
        with open("data.csv", "r", encoding='utf-8') as r_file:
            file = csv.DictReader(r_file, delimiter=",")
            for row in file:
                k = Post(row['post'], row['comm'], row['data'], row['time'], row['text'], row['like'])
                dic.append(k)
            return dic

    @staticmethod
    def write_new_data():
        """
        Добавление новой записи в файл
        """
        with open('data.csv', 'a', encoding='utf-8', newline='') as file:
            file.write("\n")
            file.write("{},{},{},{},{},{}".format(input("№ поста "), input("№ комментария "), input("дата "),
                                                  input("время "), input("текст комментария "),
                                                  input("количество лайков")))


class DictProc(FileWriter):
    def __init__(self, sl_sort):
        self.sl_sort = sl_sort

    def __repr__(self):
        return str(self.sl_sort)

    def __getitem__(self, i):
        return self.sl_sort[i]

    def output_data(self):
        """
        Вывод всех данных, содержит иттератор
        """
        obj_dic = iter(self)
        while True:
            try:
                print(next(obj_dic))
            except StopIteration:
                break
        print('\n')

    def sort_by_abc(self):
        """
        Сортировка списка объектов по тексту комментария
        """
        self.sl_sort = sorted(self.sl_sort, key=lambda name: name.text)
        self.output_data()

    def print_if(self):
        """
        Выводит данные, где like больше или равно 15
        """
        for elem in self:
            if int(elem.like) >= 15:
                print(elem)
        print('\n')


def main():
    """
    Главная функция, в которой происходит вызов остальных функций
    """
    data = DictProc.read_file()
    dat = DictProc(data)
    print("1 - Вывести все записи")
    print("2 - Сортировка записей по тексту комментария")
    print("3 - Вывод записи, в которой количество лайков больше 15")
    print("4 - Добавление новой записи в файл")
    print("5 - Подсчёт файлов в директории temp")
    while True:
        var = input()
        if var == "1":
            dat.output_data()
        elif var == "2":
            dat.sort_by_abc()
        elif var == "3":
            dat.print_if()
        elif var == "4":
            dat.write_new_data()
        elif var == "5":
            DictProc.count_file()
        else:
            print("Завершение работы")
            break


main()
