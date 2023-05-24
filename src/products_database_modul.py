import os
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

# 1 print products table from DB function
def print_products_table(get_conn):
    print('\nProducts List:\n')
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT product_id, name, price FROM products ORDER BY product_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            print(f'{row[0]}. {row[1]}, {row[2]}')

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

# 2 insert a new product to DB function
def insert_product_to_db(name, price, get_conn):
    try:
        cursor = get_conn().cursor()
        
        sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
        cursor.execute(sql, ({name}, {price}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'\nSuccessfully created a new product!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)

# 3 update products table in DB function
def update_products_table(name, price, index_v, get_conn):
    try:
        cursor = get_conn().cursor()

        if name != "" and price != "":
            sql = "UPDATE products SET name = %s, price = %s WHERE product_id = %s"
            cursor.execute(sql, ({name}, {price}, {index_v}))
        elif name != "" and price == "":
            sql = "UPDATE products SET name = %s WHERE product_id = %s"
            cursor.execute(sql, ({name}, {index_v}))
        else:
            sql = "UPDATE products SET price = %s WHERE product_id = %s"
            cursor.execute(sql, ({price}, {index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["GREEN"],'\nProduct updated!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)
# 4 Delete a product from DB function
def delete_product(index_v,get_conn):
    try:
        cursor = get_conn().cursor()

        sql = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(sql, ({index_v}))

        get_conn().commit()
        cursor.close()
        print(COLOR["RED"], '\nProduct is Deleted!', COLOR["ENDC"])
    except Exception as ex:
        print('Failed to open connection', ex)


# get products table length from DB function
def length_product(get_conn):
    try:
        cursor = get_conn().cursor()
        
        cursor.execute("select count(*) from products")  
        x = (list(cursor))
        products_number = str(x).strip(",[]() ")

        # get_conn().commit()
        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)
    return products_number

# check index value is in the product_id column? function
def ids_list(get_conn):
    try:
        cursor = get_conn().cursor()

        ids_l = []

        cursor.execute('SELECT product_id FROM products')
        rows = cursor.fetchall() # lists(rows) in a list
        for row in rows:   # turning the list in a list into juts a list
            for r in row:
                ids_l.append(r)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return ids_l

# load products table from DB function
def load_products_table(get_conn):
    products_list = []
    try:
        cursor = get_conn().cursor()
        
        cursor.execute('SELECT product_id, name, price FROM products ORDER BY product_id ASC')
        rows = cursor.fetchall()

        for row in rows:
            product ={
            "product_id": row[0],
            "name": row[1],
            "price": row[2]
            }
            products_list.append(product)

        cursor.close()
    except Exception as ex:
        print('Failed to open connection', ex)

    return products_list