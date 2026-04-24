import psycopg2

# establish connection to Postgres
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='34235156Hmm#',dbname='myduka')

# object for db operations
cur = conn.cursor()

#functions

# Task 11-04
#fetching products
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products_data = get_products()
# print(products_data)

#fetching sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales_data = get_sales()
# print(sales_data)

#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

stock_data = get_stock()
# print(stock_data)

# reusable function
def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

users = get_data('users')
products = get_data('products')
sales = get_data('sales')
stock = get_data('stock')
print(products)
# print(sales)
# print(stock)
# print(users)


#insert using functions
def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('samsung',50000,60000)")
    conn.commit()

    return products

# insert_products()

#products function
def insert_products(product_details):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_details}")
    conn.commit()

product1 = ('laptop',50000,60000)
product2 = ('soda',40,50)

# insert_products(product1)
# insert_products(product2)


#sales function
def insert_sales(sales_details):
    cur.execute(f"insert into sales(pid,quantity)values{sales_details}")
    conn.commit()

sale1 = (95,50)
sale2 = (96,60)

# insert_sales(sale1)
# insert_sales(sale2)

#stock function
def insert_stock(stock_details):
    cur.execute(f"insert into stock(pid,stock_quantity)values{stock_details}")
    conn.commit()

stock1 = (95,100)
stock2 = (96,200)

# insert_stock(stock1)
# insert_stock(stock2)

#users function
def insert_users(users_details):
    cur.execute(f"insert into users(full_name,email,phone_number,password)values{users_details}")
    conn.commit()

user1 = ('Husna Mwinyi','housny15@gmail.com',+254700539097,2307)
user2 = ('Alex Kimani','kim15@gmail.com',+254703388064,2305)

# insert_users(user1)
# insert_users(user2)

def sales_per_product():
    cur.execute('''
        Select products.name as p_name, sum(products.selling_price * sales.quantity) as total_sales 
        from products join sales on products.id = sales.pid group by (p_name);
    ''')
    sales_product = cur.fetchall()
    return sales_product

def sales_per_day():
    cur.execute('''
        select date(sales.created_at) as day , sum(sales.quantity * products.selling_price) as total_sales 
        from products join sales on sales.pid = products.id group by day;    
    ''')
    sales_day = cur.fetchall()
    return sales_day

def profit_per_product():
    cur.execute('''
        select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity) 
        from sales join products on products.id = sales.pid group by p_name;
    ''')
    profit_product = cur.fetchall()
    return profit_product

def profit_per_day():
    cur.execute('''
        select date(sales.created_at) as day, sum((products.selling_price - products.buying_price) * sales.quantity) 
        from products join sales on sales.pid = products.id group by day;
    ''')
    profit_day = cur.fetchall()
    return profit_day

# Task
#insert using placeholders
#products function
def insert_products(product_details):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",(product_details))
    conn.commit()

product1 = ('powerbank',8000,10000)
product2 = ('speaker',3000,4000)

# insert_products(product1)
# insert_products(product2)


#sales function
def insert_sales(sales_details):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",(sales_details))
    conn.commit()

sale1 = (97,70)
sale2 = (98,80)

# insert_sales(sale1)
# insert_sales(sale2)

#stock function
def insert_stock(stock_details):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",(stock_details))
    conn.commit()

stock1 = (97,200)
stock2 = (98,300)

# insert_stock(stock1)
# insert_stock(stock2)

#users function
def insert_users(users_details):
    cur.execute("insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",(users_details))
    conn.commit()

user1 = ('Mima Said','mima15@gmail.com','+254700539097',2307)
user2 = ('Kevin Alukwe','kevin15@gmail.com','+254703388064',2305)

# insert_users(user1)
# insert_users(user2)














