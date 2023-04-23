from classLAB import User, Privileges, Admin
import pytest

user = User("Karina", "Polishchuk", "karin@gmail.com", "rina")
admin = Admin("Admin", "", "admin@gmail.com", "Adm", True)


def test_describe_user(capfd):
    user.describe_user()
    out, err = capfd.readouterr()
    assert out == "\nКористувач: Polishchuk Karina\n"


def test_printInfo(capfd):
    user.printInfo()
    out, err = capfd.readouterr()
    assert out == "\nІм'я: Karina\nПрізвище: Polishchuk\nEmail: karin@gmail.com\nНік: rina\n"


def test_greeting_user(capfd):
    user.greeting_user()
    out, err = capfd.readouterr()
    assert out == "Вітаємо, Karina Polishchuk\n"


def test_increment_login_attempts(capfd):
    user.increment_login_attempts()
    out, err = capfd.readouterr()
    assert out == "Здійснюється вхід в аккаунт...\n"
    assert User.login_attempts == 1


def test_reset_login_attempts(capfd):
    user.reset_login_attempts()
    out, err = capfd.readouterr()
    assert out == "Обнуляємо спроби входу...\n"
    assert User.login_attempts == 0


def test_show_privileges(capfd):
    admin.priv.add("Allowed to add message", "Allowed to delete users", "Allowed to ban users")
    admin.priv.show_privileges()
    out, err = capfd.readouterr()
    assert out == "Привілеї: Allowed to add message,\nAllowed to delete users,\nAllowed to ban users\n"




