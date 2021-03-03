# Задание 3

# Создать программу для работы с объектами класса в соответствии с вариантом.
# Реализовать:
# конструктор
# перегрузить оператор присваивания;
# перегрузить операции отношений (<, >, !=, ==);

# Составить демонстрационную программу в виде отдельного модуля, для этого:
# создать две скалярные переменные;
# создать массив из 5 элементов;
# показать работу конструкторов,
# показать работу перечисленных функций и операторов;
# использовать для демонстрации все перечисленные выше объекты.

class Address:
    def __init__(self, index, city, street, house_num, flat_num):
            self.index = index
            self.city = city
            self.street = street
            self.house_num = house_num
            self.flat_num = flat_num

    def __str__(self):
        return ("Индекс: " + str(self.index) + "\nГород: " + str(self.city) + "\nУлица: " + str(self.street) +
                "\nНомер дома: " + str(self.house_num) + "\nНомер квартиры: " + str(self.flat_num) + "\n")

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_street(self, street):
        self.street = street

    def get_street(self):
        return self.street

    def set_house_num(self, house_num):
        self.house_num = house_num

    def get_house_num(self):
        return self.house_num

    def set_flat_num(self, flat_num):
        self.flat_num = flat_num

    def get_flat_num(self):
        return self.flat_num

    def __eq__(self, other):
        if self.index == other.index and self.city == other.city:
            if self.street == other.street:
                if self.house_num == other.house_num:
                    if self.flat_num == other.flat_num:
                        return "Ольга и Иван живут в одной квратире\n"
                    else:
                        return "Ольга и Иван живут в одном доме\n"
                else:
                    return "Ольга и Иван живут на одной улице\n"
            else:
                return "Ольга и Иван живут в одном городе\n"
        else:
            return "Ольга и Иван живут в разных городах\n"

    def __gt__(self, other):
        if self.house_num > other.house_num:
            return "Номер дома Ольги больше номера квартиры Ивана"
        else:
            return "Номер дома Ольги меньше номера квартиры Ивана"

    def __lt__(self, other):
        if self.flat_num < other.flat_num:
            return "Номер квартиры Ольги меньше номера квартиры Ивана"
        else:
            return "Номер квартиры Ольги больше номера квартиры Ивана"


Olga_address = Address(400019, "Volgograd", "Krepilnaya", 128, 4)
Ivan_address = Address(400019, "Volgograd", "Krepilnaya", 18, 34)

print(Olga_address)
print(Ivan_address)
print(Olga_address == Ivan_address)

Olga_address.set_street("Mira")
print(Olga_address)
print(Ivan_address)
print((Olga_address == Ivan_address))
print(Olga_address > Ivan_address)
print(Olga_address < Ivan_address)

