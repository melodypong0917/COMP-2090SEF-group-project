from abc import ABC
from datetime import datetime

class StockError(Exception):
    pass

class InventoryItem(ABC):
    total_items_created = 0

    def __init__(self, name: str, quantity: int, base_price: float):
        self._name = name
        self._quantity = quantity
        self._base_price = base_price
        self._last_updated = datetime.now()
        InventoryItem.total_items_created += 1

    def get_name(self) -> str:
        return self._name
    
    def get_quantity(self) -> int:
        return self._quantity
    
    def get_base_price(self) -> float:
        return self._base_price

    def set_quantity(self, value: int):
        if value < 0:
            raise StockError(f"Quantity for {self.get_name()} cannot be negative.")
        self._quantity = value
        self._last_updated = datetime.now()

    def get_last_updated_str(self) -> str:
        return self._last_updated.strftime("%Y-%m-%d %H:%M:%S")

    name = property(fget=get_name)
    quantity = property(fget=get_quantity, fset=set_quantity)
    base_price = property(fget=get_base_price)
    last_updated_str = property(fget=get_last_updated_str)

    def display_info(self) -> str:
        raise NotImplementedError("Subclasses must implement display_info()")

    def calculate_value(self) -> float:
        raise NotImplementedError("Subclasses must implement calculate_value()")

    def add_stock(self, amount: int):
        if amount <= 0:
            raise StockError("Amount to add must be positive.")
        self.set_quantity(self.get_quantity() + amount)

    def remove_stock(self, amount: int):
        if amount <= 0:
            raise StockError("Amount to remove must be positive.")
        if amount > self.get_quantity():
            raise StockError(f"Insufficient stock for {self.get_name()}.")
        self.set_quantity(self.get_quantity() - amount)

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.get_name()}', qty={self.get_quantity()})"

    def __eq__(self, other):
        if not isinstance(other, InventoryItem):
            return False
        return self.get_name().lower() == other.get_name().lower()


class StockItem(InventoryItem):
    def display_info(self) -> str:
        return f"Item: {self.get_name():<15} | Qty: {self.get_quantity():<5} | Price: ${self.get_base_price():<7.2f} | Updated: {self.get_last_updated_str()}"

    def calculate_value(self) -> float:
        return self.get_quantity() * self.get_base_price()


class CategorizedStockItem(StockItem):
    def __init__(self, name: str, quantity: int, base_price: float, category: str):
        super().__init__(name, quantity, base_price)
        self._category = category

    def get_category(self) -> str:
        return self._category
    
    category = property(fget=get_category)

    def display_info(self) -> str:
        base_info = super().display_info()
        return f"[{self.get_category()}] {base_info}"

class Transaction:
    def __init__(self, item_name: str, action: str, amount: int, status: str = "SUCCESS"):
        self.item_name = item_name
        self.action = action
        self.amount = amount
        self.status = status
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] {self.status:<8} | {self.action:<12}: {self.item_name} (Amt: {self.amount})"
