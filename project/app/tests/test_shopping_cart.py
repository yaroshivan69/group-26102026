import pytest
from app.utils.shopping_cart import ShoppingCart


class TestShoppingCart:
    def setup_method(self):
        self.cart = ShoppingCart()

    def test_init_empty_cart(self):
        assert self.cart.items == []

    def test_add_new_item(self):
        self.cart.add_item("Apple", 10.5, 3)

        assert len(self.cart.items) == 1
        assert self.cart.items[0] == {
            "name": "Apple",
            "price": 10.5,
            "quantity": 3
        }

    def test_add_existing_item_updates_quantity_and_price(self):
        self.cart.add_item("Apple", 10.5, 3)
        self.cart.add_item("Apple", 12.0, 2)

        assert len(self.cart.items) == 1
        assert self.cart.items[0] == {
            "name": "Apple",
            "price": 12.0,
            "quantity": 5
        }

    def test_add_multiple_different_items(self):
        self.cart.add_item("Apple", 10.0, 2)
        self.cart.add_item("Banana", 15.0, 4)

        assert len(self.cart.items) == 2

    def test_remove_existing_item(self):
        self.cart.add_item("Apple", 10.0, 2)
        self.cart.add_item("Banana", 15.0, 4)

        self.cart.remove_item("Apple")

        assert len(self.cart.items) == 1
        assert self.cart.items[0]["name"] == "Banana"

    def test_remove_non_existing_item_does_nothing(self):
        self.cart.add_item("Apple", 10.0, 2)

        self.cart.remove_item("Orange")

        assert len(self.cart.items) == 1
        assert self.cart.items[0]["name"] == "Apple"