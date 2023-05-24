import os
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

# 1 print orders table from DB function
def print_orders_table(get_conn):
    print('\nOrders List:\n')
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, courier, status, items FROM orders ORDER BY order_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            print(f'{row[0]}. {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

# 2 - insert a new order in DB function
def insert_new_order(nam, addr, phone_num, courier_ind, com_sept_l, get_conn):
    try:
        cursor = get_conn().cursor()
        
        sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, ({nam}, {addr}, {phone_num}, {courier_ind}, 1, {com_sept_l}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'\nSuccessfully created a new Order!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 3 Update Existing Order Status in DB
def update_order_status(new_stat_index, order_num, get_conn):
    try:
        cursor = get_conn().cursor()

        # sql = "SELECT order_status FROM order_status WHERE order_status_id = %s"
        # cursor.execute(sql, ({new_stat_index}))
        # row = cursor.fetchall()
        # new_status = row[0][0]

        sql = "UPDATE orders SET status = %s WHERE order_id = %s"
        cursor.execute(sql, ({new_stat_index},{order_num}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'Order status is Updated!',COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 4 update orders table in DB function
def update_order_table(order_d, index_v, get_conn):
    try:
        cursor = get_conn().cursor()

        if order_d["customer_name"] != "":
            sql = "UPDATE orders SET customer_name = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["customer_name"]}, {index_v}))
        if order_d["customer_address"] != "":
            sql = "UPDATE orders SET customer_address = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["customer_address"]}, {index_v}))
        if order_d["customer_phone"] != "":
            sql = "UPDATE orders SET customer_phone = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["customer_phone"]}, {index_v}))
        if order_d["courier"] != "":
            sql = "UPDATE orders SET courier = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["courier"]}, {index_v}))
        if order_d["status"] != "":
            sql = "UPDATE orders SET status = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["status"]}, {index_v}))
        if order_d["items"] != "":
            sql = "UPDATE orders SET items = %s WHERE order_id = %s"
            cursor.execute(sql, ({order_d["items"]}, {index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'Order is Updated!',COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 5 Delete an order from DB function
def delete_order(index_v,get_conn):
    try:
        cursor = get_conn().cursor()

        sql = "DELETE FROM orders WHERE order_id = %s"
        cursor.execute(sql, ({index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["RED"],'Order is DELETED!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)


# check index value is in the order_id column? function
def ids_list(get_conn):
    try:
        cursor = get_conn().cursor()

        ids_l = []

        cursor.execute('SELECT order_id FROM orders')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                ids_l.append(r)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return ids_l

#  print order status table from DB function
def print_orderstatus_table(get_conn):
    print('\nOrder Status List:\n')
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT order_status_id, order_status FROM order_status ORDER BY order_status_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            print(f'{row[0]}. {row[1]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

# check index value is in the order_status_id column? function
def status_ids_list(get_conn):
    try:
        cursor = get_conn().cursor()

        status_ids_l = []

        cursor.execute('SELECT order_status_id FROM order_status')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                status_ids_l.append(r)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return status_ids_l

# load orders table from DB function
def load_order_table(index_val, get_conn):
    order = {}
    try:
        cursor = get_conn().cursor()
        
        sql = "SELECT order_id, customer_name, customer_address, customer_phone, courier, status, items  FROM orders WHERE order_id = %s"
        cursor.execute(sql, ({index_val}))
        rows = cursor.fetchall()
        
        for row in rows:
            order ={
            "customer_name": row[0],
            "customer_address": row[1],
            "customer_phone": row[2],
            "courier": row[3],
            "status": row[4],
            "items": row[5]
            }

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return order

# load all orders table from DB function
def load_all_order_table(get_conn):
    order = {}
    try:
        cursor = get_conn().cursor()
        
        sql = "SELECT order_id, customer_name, customer_address, customer_phone, courier, status, items  FROM orders "
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        orders_list = []

        for row in rows:
            order ={
            "order_id": row[0],
            "customer_name": row[1],
            "customer_address": row[2],
            "customer_phone": row[3],
            "courier": row[4],
            "status": row[5],
            "items": row[6]
            }
            orders_list.append(order)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return orders_list

# load status table from DB function
def load_status_table(get_conn):
    status_list = []
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT order_status_id, order_status FROM order_status ORDER BY order_status_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            status ={
            "product_id": row[0],
            "name": row[1],
            "price": row[2]
            }
            status_list.append(status)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return status_list

def status_ids_list(get_conn):
    try:
        cursor = get_conn().cursor()

        status_ids_l = []

        cursor.execute('SELECT order_status_id FROM order_status')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                status_ids_l.append(r)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return status_ids_l

def orders_by_status(status_ind, get_conn):
    try:
        cursor = get_conn().cursor()

        sql = "SELECT order_id, customer_name, customer_address, customer_phone, courier, status, items  FROM orders WHERE 	status = %s"
        cursor.execute(sql, ({status_ind}))
        rows = cursor.fetchall()
        for row in rows:
            print(f'{row[0]}. {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

def orders_by_courier(get_conn):
    try:
        cursor = get_conn().cursor()

        ids_l = []
        couriers_name_list = []

        cursor.execute('SELECT courier_id FROM couriers')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                ids_l.append(r)

        cursor.execute('SELECT name FROM couriers')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                couriers_name_list.append(r)

        name = 0
        for id in ids_l:
            sql = "SELECT order_id, customer_name, customer_address, customer_phone, courier, status, items  FROM orders WHERE courier = %s"
            cursor.execute(sql, ({id}))
            rows = cursor.fetchall()
            if not rows:
                print(COLOR["RED"],f'\n{couriers_name_list[name]} has no orders yet! ', COLOR["ENDC"])
                name += 1
            else:
                print(f'\n{couriers_name_list[name]} has the following orders: ')
                name += 1
                for row in rows:
                    print(f'{row[0]}. {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)


