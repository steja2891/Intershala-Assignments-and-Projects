import sqlite3

Book = sqlite3.connect("Book_Database.db")

print("Welcome to SAITEJA's Book store ")
Book_Name = input("Enter the name of the book you want to purchase: ")
Data = "SELECT * from BookDetails WHERE Name='"+Book_Name+"';"
b = Book.cursor()
b.execute(Data)
result = b.fetchall()

if result == []:
        print('''Sorry..The Book which you are requested is 'NOT AVAILABLE' righr now..
              Please Come Back after some days
              Thank You..Visit Again:)''')
else:
        print(result)
        print("Yes.. It is Available")
final_amount = 0 
while True:        
    Book_Quantity = int(input("Enter how many copies of Book you needed: "))
    price_data = "SELECT price FROM BookDetails WHERE Name = '"+Book_Name+"';"
    price = b.execute(price_data)
    re = price.fetchall()
    answer = input("Add More Books...?(Y/N)")
    final_amount += re[0][0]*Book_Quantity
    if "N" == answer or "n" == answer:
        print("Total cost is: Rs {}/-".format(final_amount))
        print("Please pay your bill and dont forget to receive the receipt")
        break         
    if "Y" == answer or "y" == answer:
        pass

b.close()
Book.close()