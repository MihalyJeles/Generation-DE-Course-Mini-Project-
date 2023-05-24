import os
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

# 1 print couriers table from DB function
def print_couriers_table(get_conn):
    print('\nCouriers List:\n')
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT courier_id, name, phone FROM couriers ORDER BY courier_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            print(f'{row[0]}. {row[1]}, {row[2]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

# 2 insert a new courier to DB function
def insert_courier_to_db(name, phone, get_conn):
    try:
        cursor = get_conn().cursor()
        
        sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
        cursor.execute(sql, ({name}, {phone}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'\nSuccessfully created a new courier!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 3 update couriers table in DB function
def update_couriers_table(name, phone, index_v, get_conn):
    try:
        cursor = get_conn().cursor()

        if name != "" and phone != "":
            sql = "UPDATE couriers SET name = %s, phone = %s WHERE courier_id = %s"
            cursor.execute(sql, ({name}, {phone}, {index_v}))
        elif name != "" and phone == "":
            sql = "UPDATE couriers SET name = %s WHERE courier_id = %s"
            cursor.execute(sql, ({name}, {index_v}))
        else:
            sql = "UPDATE couriers SET phone = %s WHERE courier_id = %s"
            cursor.execute(sql, ({phone}, {index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'\nCourier updated!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 4 Delete a courier from DB function
def delete_courier(index_v,get_conn):
    try:
        cursor = get_conn().cursor()

        sql = "DELETE FROM couriers WHERE courier_id = %s"
        cursor.execute(sql, ({index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["RED"],'Courier is DELETED!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)


# get couriers table length from DB function
def length_courier(get_conn):
    try:
        cursor = get_conn().cursor()
        
        cursor.execute("select count(*) from couriers")  
        x = (list(cursor))
        couriers_number = str(x).strip(",[]() ")

        # get_conn().commit()
        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    return couriers_number

# check index value is in the couriers_id column? function
def ids_list(get_conn):
    try:
        cursor = get_conn().cursor()

        ids_l = []

        cursor.execute('SELECT courier_id FROM couriers')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                ids_l.append(r)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return ids_l

# load couriers table from DB function
def load_couriers_table(get_conn):
    couriers_list = []
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT courier_id, name, phone FROM couriers ORDER BY courier_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            courier ={
            "courier_id": row[0],
            "name": row[1],
            "phone": row[2]
            }
            couriers_list.append(courier)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return couriers_list
