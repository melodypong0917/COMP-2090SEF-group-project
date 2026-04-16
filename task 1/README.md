topic: inventory system

Introduction video: https://youtu.be/HqFHqPwTV1o?si=ByLkH4iN7eUe1aUG

Inventory System User Guide
1. Install the all files
2. Open all the files using VS code
3. Run the main.py

There will be 7 actions to be chosen, you can choose the action by entering the according number.
For the actions, you can choose to
1. Add New Item (Standard/Catergorized)
    - Input the name, quantity (in integer) and price (in numbers) of the item
    - Choose the type of the item
        1. Standard: There will be no tag to search
        2. Catergorized: There will be tag to search
            ~ Please enter the catergory name

2. Restock Existing Item
    - Input the name, amount (in integer) and price (in numbers) of the item
    - Choose the type of the item
        1. Standard: There will be no tag to search
        2. Catergorized: There will be tag to search
            ~ Please enter the catergory name

3. Withdraw Stock
    - Input the name and amount (in integer) of the item

4. View all Items
    You can see a report of the inventory in the system with their name, quantity, price, catergory, and latest updated time.

5. Search Items
    - Input the item that you want to search
        *You can enter the catergory of the item if you input it with catergory*
    The results with the keyword will be diplayed

6. View Transaction History
    You can see all the history no matter it is successful or fail done in the system.
    All the related inforamtion will be shown, such as the time that the actions is made.

7. Exit
    The system will be closed and all the actions made will be saved.
    You can continue to used the data when you open the system again.
    A JSON file will be saved to the file.