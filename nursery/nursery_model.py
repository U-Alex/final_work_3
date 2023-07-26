
from mysql.connector import connect, Error
from nursery_entities import Animal_dog, Animal_cat, Animal_hamster, Animal_horse, Animal_camel, Animal_donkey

class Model:
    class_list = {'собаки': 'Animal_dog', 'кошки': 'Animal_cat', 'хомяки': 'Animal_hamster', 
                  'лошади': 'Animal_horse', 'верблюды': 'Animal_camel', 'ослы': 'Animal_donkey', }
    database='nursery'; user='root'; password='123123'; host='127.0.0.1'; port=3306

    def __init__(self):
        self.records = []
        self.a_title = {}
        self.commands_list = {}

    def read_db(self):
        try:
            with connect(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, name FROM animals_title order by id; ")
                    animal_title = cursor.fetchall()
                    cursor.execute("select a.id , a.nickname , a.birthday , a.parent_id , comm.comm_id from animals a \
	                                left join (select animals_id ,	group_concat(commands_id) as comm_id \
				                               from animals_commands ac group by animals_id ) as comm \
                                               on (comm.animals_id = a.id); ")
                    animal_list = cursor.fetchall()
                    cursor.execute("SELECT id, name FROM commands; ")
                    commands = cursor.fetchall()
        except Error as e:
            raise(e)

        for ob in animal_title:
            self.a_title[ob[0]] = ob[1]
        for ob in animal_list:
            init_class = self.class_list.get(self.a_title[ob[3]])
            comm_list = ob[4].split(',') if (ob[4]) else []
            self.records.append(eval(init_class)(ob[0], ob[1], ob[2], comm_list))
        for ob in commands:
            self.commands_list[ob[0]] = ob[1]
        
        return len(self.records)

    def get_all_animals(self):
        data = []
        for ob in self.records:
            comm = []
            for ob2 in ob.get_comm_list():
                comm.append(self.commands_list.get(int(ob2)))
            data.append([ob, comm])
        return data

    def get_animal(self, id):
        for ob in self.records:
            if ob.get_id() == id:
                comm = []
                for ob2 in ob.get_comm_list():
                    comm.append(self.commands_list.get(int(ob2)))
                return [ob, comm]
        else:
            return False

    def get_titles(self):
        return self.a_title

    def get_commands_list(self):
        return self.commands_list

    def add_animal(self, nickname, birthday, title):
        try:
            with connect(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port) as connection:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO animals (nickname, birthday, parent_id) \
                           VALUES (%s, %s, (select id from animals_title where name=%s)) "
                    val = (nickname, birthday, title)
                    cursor.execute(sql, val)
                    connection.commit()
                    new_id = cursor.lastrowid
        except Error as e:
            raise(e)

        init_class = self.class_list.get(title)
        self.records.append(eval(init_class)(new_id, nickname, birthday, []))

    def add_command(self, id, comm):
        try:
            with connect(user=self.user, password=self.password, host=self.host, database=self.database, port=self.port) as connection:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO animals_commands (animals_id, commands_id) \
                           VALUES (%s, %s); "
                    val = (id, comm)
                    cursor.execute(sql, val)
                    connection.commit()
        except Error as e:
            raise(e)

        self.get_animal(id)[0].add_command(comm)


