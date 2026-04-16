import sys

sys.dont_write_bytecode = True

from inventory import InventoryManager
from models import StockItem, CategorizedStockItem, StockError, InventoryItem

class StockCLI:
    
    def __init__(self):
        self.inventory = InventoryManager()

    def display_header(self):
        print(f" Inventory System (Types: {InventoryItem.total_items_created}) ")

    def display_menu(self):
        self.display_header()
        print(" 1. Add New Item (Standard/Categorized)")
        print(" 2. Restock Existing Item")
        print(" 3. Withdraw Stock")
        print(" 4. View All Items")
        print(" 5. Search Items")
        print(" 6. View Transaction History")
        print(" 7. Exit")   
        print("-" * 60)
        return input("Select an option (1-7): ").strip() 

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == "1":
                self._process_new_item()
            elif choice == "2":
                self._process_update("add")
            elif choice == "3":
                self._process_update("remove")
            elif choice == "4":
                self._show_list("FULL INVENTORY REPORT", self.inventory.get_all_reports())
            elif choice == "5":
                self._process_search()
            elif choice == "6":
                self._show_list("TRANSACTION LOG", self.inventory.get_history())
            elif choice == "7":
                print("\nData saved")
                sys.exit(0)
            else:
                print("\n[Error] Invalid choice. Please select 1-7.")

    def _process_new_item(self):
        print("\n--- ADD NEW ITEM ---")
        name = input("Name: ").strip()
        try:
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            
            print("Type: 1. Standard  2. Categorized ")
            type_choice = input("Select type (1-2): ")
            
            if type_choice == "2":
                cat = input("Category: ")
                item = CategorizedStockItem(name, qty, price, cat)
            else:
                item = StockItem(name, qty, price)
            
            self.inventory.add_new_item(item)
            print(f"\n[Result] {item.get_name()} added to inventory.")
        except (ValueError, StockError) as e:
            print(f"\n[Error] {e}")

    def _process_update(self, action):
        title = "RESTOCK" if action == "add" else "WITHDRAWAL"
        print(f"\n--- {title} ---")
        name = input("Item name: ").strip()
        try:
            amt = int(input("Amount: "))
            self.inventory.update_stock(name, amt, action)
            print(f"\n[Result] Stock updated for {name}.")
        except (ValueError, StockError) as e:
            print(f"\n[Error] {e}")

    def _process_search(self):
        query = input("\nEnter search term: ").strip()
        results = self.inventory.search_items(query)
        self._show_list(f"SEARCH RESULTS: '{query}'", results)

    def _show_list(self, title, items):
        print(f"\n--- {title} ---")
        if not items:
            print("No records found.")
        else:
            for item in items:
                print(item)

def main():
    try:
        app = StockCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
