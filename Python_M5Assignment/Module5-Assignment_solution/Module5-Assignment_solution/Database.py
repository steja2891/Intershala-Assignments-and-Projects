import sqlite3

Book = sqlite3.connect("Book_Database.db")
a = Book.cursor()

def Create_table():
	a.execute('''CREATE TABLE IF NOT EXISTS BookDetails(Sno INTEGER (1000),
	 Name of the Book TEXT (20), Title of the Book TEXT (20),
	  Price INTEGER (5));''')

def Data_Entry():
	a.execute('''INSERT INTO BookDetails VALUES(1,"Heat and Mass Transfer", "R.K.Rajput", 700);''')
	a.execute('''INSERT INTO BookDetails VALUES(2,"Quantitative Aptitude", "R.S.Agarwal", 1000);''')
	a.execute('''INSERT INTO BookDetails VALUES(3,"Introduction to Python", "Guido Van Rassum", 1200);''')
	a.execute('''INSERT INTO BookDetails VALUES(4,"Engineering Mechanics", "Surya Teja", 800);''')
	a.execute('''INSERT INTO BookDetails VALUES(5,"Managerial Economics and Financial Analysis", "A.R. Aryasri", 500);''')
	a.execute('''INSERT INTO BookDetails VALUES(6,"Environmental Science", "Kaushik", 200);''')
	a.execute('''INSERT INTO BookDetails VALUES(7,"Strength of Materials", "R.K.Bansal", 2000);''')
	a.execute('''INSERT INTO BookDetails VALUES(8,"Thermal Engineering", "Rajput", 1100);''')
	a.execute('''INSERT INTO BookDetails VALUES(9,"Theory of Machines", "S.S.Rattan", 1000);''')
	a.execute('''INSERT INTO BookDetails VALUES(10,"Refrigeration and Air Conditioning", "R.S.Khurmi", 900);''')
	Book.commit()
	a.close()
	Book.close()

Create_table()
Data_Entry()