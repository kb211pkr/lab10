from classLAB import Shop, Discount
import pytest

store1 = Shop("Products", "магазин фермерської продукції")
store_discount  = Discount()

def test_describe_shop(capfd):
    store1.describe_shop()
    out, err = capfd.readouterr()
    assert out == "\nМагазин 'Products' - це магазин фермерської продукції\n"

def test_set_number_of_units(capfd):
    if store1.set_number_of_units(10):
     assert store1.number_of_units == 10
    else:
        store1.set_number_of_units(-1)
        out, err = capfd.readouterr()
        assert out == "Недопустиме значення\n"

def test_increment_number_of_units(capfd):
    store1.increment_number_of_units(10)
    assert store1.number_of_units == 20
    out, err = capfd.readouterr()
    assert out == "Постачання нового товару...\n"

def test_open_shop(capfd):
  store1.open_shop()
  out, err = capfd.readouterr()
  assert out == "\n-------- Зачинено --------\n"

def test_add(capfd):
    store_discount.add("Сукня", "Джинси")
    out, err = capfd.readouterr()
    assert out == "Додаємо акціні товари...\n"

def test_get_discounts_ptoducts(capfd):
    store_discount.get_discounts_ptoducts()
    out, err = capfd.readouterr()
    assert out == "Акційні товари: Сукня Джинси\n"

