import random


class GeneralDescription():

    def __init__(self, health, mana):
        self.max_health = 100
        self.max_mana = mana  # 100
        self.health = health
        self.mana = mana
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health != 0

    def can_cast(self):
        if self.known_spell is True:
            if self.mana >= self.__spell.mana_cost:
                return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if(self.health + healing_points) > self.max_health:
            self.health = 100

        self.health += healing_points
        return True

    def take_mana(self, mana_points):
        if self.mana + mana_points > 100:
            self.mana = 100
        self.mana += mana_points

    def attack(self, by=""):
        if by == "weapon":
            if self.has_weapon is False:
                return 0
            else:
                return self.__weapon.damage
        elif by == "spell":
            if self.knows_spell is False:
                return 0
            else:
                return self.__weapon.damage
        else:
            raise Exception("Not a valid attack by")

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range


class Hero (GeneralDescription):

    def __init__(self, name="Didka", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2):
        super().__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__weapon = Weapon("", 0)
        self.spell = Spell("", 0, 0, 0)
        self.has_weapon = False
        self.known_spell = False

    def known_as(self):
        return "{0} the {1}".format(self.__name, self.__title)

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
            print(self.__weapon.name)

    def learn(self, spell):
        self.spell = spell
        print(self.spell.name)


class Enemy(GeneralDescription):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage

    def __str__(self):
        return "Health:{},mana: {}, damage: {}".format(self.health, self.mana, self.damage)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())


class Dungeons:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.dungeon = [list(line) for line in lines]
        self.row = 0
        self.col = 0
        self.treasure = {}
        self.dict_enemies = {}
        self.hero = None

    def cast_right(self, hero):
        self.hero = hero
        if self.hero.mana >= self.hero.spell.mana_cost:
            print(self.hero.spell.cast_range)
            for i in range(self.col, self.col + self.hero.spell.cast_range):
                if self.dungeon[self.row][i] == "E":
                    self.dict_enemies[
                        (self.row, i)].health -= self.hero.spell.damage
                    self.hero.mana -= self.hero.spell.mana_cost
                    break
                    if not self.dict_enemies[(self.row, i)].is_alive():
                        self.dungeon[self.row][i] = "."
                    else:
                        self.dict_enemies[
                            (self.row, i - 1)] = self.dict_enemies[(self.row, i)]
                        del self.dict_enemies[(self.row, i)]
        return

    def get_enemies(self):
        enemies_sequence = self.find_symbol("E")
        i = 0
        for x in enemies_sequence:
            self.dict_enemies[x] = enemy[i]
            i += 1
        return self.dict_enemies

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def spawn(self, hero_instance):
        if not isinstance(hero_instance, Hero):
            raise TypeError("The hero must be from class Hero")
        self.hero = hero_instance
        found = False
        for i in range(0, len(self.dungeon)):
            for j in range(0, len(self.dungeon[i])):
                if self.dungeon[i][j] == "S":
                    self.dungeon[i][j] = "H"
                    self.row = i
                    self.col = j
                    found = True
                    break
            if found:
                break
            return found

    def find_symbol(self, symbol):
        positions = []
        line_index = 0
        for line in self.dungeon:
            elem_index = 0
            for elem in line:
                if elem == symbol:
                    # return [(line_index, elem_index)]  # touple ot pozicii
                    positions.append((line_index, elem_index))
                elem_index += 1
            line_index += 1
        return positions

    def is_in_bound(self, positions):
        # positions = [row, col]
        count_row = len(self.dungeon)
        count_col = len(self.dungeon[0])
        return (positions[0] >= 0 and positions[0] < count_row)\
            and (positions[1] >= 0 and positions[1] < count_col)

    def return_what_found_while_moving(self, symbol):
        if symbol == 'G':
            return "You are the best ^_^ End of level!"

        if symbol == '.':
            return True
        if symbol == 'T':

            return "You found treasure"

        if symbol == 'E':
            # make fight
            return "Fight! Let the better win!"

    def make_move(self, old_positions, new_positions):
        new_row = new_positions[0]
        new_col = new_positions[1]
        old_row = old_positions[0]
        old_col = old_positions[1]
        if self.is_in_bound(new_positions):
            if self.dungeon[new_row][new_col] is not'#':
                to_return = self.return_what_found_while_moving(
                    self.dungeon[new_row][new_col])
                self.dungeon[old_row][old_col] = '.'
                self.dungeon[new_row][new_col] = 'H'
            else:
                return False
        else:
            return False

        self.row = new_row
        self.col = new_col
        return to_return

    def is_valid_move(self, directions):
        if directions == "up":
            return self.make_move([self.row, self.col], [self.row - 1, self.col])

        elif directions == "down":
            return self.make_move([self.row, self.col], [self.row + 1, self.col])

        elif directions == "left":
            return self.make_move([self.row, self.col], [self.row, self.col - 1])

        elif directions == "right":
            return self.make_move([self.row, self.col], [self.row, self.col + 1])

    def move_hero(self, directions):
        if directions in ["up", "down", "left", "right"]:
            return self.is_valid_move(directions)
            self.mana += self.mana_regeneration_rate
        else:
            print("Wrong input!")

    def pick_treasure(self):

        weapon_bonus = Weapon("Spike", 25)
        spell_bonus = Spell("Silver", 30, 7)
        mana_bonus = 6,
        health_potion_bonus = 10

        T = random.choice(
            [mana_bonus, health_potion_bonus, weapon_bonus, spell_bonus])
        if T == mana_bonus:
            self.hero.take_mana(mana_bonus)
        elif T == health_potion_bonus:
            self.hero.take_healing(health_potion_bonus)
        elif T == weapon_bonus:
            self.hero.equip(T)
        else:
            self.hero.learn(T)


didi = Hero()
didi.equip(Weapon("Asda", 50))
didi.learn(Spell("spell", 70, 5, 2))
a = Dungeons("map.txt")
a.print_map()
a.spawn(didi)
print("------------------------")
a.print_map()

hero = Hero()
print(hero.known_as())
# print(a.pick_treasure())
w = Weapon("Silver", 50)
print("---------------------------")
didi.equip(w)
enemy1 = Enemy(100, 30, 20)
enemy2 = Enemy(50, 30, 5)
enemy3 = Enemy(30, 10, 15)
enemy = [enemy1, enemy2, enemy3]
print(a.get_enemies())
a.move_hero("right")
a.move_hero("down")
a.move_hero("down")
a.move_hero("down")
a.cast_right(didi)
print("----------------------")
print(didi.mana)
a.print_map()
print("----------------------")
print(a.get_enemies())
