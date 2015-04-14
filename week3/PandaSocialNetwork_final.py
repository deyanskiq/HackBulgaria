import json


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
        self.checked = False

    def __str__(self):
        return "Hello, I'm {} my email is {} and I'm {} ".format(self.name, self.email, self.gender)

    def __eq__(self, other):
        var1 = (self.name == other.name)
        var2 = (self.email == other.email)
        var3 = (self.gender == other.gender)
        return var1 and var2 and var3

    def __hash__(self):
        return hash(self.__str__())

    def isMale(self):
        return self.gender.lower() == "male"

    def isFemale(self):
        return self.gender.lower() == "female"

    def getName(self):
        return self.name
daido = Panda("Daido", "deyanskiq@abv.bg", "male")
print(daido.getName())


class PandaSocialNetwork:

    def __init__(self):

        self.network = {}

    def has_panda(self, panda):
        return panda in self.network

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise Exception("PandaAlreadyThere")
        else:

            self.network[panda] = []

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("Panda are already friends")
        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def friends_of(self, panda):
        return self.network[panda]

    def __panda_connections(self, panda):  # bfs
        connections = {}
        q = []
        visited = set()
        q.append((0, panda))
        visited.add(panda)
        while len(q) != 0:
            panda_data = q.pop(0)
            current_level = panda_data[0]
            current_node = panda_data[1]
            connections[current_node] = current_level
            for neighbour in self.network[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append((current_level + 1, neighbour))
        return connections

    def connection_level(self, panda1, panda2):
        panda_table = self.__panda_connections(panda1)
        if panda2 not in panda_table:
            return -1
        return panda_table[panda2]

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) >= 1:
            return True
        return False

    def genders_in_network(self, level, gender, panda):
        panda_table = self.__panda_connections(panda)
        counter = 0
        for panda in panda_table:
            p_level = panda_table[panda]
            if p_level != 0 and p_level <= level and panda.gender() == gender:
                counter += 1
        return counter

    def __repr__(self, filename):
        for_save = {}
        for panda in self.network:
            friends = [repr(panda_friend)
                       for panda_friend in self.network[panda]]
            for_save[repr(panda)] = friends
        return for_save

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.__repr__(), indent=True))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            json_network = json.loads(contents)
            network = PandaSocialNetwork()
            for panda in json_network:
                for friends in json_network[panda]:
                    p1 = eval(panda)
                    p2 = eval(friends)
                    if not network.are_friends(p1, p2):
                        network.make_friends(p1, p2)
        return network

network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")
sonic = Panda("Sonic", "Sonic@pandamail.com", "male")
kimo = Panda("Kimono", "kimo@pandamail.com", "female")
for panda in [ivo, rado]:
    network.add_panda(panda)
network.make_friends(tony, rado)
network.make_friends(ivo, tony)
network.make_friends(kimo, ivo)
print(network.connection_level(ivo, rado))
print(network.are_connected(ivo, daido))
print(network.connection_level(kimo, rado))
print(Panda.isMale(daido))
