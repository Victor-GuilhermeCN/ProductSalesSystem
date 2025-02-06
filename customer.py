from databank import Bank

class Customer:

    def __init__(self):
        self.bank = Bank()

    def customer_register(self, snn, name, b_date, street, neighborhood, city, state, country, zipcode, phone):
        try:
            self.bank.cursor.execute('INSERT INTO customer (snn, name, b_date, street, neighborhood, city, state, country, zipcode, phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (snn, name, b_date, street, neighborhood, city, state, country, zipcode, phone))
            self.bank.con.commit()
            self.bank.con.close()
        except Exception as error_reg_customer:
            print('Register error')
            print(error_reg_customer)
        else:
            print("Registration completed successfully")

    def customer_delete(self, snn):
        try:
            self.bank.cursor.execute('DELETE FROM customer WHERE snn = (%s)', (snn))
            self.bank.con.commit()
            self.bank.con.close()
        except Exception as error_delete:
            print('Error')
            print(error_delete)
        else:
            print("Deleted Successfully!")

    def customer_update_address(self, snn, street, neighborhood, city, state, country, zipcode):
        try:
            self.bank.cursor.execute('UPDATE customer SET street = %s, neighborhood = %s, city = %s, state = %s, country = %s, zipcode = %s WHERE snn = %s',
                                     (street, neighborhood, city, state, country, zipcode, snn))
            self.bank.con.commit()
            self.bank.con.close()
        except Exception as error_update_adress:
            print("Failed in the update.")
            print(error_update_adress)
        else:
            print('Updated successfully!')

    def customer_update_phone(self, snn, phone):
        try:
            self.bank.cursor.execute('UPDATE customer SET phone = %s WHERE snn = %s', (phone, snn))
            self.bank.con.commit()
            self.bank.con.close()
        except Exception as error_update_phone:
            print('Failed in the update.')
            print(error_update_phone)
        else:
            print('Updated successfully!')


if __name__ == '__main__':
    c = Customer()
    #c.customer_register(12, 'alex', '1990-05-15',  '123 Main St', 'Downtown', 'New York', 'NY', 'USA', 10001, '555-1234'  )
    #c.customer_delete(12)
    #c.customer_update_address(12, "Mainford", "Lambi", "Ohio","California", "USA", "50444")
    c.customer_update_phone(12, "251-2583")