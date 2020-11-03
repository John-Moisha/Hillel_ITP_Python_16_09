# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики [Написать атрибуты]:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 10)
# ловкость    (int от 1 до 10. Начальное значение 10)
# интелект    (int от 1 до 10. Начальное значение 10)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100). [Написать метод]
#
# Есть три типа юнитов - маги, лучники и рыцари. [Написать атрибуты]
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Только маг может увеличить интелект на 1 пункт, максимум 10. [Написать метод]
# Только лучник может увеличить ловкость на 1 пункт, максимум 10. [Написать метод]
# Только рыцарь может увеличить силу на 1 пункт, максимум 10. [Написать метод]
#
# Создать классы Mage, Archer, Knight, Unit.
# Причем Unit сделать родительским классом.
from random import randint, choice

class Unit:
    def init(self, name: str, clan: str, health: int = 100, power: int = 10, agility: int = 10, intelligence: int = 10):
        self.name = name
        self.clan = clan
        self.health = health
        self.power = power
        self.agility = agility
        self.intelligence = intelligence

    def _health(self):
        self.health = randint(1,100)
        return self.health
    def _power(self):
        self.power = randint(1,10)
        return self.power
    def _agility(self):
        self.agility = randint(1,10)
        return self.agility
    def _intelligence(self):
        self.intelligence = randint(1,10)
        return self.intelligence

    def healthing(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        return self.health

##### Маг
class Mage(Unit):

    @staticmethod
    def _choice_feature():
        feature = choice(['Воздух', 'Огонь', 'Вода'])
        return feature

    def __init__(self, name, clan, feature=None):
        super().init(name, clan)
        self.health = self._health()
        self.power = self._power()
        self.agility = self._agility()
        self.intelligence = self._intelligence()
        self.feature = feature
        if not self.feature:
            self.feature = self._choice_feature()


    def intelligence_up(self):
        if self.intelligence <= 9:
            self.intelligence += 1
        else:
            self.intelligence = 10
        return self.intelligence


#### Лучник
class Archer(Unit):

    @staticmethod
    def _choice_feature():
        feature = choice(['Лук', 'Арбалет'])
        return feature

    def __init__(self, name, clan, feature=None):
        super().init(name, clan)
        self.health = self._health()
        self.power = self._power()
        self.agility = self._agility()
        self.intelligence = self._intelligence()
        self.feature = feature
        if not self.feature:
            self.feature = self._choice_feature()


    def agility_up(self):
        if self.agility <= 9:
            self.agility += 1
        else:
            self.agility = 10
        return self.agility

#Рыцарь
class Knight(Unit):

    @staticmethod
    def _choice_feature():
        feature = choice(['Мечь', 'Топор', 'Пика'])
        return feature

    def __init__(self, name, clan, feature=None):
        super().init(name, clan)
        self.health = self._health()
        self.power = self._power()
        self.agility = self._agility()
        self.intelligence = self._intelligence()
        self.feature = feature
        if not self.feature:
            self.feature = self._choice_feature()


    def power_up(self):
        if self.power <= 9:
            self.power += 1
        else:
            self.power = 10
        return self.power


mage = Mage('Маг', 'Клан М')
archer = Archer('Лучник', 'Клан Л')
knight = Knight('Рыцарь', 'Клан р')

print(f'\t\tМаг\n'
      f'Имя:\t\t {mage.name}\n'
      f'Клан:\t\t {mage.clan}\n'
      f'Здоровье:\t {mage.health}\n'
      f'Выличился:\t {mage.healthing()}\n'
      f'Тип Магии:\t {mage.feature}\n'
      f'Сила:\t\t {mage.power}\n'
      f'Ловкость:\t {mage.agility}\n'
      f'Интелект:\t {mage.intelligence}\n'
      f'Интелект UP: {mage.intelligence_up()}\n')

print(f'\t\tЛучник\n'
      f'Имя:\t\t {archer.name}\n'
      f'Клан:\t\t {archer.clan}\n'
      f'Здоровье:\t {archer.health}\n'
      f'Выличился: \t {archer.healthing()}\n'
      f'Тип Магии:\t {archer.feature}\n'
      f'Сила:\t\t {archer.power}\n'
      f'Ловкость:\t {archer.agility}\n'
      f'Ловкость UP: {archer.agility_up()}\n'
      f'Интелект:\t {archer.intelligence}\n')

print(f'\t\tРыцарь\n'
      f'Имя:\t\t {knight.name}\n'
      f'Клан:\t\t {knight.clan}\n'
      f'Здоровье:\t {knight.health}\n'
      f'Выличился:\t {knight.healthing()}\n'
      f'Тип Магии:\t {knight.feature}\n'
      f'Сила:\t\t {knight.power}\n'
      f'Сила UP:\t {knight.power_up()}\n'
      f'Ловкость:\t {knight.agility}\n'
      f'Интелект:\t {knight.intelligence}\n')