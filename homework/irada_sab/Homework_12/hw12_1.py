# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (по среднему времени жизни - и это тоже метод).


class Flower:
    def __init__(self, name, color, freshness, stem_length, price, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan

    def __str__(self):
        return (f"{self.name} ({self.color}), freshness: {self.freshness}, stem length: "
                f"{self.stem_length}, price: ${self.price}, lifespan: {self.lifespan} days.")


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Rose", color, freshness, stem_length, price, 7)


class Daisy(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Daisy", color, freshness, stem_length, price, 5)


class Lilac(Flower):
    def __init__(self, color, freshness, stem_length, price):
        super().__init__("Lilac", color, freshness, stem_length, price, 10)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_flowers(self, flowers_list):
        self.flowers.extend(flowers_list)

    def calculate_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def calculate_wilting_time(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_by_price(self):
        self.flowers.sort(key=lambda x: x.price, reverse=True)

    def find_by_lifespan(self, min_lifespan, max_lifespan):
        return [flower for flower in self.flowers if min_lifespan <= flower.lifespan <= max_lifespan]

    def find_by_color(self, color):
        return [flower for flower in self.flowers if flower.color.lower() == color.lower()]

    def find_by_freshness(self, min_freshness):
        return [flower for flower in self.flowers if flower.freshness >= min_freshness]

    def __str__(self):
        if not self.flowers:
            return "Empty bouquet"

        result = f"Bouquet (price: ${self.calculate_total_price()}):\n"
        for i, flower in enumerate(self.flowers, 1):
            result += f"{i}. {flower}\n"
        result += f"Fade time: {self.calculate_wilting_time():.1f} days"
        return result


rose_red = Rose("red", 7, 40, 15)
rose_white = Rose("white", 8, 35, 12)
daisy_yellow = Daisy("yellow", 10, 30, 5)
daisy_pink = Daisy("pink", 9, 25, 4)
lilac_white = Lilac("white", 9, 45, 10)
lilac_purple = Lilac("purple", 10, 40, 13)

bouquet = Bouquet()
bouquet.add_flowers([rose_red, rose_white, daisy_pink, daisy_yellow, lilac_white, lilac_purple])

print(bouquet)
print()

print('Sort by freshness')
bouquet.sort_by_freshness()
print(bouquet)
print()

print('Sort by color')
bouquet.sort_by_color()
print(bouquet)
print()

print('Sort by stem length')
bouquet.sort_by_stem_length()
print((bouquet))
print()

print('Sort by price')
bouquet.sort_by_price()
print(bouquet)
print()


print('Finding flowers by 6-8 days length')
long_living_flowers = bouquet.find_by_lifespan(6, 8)
for flower in long_living_flowers:
    print(f"- {flower}")

print('\n Finding white flowers')
white_flowers = bouquet.find_by_color("white")
for flower in white_flowers:
    print(f"- {flower}")

print('\n Finding flowers by freshness not less than 9 days')
fresh_flowers = bouquet.find_by_freshness(9)
for flower in fresh_flowers:
    print(f"- {flower}")
