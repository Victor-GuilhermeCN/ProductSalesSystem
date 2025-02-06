import pymysql

class Bank:

    def __init__(self):
        self.con = pymysql.connect(host='localhost', db='pdv', user='root', passwd='')
        self.cursor = self.con.cursor()


    def create_table_costumer(self):
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS customer (
                            id_customer INT AUTO_INCREMENT,
                            snn INT(10) NOT NULL,
                            name VARCHAR(255) NOT NULL,
                            b_date DATE,
                            street VARCHAR(255),
                            neighborhood VARCHAR(255),
                            city VARCHAR(255),
                            state VARCHAR(255),
                            country VARCHAR(255),
                            zipcode INT(10),
                            phone VARCHAR(14),
                            PRIMARY KEY (id_customer))''')
            self.con.commit()
        except Exception as error_table_costumer:
            print("Unsuccessful")
            print(error_table_costumer)
        else:
            print('Table Costumer created successfully.')

    def create_table_product(self):
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS product (
                            id_product INT(13) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                            name VARCHAR(255), 
                            manufacturer VARCHAR(255), 
                            manuf_batch varchar(255),
                            exp_date date, 
                            entry_date date, 
                            price DECIMAL(10,2), 
                            quant DECIMAL(10,3), 
                            prod_type VARCHAR(255))''')
            self.con.commit()
        except Exception as error_table_prod:
            print('Unsuccessful')
            print(error_table_prod)
        else:
            print('Table Product created successfully.')

    def create_table_invoice(self):
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS invoice (
                            id_invoice INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            date_inv date DEFAULT NULL,
                            value DECIMAL(10,2),
                            taxes DECIMAL(10,2),
                            item VARCHAR(255),
                            inv_hour time DEFAULT NULL)''')
        except Exception as error_table_invoice:
            print('Unsuccessful')
            print(error_table_invoice)
        else:
            print('Table Invoice created successfully.')

    def create_table_fidelity(self):
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS loyalty_system (
                            id int AUTO_INCREMENT PRIMARY KEY,
                            points DECIMAL(10,2))''')
        except Exception as error_table_fidelity:
            print('Unsuccessful')
            print(error_table_fidelity)
        else:
            print('Table Fidelity created successfully.')

    def select_universal(self, table: str, column: str, identify):
        try:
            self.cursor.execute(f'SELECT * FROM {table} WHERE {column} = {identify}')
            result = self.cursor.fetchall()
            if result:
                for row in result:
                    print(f'SNN:{row[1]}, Name:{row[2]}, Birthday:{row[3]}, Address:{row[4]}, '
                          f'{row[5]} - {row[6]}/{row[7]} - {row[8]}, Zipcode:{row[9]}'
                          f'Phone:{row[10]}.')
            else:
                print('No costumer found.')
        except Exception as error_select_universal:
            print(error_select_universal)



        """    if column == "*":
                self.cursor.execute('SELECT %s FROM %s', (value, column))
            else:
                self.cursor.execute('SELECT %s FROM %s WHERE %s = %s')
        except Exception as error_select_universal
            print('Error in the search.')
            print(error_select_universal)
        else:
            print()"""

if __name__ == '__main__':
    store = Bank()
    #store.create_table_costumer()
    #store.create_table_product()
    #store.create_table_invoice()
    #store.create_table_fidelity()
    store.select_universal('customer', 'snn', 12)
