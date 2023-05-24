import json

# save all data function
def save_all_data(orders_l, couriers_l, products_l):
    
    # # save products list
    try:
        with open('products_list.json', 'w') as f:
            json.dump(products_l, f, sort_keys = True, indent = 4)
    except FileNotFoundError as a:
        print('Unable to open file: ' + str(a))


    # # save couriers list
    try:
        with open('couriers.json', 'w') as f:
            json.dump(couriers_l, f,  sort_keys = True, indent = 4)
    except FileNotFoundError as a:
        print('Unable to open file: ' + str(a))


    #save orders list
    try:
        with open('data.orders_list.json', 'w') as f:
            json.dump(orders_l, f,  sort_keys = True, indent = 4)
    except FileNotFoundError as a:
        print('Unable to open file: ' + str(a))


    print('All DATA saved into JSON files!')