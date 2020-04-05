class Fruit:
    def __init__(self, fruit_type, height, weight):
        self.fruit_type = fruit_type
        self.height = height
        self.weight = weight

    def get_fruit_type(self):
        return self.fruit_type

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight


# "fruit": [inches, pounds]
fruits = {
    "apples": [2.964, 0.331],
    "bananas": [7.201, 0.202],
    "blueberries": [0.603, 0.0011],
    "cantaloupes": [6.535, 3.034],
    "cherries": [0.812, 0.001],
    "coconuts": [6.515, 3.213],
    "cranberries": [0.628, 0.0012],
    "cucumbers": [6.642, 0.443],
    "eggplants": [8.194, 2.256],
    "elongated muskmelons": [6.172, 2.936],
    "grapes": [0.893, 0.0015],
    "grapefruits": [3.774, 0.519],
    "honeydew melons": [6.362, 3.155],
    "kiwis": [2.261, 0.168],
    "lemons": [2.673, 0.219],
    "limes": [2.562, 0.312],
    "mangoes": [5.153, 1.131],
    "oranges": [2.789, 0.212],
    "papayas": [7.413, 1.256],
    "peaches": [2.688, 0.298],
    "pears": [3.352, 0.434],
    "pineapples": [10.516, 2.532],
    "plums": [2.341, 0.276],
    "pomegranates": [4.234, 0.935],
    "raspberries": [0.823, 0.0019],
    "strawberries": [1.215, 0.026],
    "tomatoes": [1.181, 0.044],
    "watermelons": [9.30, 18.69],
}


def get_height_in_fruits(person, fruit):
    return person.get_height()/fruit.get_height()

def get_weight_in_fruits(person, fruit):
    return person.get_weight()/fruit.get_weight()

def input_height():
    print("\nWhat's your height?\nI am ___ ft and ___ in")
    ft = float(input("ft: "))
    inch = float(input("in: "))
    if (ft <= 0 or inch < 0 or inch >= 12):
        raise ValueError("invalid height")
    height = ft * 12 + inch
    return height

def input_weight():
    print("\nWhat's your weight?\nI am ___ lb")
    weight = float(input("lb: "))
    if (weight <= 0):
        raise ValueError("invalid weight")
    return weight

def input_fruit_type():
    fruit_type = input("\nChoose your fruit:\n").lower()
    if (not fruits[fruit_type]):
        raise ValueError("invalid fruit")
    return fruit_type


def main():
    print("\nWelcome to the Fruit Meter!")
    print("Are you frustrated with having to convert your weight every time your English friend asks you for your weight in kilos?")
    print("Don't you fret! Just tell them how many bananas you weigh instead, they'll know right away!")

    while True:
        try:
            height = input_height()
            break
        except:
            print("\nInvalid height! Try again!")

    while True:
        try:
            weight = input_weight()
            break
        except:
            print("\nInvalid weight! Try again!")
    
    person = Person(height, weight)

    print("\n~~~Fruit Choices:~~~")
    fruit_display = "| "
    for fruit in fruits:
        fruit_display += fruit + " | "
    print(fruit_display)

    while True:
        try:
            fruit_type = input_fruit_type()
            break
        except:
            print("\ninvalid fruit! Try again!")

    fruit = Fruit(fruit_type, fruits[fruit_type][0], fruits[fruit_type][1])

    print("\nYour height:\t" + str(round(get_height_in_fruits(person, fruit), 2)) + "\t" + fruit_type + "!\n"
              + "Your weight:\t" + str(round(get_weight_in_fruits(person, fruit), 2)) + "\t" + fruit_type + "!\n")

if __name__ == '__main__':
    main()