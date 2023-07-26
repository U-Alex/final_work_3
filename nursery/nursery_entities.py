
class Animals:
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        self.id = id
        self.nickname = nickname
        self.birthday = birthday
        self.comm_list = comm_list

    def get_comm_list(self):
        return self.comm_list

    def add_command(self, comm_id):
        self.comm_list.append(comm_id)

    def get_id(self):
        return self.id

    def is_knows(self, comm_id):
        return comm_id in self.comm_list


class Animals_homemade(Animals):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        return 'домашние животные'
    
class Animals_pack(Animals):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)
        
    def __str__(self) -> str:
        return 'вьючные животные'


class Animal_dog(Animals_homemade):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | собаки ({super().__str__()}) "

class Animal_cat(Animals_homemade):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | кошки ({super().__str__()}) "

class Animal_hamster(Animals_homemade):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | хомяки ({super().__str__()}) "

class Animal_horse(Animals_pack):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | лошади ({super().__str__()}) "

class Animal_camel(Animals_pack):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | верблюды ({super().__str__()}) "

class Animal_donkey(Animals_pack):
    def __init__(self, id, nickname, birthday, comm_list) -> None:
        super().__init__(id, nickname, birthday, comm_list)

    def __str__(self) -> str:
        birth = self.birthday.strftime("%d-%m-%Y")
        return f"id: {self.id}\t {self.nickname}   | д.р: {birth} | ослы ({super().__str__()}) "





