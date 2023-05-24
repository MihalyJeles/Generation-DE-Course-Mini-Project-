import orders_database_modul
import products_database_modul
import couriers_database_modul
import save_data_modul
import sys
import re
#-----------------------------Connection to DB funtions-----------------------------------------------------------------------------
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

current_connection = None

def get_connection():
    global current_connection
    if current_connection == None:
        current_connection = pymysql.connect(host=host_name, database=database_name,
                                             user=user_name, password=user_password)
    return current_connection

def close_connection():
    if current_connection != None:
        current_connection.close()
        print('Connection closed!')

#-------------------------------------------Colors-----------------------------------------------------------------------------

os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

#-------------------------------------General functions-----------------------------------------------------------------------------

# clear screen function
def Clear_screen():
    os.system('cls')

# press enter to continue
def press_to_continue():
    input('\nPress enter to continue!')

#-------------------------------------Input check functions-----------------------------------------------------------------------------

# input int expect funtion
def input_int_expect():
    while True:
        try:
            input_int = int(input('\nPlease enter a number from the available options: '))
            return input_int
        except (OverflowError,ValueError,NameError,IndexError):
            input_int = 1000
            return input_int
        
# input float expect funtion
def input_float_expect():
    while True:
        try:
            input_float = float(input('\nPlease enter the price: '))
            if input_float < 9999:
                return input_float
            else:
                print(COLOR["RED"],'Invalid value',COLOR["ENDC"])
        except (OverflowError,ValueError,NameError,IndexError):
            print(COLOR["RED"],'Invalid value',COLOR["ENDC"])

# input phone number length funtion
def input_phone_expect():
    while True:
        try:
            input_str = input("Please type in customer's phone number: ")
            if not re.match("^[0-9,+]*$", input_str):
                print(COLOR["RED"], "Error! Only numbers 0-9 and  '+' allowed!", COLOR["ENDC"])
            elif len(input_str) >= 11 and len(input_str) <= 13:
                return input_str
            else:
                print(COLOR["RED"], "Error! Only 11-13 characters allowed!", COLOR["ENDC"])
        except (OverflowError,ValueError,NameError,IndexError):
            print(COLOR["RED"], "Invalid value!", COLOR["ENDC"])

#-------------------------------------Main program-------------------------------------------------------------------------------
#---------------------------------------main menu--------------------------------------------------------------------------------
while True:
    Clear_screen()
    print('''
                                               ---WELCOM TO MY COFFEE SHOP!---
Main Menu Options:

1 - Products Menu
2 - Orders Menu
3 - Couriers Menu
0 - Exit the App

        ''')
    while True:
        x = input_int_expect()
        if x == 0:
            Clear_screen()
            products_list = products_database_modul.load_products_table(get_connection)
            couriers_list = couriers_database_modul.load_couriers_table(get_connection)
            orders_list = orders_database_modul.load_all_order_table(get_connection)
            save_data_modul.save_all_data(orders_list, couriers_list, products_list)
            close_connection()
            print("Exit App!") 
            sys.exit()

#-------------------------------------products menu----------------------------------------------------------------------------- 
    
        elif x == 1:
            while True:      
                Clear_screen()
                print('''
Product Menu:

1 - Products Menu          
2 - Creat/Add new Product      
3 - Update existing Product
4 - Delete Product         
0 - Return to Main Menu

                ''')
                product_user_input = input_int_expect()
                if product_user_input == 0: # 0-Return to Main Menu
                    Clear_screen()
                    break
                elif product_user_input == 1: # 1-Products Menu 
                    Clear_screen()
                    products_database_modul.print_products_table(get_connection)
                    press_to_continue()
                elif product_user_input == 2: # 2-Creat/Add new Product
                    Clear_screen()
                    print('Creat/Add new Product:\n')
                    new_product = input('\nPlease type in the new product: ')
                    price = input_float_expect()
                    products_database_modul.insert_product_to_db(new_product, price, get_connection)
                    press_to_continue()
                elif product_user_input == 3: # 3-Update existing Product
                    while True:
                        Clear_screen()
                        print('Update existing Product:\n')
                        products_database_modul.print_products_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = products_database_modul.ids_list(get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            name = input(f'Update name, please add the new value, or press enter: ')
                            price = input_float_expect()
                            products_database_modul.update_products_table(name, price, index_value, get_connection)
                            press_to_continue()
                            Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                elif product_user_input == 4: # 4-Delete Product 
                    while True:
                        Clear_screen()
                        print('Delete Product:\n')
                        products_database_modul.print_products_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = products_database_modul.ids_list(get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            products_database_modul.delete_product(index_value, get_connection)
                            press_to_continue()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                else:
                    Clear_screen()
                    print(COLOR["RED"],"Invalid number!Please choose from the available options!", COLOR["ENDC"])
                    press_to_continue()
                
#-------------------------------------orders menu-----------------------------------------------------------------------------       
        
        elif x == 2:
            while True:      
                Clear_screen()
                print('''
Orders Menu:

1 - Orders          
2 - New Order      
3 - Update Existing Order Status
4 - Update Existing Order
5 - Delete Order
6 - Orders list by Status/Courier      
0 - Return to Main Menu
            
            ''')
                order_user_input = input_int_expect()
                if order_user_input == 0: # 0-Return to Main Menu
                    Clear_screen()
                    break # exit from the inner while loop
                elif order_user_input == 1: # 1-Orders 
                    Clear_screen()
                    orders_database_modul.print_orders_table(get_connection)
                    press_to_continue()
                elif order_user_input == 2: # 2-New Order 
                    while True:
                        Clear_screen()
                        name = input("Please type in the customer's name: ")
                        address = input("Please type in customer's address: ")
                        phone_number = input_phone_expect()
                        press_to_continue()
                        # ------------------------- comma separated list----------------------------------
                        act_product_list = []
                        products_list = products_database_modul.load_products_table(get_connection)
                        while True:
                            Clear_screen()
                            products_database_modul.print_products_table(get_connection)
                            print('\n0 - Exit')
                            print('\n\nProducts in the basket:')
                            for number in act_product_list:
                                print(f'   {products_list[number-1]["name"]}, {products_list[number-1]["price"]}')
                            product_number = input_int_expect()
                            if product_number > 0 and product_number <= len(products_list):
                                act_product_list.append(product_number)
                            elif product_number == 0:
                                break
                            else:
                                print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                                press_to_continue()
                            act_product_list_string = [str(x) for x in act_product_list] # change the int list into a string list
                            comma_separated_string = ','.join(act_product_list_string) # turn the string list into a string
                        # ------------------------- comma separated list----------------------------------
                        while True:
                            Clear_screen()
                            couriers_database_modul.print_couriers_table(get_connection)
                            courier_index = input_int_expect()
                            ids_list = couriers_database_modul.ids_list(get_connection)
                            Clear_screen()
                            if courier_index in ids_list:
                                orders_database_modul.insert_new_order(name, address, phone_number, courier_index, comma_separated_string, get_connection)
                                press_to_continue()
                                Clear_screen()
                                break
                            else:
                                print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                                press_to_continue()
                        break
                elif order_user_input == 3: # 3-Update Existing Order Status
                    while True:
                        Clear_screen()
                        orders_database_modul.print_orders_table(get_connection)
                        order_number = input_int_expect()
                        ids_list = orders_database_modul.ids_list(get_connection)
                        if order_number in ids_list:
                            while True:
                                orders_database_modul.print_orderstatus_table(get_connection)
                                new_status_index = input_int_expect()
                                status_ids_list = orders_database_modul.status_ids_list(get_connection)
                                if new_status_index in status_ids_list:
                                    orders_database_modul.update_order_status(new_status_index, order_number, get_connection)
                                    press_to_continue()
                                    Clear_screen()
                                    break
                                else:
                                    print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                                    press_to_continue()
                                    Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                elif order_user_input == 4: # 4-Update Existing Order
                    while True: 
                        Clear_screen()
                        orders_database_modul.print_orders_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = orders_database_modul.ids_list(get_connection)
                        order_dic = orders_database_modul.load_order_table(index_value, get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            for key in order_dic.keys():
                                word = input(f'Update {key} please add the new value, or press enter: ')
                                if word == '':
                                    print('')
                                else:
                                    order_dic[key] = word
                                    print(f'{key} is Updated to {word}\n')
                            orders_database_modul.update_order_table(order_dic, index_value, get_connection)
                            press_to_continue()
                            Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                elif order_user_input == 5: # 5-Delete Order
                    while True: 
                        Clear_screen()
                        print('Delete an Order:\n')
                        orders_database_modul.print_orders_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = orders_database_modul.ids_list(get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            orders_database_modul.delete_order(index_value,get_connection)
                            press_to_continue()
                            Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                elif order_user_input == 6: # 6 list the orders by status
                    while True: 
                        Clear_screen()
                        print('''
1 - Orders list by Status
2 - Orders list by Courier      
0 - Return to Orders Menu
                        ''')
                        list_user_input = input_int_expect()
                        Clear_screen()
                        if list_user_input == 0:
                            Clear_screen()
                            break
                        elif list_user_input == 1:
                            while True:
                                Clear_screen()
                                print('Orders list by Status\n')
                                # order_functions_modul.print_order_status_list(order_status)
                                orders_database_modul.print_orderstatus_table(get_connection)
                                status_index = input_int_expect()
                                status_ids_list = orders_database_modul.status_ids_list(get_connection)
                                if status_index in status_ids_list:
                                    Clear_screen()
                                    # order_functions_modul.orders_by_status(status_index, order_status, orders_list)
                                    orders_database_modul.orders_by_status(status_index, get_connection)
                                    press_to_continue()
                                    break
                                else:
                                    print("Invalid value!Please choose from the available options!")
                                    press_to_continue()
                        elif list_user_input == 2:
                            while True:
                                Clear_screen()
                                print('Orders list by Courier\n')
                                orders_database_modul.orders_by_courier(get_connection)
                                press_to_continue() 
                                break                    
                else:
                    Clear_screen()
                    print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                    press_to_continue()
            if order_user_input == 0: # exit from the inner while loop
                    break
            
#-------------------------------------couriers menu-----------------------------------------------------------------------------   

        elif x == 3: 
            while True:     
                Clear_screen()
                print('''
Couriers Menu:

1 - Couriers list          
2 - Creat/Add new Courier      
3 - Update existing Courier
4 - Delete Courier         
0 - Return to Main Menu

            ''')
                courier_user_input = input_int_expect()
                if courier_user_input == 0: # 0-Return to Main Menu
                    Clear_screen()
                    break
                elif courier_user_input == 1: # 1-PRINT couriers list 
                    Clear_screen()
                    couriers_database_modul.print_couriers_table(get_connection)
                    press_to_continue()
                elif courier_user_input == 2: # 2-Creat/Add new couriers
                    Clear_screen()
                    print('Creat/Add new Courier:\n')
                    new_courier = input('\nPlease type in the courier name: ')
                    new_courier_phone = input_phone_expect()
                    couriers_database_modul.insert_courier_to_db(new_courier, new_courier_phone, get_connection)
                    press_to_continue()
                elif courier_user_input == 3: # 3-Update existing couriers
                    while True: 
                        Clear_screen()
                        print('Update existing Couriers:\n')
                        couriers_database_modul.print_couriers_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = couriers_database_modul.ids_list(get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            name = input(f'Update name, please add the new value, or press enter: ')
                            phone = input_phone_expect()
                            couriers_database_modul.update_couriers_table(name, phone, index_value, get_connection)
                            press_to_continue()
                            Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                elif courier_user_input == 4: # 4-Delete couriers                            
                    while True: 
                        Clear_screen()
                        print('Delete Courier:\n')
                        couriers_database_modul.print_couriers_table(get_connection)
                        index_value = input_int_expect()
                        ids_list = couriers_database_modul.ids_list(get_connection)
                        Clear_screen()
                        if index_value in ids_list:
                            couriers_database_modul.delete_courier(index_value,get_connection)
                            press_to_continue()
                            Clear_screen()
                            break
                        else:
                            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
                            press_to_continue()
                else:
                    Clear_screen()
                    print(COLOR["RED"],"Invalid number!Please choose from the available options!", COLOR["ENDC"])
                    press_to_continue()     
        else:
            Clear_screen()
            print(COLOR["RED"],"Invalid value!Please choose from the available options!", COLOR["ENDC"])
            press_to_continue()
        break     

