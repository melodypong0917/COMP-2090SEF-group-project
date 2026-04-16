import json
import os
from models import (
    StockItem, CategorizedStockItem,
    Transaction, InventoryItem, StockError
)
from typing import Dict, List

class InventoryManager:
    
    def __init__(self, file_name: str = "inventory.json"):
        self._items: Dict[str, InventoryItem] = {}
        self._history: List[Transaction] = []
        self._file_name = file_name
        self._load_from_file()

    def add_new_item(self, item: InventoryItem):
        item_name = item.get_name()
        if item_name in self._items:
            raise StockError(f"Item '{item_name}' already exists.")
        
        self._items[item_name] = item
        self._log_transaction(item_name, "New Item", item.get_quantity())
        self._save_to_file()

    def update_stock(self, name: str, amount: int, action: str = "add"):
        if name not in self._items:
            raise StockError(f"Item '{name}' not found.")
        
        item = self._items[name]
        try:
            if action == "add":
                item.add_stock(amount)
                self._log_transaction(name, "Restock", amount)
            elif action == "remove":
                item.remove_stock(amount)
                self._log_transaction(name, "Withdrawal", amount)
            self._save_to_file()
        except StockError as e:
            self._log_transaction(name, f"Failed {action}", amount, status="FAILED")
            raise e

    def _log_transaction(self, name: str, action: str, amount: int, status: str = "SUCCESS"):
        self._history.append(Transaction(name, action, amount, status))

    def search_items(self, query: str) -> List[str]:
        results = [
            item.display_info() for name, item in self._items.items() 
            if query.lower() in name.lower()
        ]
        return results

    def get_all_reports(self) -> List[str]:
        return [item.display_info() for item in self._items.values()]

    def get_inventory_value(self) -> float:
        return sum(item.calculate_value() for item in self._items.values())

    def get_history(self) -> List[str]:
        return [str(tx) for tx in self._history]

    def _save_to_file(self):
        data = {
            "items": [
                {
                    "name": item.get_name(),
                    "type": type(item).__name__,
                    "quantity": item.get_quantity(),
                    "base_price": item.get_base_price(),
                    "category": getattr(item, "_category", "")
                }
                for item in self._items.values()
            ]
        }
        with open(self._file_name, "w") as f:
            json.dump(data, f, indent=4)

    def _load_from_file(self):
        if not os.path.exists(self._file_name):
            return
            
        try:
            with open(self._file_name, "r") as f:
                data = json.load(f)
                for item_data in data.get("items", []):
                    name = item_data["name"]
                    itype = item_data["type"]
                    qty = item_data["quantity"]
                    price = item_data["base_price"]
                    cat = item_data["category"]
                    
                    if itype == "CategorizedStockItem":
                        item = CategorizedStockItem(name, qty, price, cat)
                    else:
                        item = StockItem(name, qty, price)
                    self._items[name] = item
        except (json.JSONDecodeError, KeyError):
            pass
