
from datetime import datetime
from nursery_model import Model


class View:
    operations = {"m": "self.print_menu()", 
                  "1": "self.print_all_animals()", 
                  "2": "self.add_animal()",
                  "3": "self.add_command()"
                  }

    def __init__(self):
        self.orm = Model()

    def start(self):
        try:
            count = self.orm.read_db()
        except Exception as e:
            print('error! ', e)
            exit()

        print(f"подключение к БД... количество записей: {count}")
        run = True
        self.print_menu()
        while run:
            user_input = input("выберите операцию: (0 - выход, m - показать меню): ")
            if user_input == "0":
                run = not run
                continue
            oper = self.operations.get(user_input, False)
            if oper:
                eval(oper)

    def print_menu(self):
        print( " --- список действий --- \n"+
               "1 - показать весь список животных \n"+
               "2 - добавить новое животное\n"+
               "3 - добавить выученную команду\n"
               )

    def print_all_animals(self):
        data = self.orm.get_all_animals()
        if len(data) == 0:
            print("список пуст")
        else:
            for entry in data:
                print(entry[0], 
                      ' |  команды: ' if (entry[1]) else '', 
                      ', '.join(entry[1]))

    def add_animal(self):
        ok = False
        titles = self.orm.get_titles()
        while not ok:
            print(' --- список доступных животных --- ')
            for key,val in titles.items():
                print(key, ' - ', val)
            title = input("введите номер добавляемого животного: (0 - выход): ")
            if title == "0": return
            if title.isdigit() and titles.get(int(title), False):
                ok = True
        ok = False
        while not ok:
            nickname = input("введите кличку, не менее 3 символов, уникальную: (0 - выход): ")
            if nickname == "0":     return
            if len(nickname) > 2:   ok = True
        ok = False
        while not ok:
            birthday = input("введите дату рождения, в формате дд-мм-гггг: (0 - выход): ")
            if birthday == "0":     return
            try:
                birthday = datetime.strptime(birthday, "%d-%m-%Y")
                ok = True
            except Exception as e:
                print(e)

        try:
            self.orm.add_animal(nickname, birthday, titles.get(int(title)))
        except Exception as e:
            print('error! ', e)
            
    def add_command(self):
        ok = False
        while not ok:
            self.print_all_animals()
            id = input("введите id животного из списка: (0 - выход): ")
            if id == "0": return
            if id.isdigit():
                animal = self.orm.get_animal(int(id))
                if animal:
                    print(animal[0], ' |  команды: ' if (animal[1]) else '', ', '.join(animal[1]))
                    ok = True
        ok = False 
        comm_list = self.orm.get_commands_list()
        while not ok:
            print(' --- список доступных команд --- ')
            for key,val in comm_list.items():
                print(key, ' - ', val)
            comm = input("введите номер команды: (0 - выход): ")
            if comm == "0": return
            if comm.isdigit() and comm_list.get(int(comm), False):
                ok = True
                if animal[0].is_knows(comm):
                    print('животное уже умеет это')
                else:
                    try:
                        self.orm.add_command(animal[0].get_id(), int(comm))
                    except Exception as e:
                        print('error! ', e)

