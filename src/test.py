import pymysql
import os
import csv
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



# some function

def extract_and_clean_sales_data():
    sales_data = []
    try:
        with open('sales_data.csv', 'r') as file:
            source_file = csv.DictReader(file, fieldnames=['customer_id', 'purchase_date', 'purchase_amount', 'product_id'], delimiter=',')
            next(source_file) #ignore the header row
            for row in source_file:
                if '' not in row.values():
                    sales_data.append(row)
    except Exception as error:
        print("An error occurred: " + str(error))

    return sales_data


# extract and clean the data
cleaned_sales_data = extract_and_clean_sales_data()

# Transform
def insert_data_to_database(cleaned_sales_d, get_conn):
    try:
        cursor = get_conn().cursor()
        
        for data in cleaned_sales_d:
            sql = "INSERT INTO sales_data VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ({data[0]}, {data[1]}, {data[2]}, {data[3]}))

        get_conn().commit()
        cursor.close()
        print('\nSuccessfully created a new Order!')
    except Exception as ex:
        print('Failed to open connection', ex)


insert_data_to_database(cleaned_sales_data, get_connection)


