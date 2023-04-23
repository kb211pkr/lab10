import random
import datetime


class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"\nМагазин '{self.shop_name}' - це {self.store_type}")

    def set_number_of_units(self, number_of_units):
        if number_of_units > 0:
            self.number_of_units = number_of_units
        else:
            print("Недопустиме значення")

    def increment_number_of_units(self, amount):
        print("Постачання нового товару...")
        self.number_of_units += amount

    def open_shop(self):
        def time_in_range(start, end, current):
            return start <= current <= end

        start = datetime.time(8, 0, 0)
        end = datetime.time(20, 0, 0)
        current = datetime.datetime.now().time()
        if (time_in_range(start, end, current) == True):
            print("\n-------- Відчинено --------")
        else:
            print("\n-------- Зачинено --------")


class Discount(Shop):
    def __init__(self):
        self.discount_products = []

    def add(self, *a):
        print("Додаємо акціні товари...")
        self.discount_products.extend(a)

    def get_discounts_ptoducts(self):
        print(f"Акційні товари:", *(self.discount_products))
        return self.discount_products


# ------------------------------------------------------------- task9 -----------------------------------------------------------------

class User:
    login_attempts = 0

    def __init__(self, first_name="", last_name="", email="", nickname="", agreement=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.agreement = agreement

    def describe_user(self):
        print("\nКористувач:", self.last_name, self.first_name)

    def printInfo(self):
        print(f"\nІм'я: {self.first_name}\nПрізвище: {self.last_name}\nEmail: {self.email}\nНік: {self.nickname}")

    def greeting_user(self):
        print("Вітаємо,", self.first_name, self.last_name)

    @staticmethod
    def increment_login_attempts():
        print("Здійснюється вхід в аккаунт...")
        User.login_attempts += 1

    @staticmethod
    def reset_login_attempts():
        print("Обнуляємо спроби входу...")
        User.login_attempts = 0


class Privileges():
    privileges = []

    def __init__(self, admin):
        self.privileges = list(admin.privileges)

    def add(self, *a):
        self.privileges.extend(a)

    def show_privileges(self):
        print(f"Привілеї:", ',\n'.join(self.privileges))


class Admin(User):
    privileges = []

    def __init__(self, first_name="", last_name="", email="", nickname="", agreement=True):
        self.priv = Privileges(self)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.agreement = agreement


def add(firstNumber, secondNumber):
    return firstNumber + secondNumber


def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber