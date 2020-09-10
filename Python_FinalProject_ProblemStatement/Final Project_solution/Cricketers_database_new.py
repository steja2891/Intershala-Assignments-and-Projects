import sqlite3

Cricket = sqlite3.connect("Cricket_Players_Database.db")
a = Cricket.cursor()

def Create_match1():
   a.execute('''CREATE TABLE IF NOT EXISTS Match1(Player STRING (50),
Scored INTEGER (1000),Faced INTEGER (1000),Fours INTEGER (1000),
Sixes INTEGER (1000),Bowled INTEGER (1000),Maiden INTEGER (1000),
Given INTEGER (1000),Wickets INTEGER (1000),Catches INTEGER (1000),
Stumping INTEGER (1000),RunOut INTEGER (10));''')

def Data_Entry():
   a.execute('''INSERT INTO Match VALUES("Virat Kohli",102,98,8,2,0,0,0,0,0,0,1);''')
   a.execute('''INSERT INTO Match VALUES("Yuvraj Singh",12,20,1,0,48,0,36,1,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Ajinkya Rahane",49,75,3,0,0,0,0,0,1,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Shikhar Dhawan",32,35,4,0,0,0,0,0,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("MS Dhoni",56,45,3,1,0,0,0,0,3,2,0);''')
   a.execute('''INSERT INTO Match VALUES("Axar Patel",8,4,2,0,48,2,35,1,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Hardik Pandya",42,36,3,3,30,0,25,0,1,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Ravindra Jadeja",18,10,1,1,60,3,50,2,1,0,1);''')
   a.execute('''INSERT INTO Match VALUES("Kedar Jadav",65,60,7,0,24,0,24,0,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Ravichandran Ashwin",23,42,3,0,60,2,45,6,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Umesh Yadav",0,0,0,0,54,0,50,4,1,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Jasprit Bumrah",0,0,0,0,60,2,49,1,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Bhuvaneshwar Kumar",15,12,2,0,60,1,46,2,0,0,0);''')
   a.execute('''INSERT INTO Match VALUES("Rohit Sharma",264,170,24,16,0,0,0,0,2,0,1);''')
   a.execute('''INSERT INTO Match VALUES("Dinesh Karthick",29,42,3,0,0,0,0,0,2,0,1);''')
   Cricket.commit()


def Create_table2():
    a.execute('''CREATE TABLE Teams(Name TEXT (20), Players TEXT (10000), Value INTEGER (10000)), Points_used INTEGER (1000), Points_avail INTEGER (1000);''')


def Create_table3():
    a.execute('''CREATE TABLE Stats(Player TEXT (20), Matches INTEGER (1000),
Runs INTEGER (100000),Centuries INTEGER (1000),HalfCenturies INTEGER (1000),Value INTEGER (1000),
Category STRING (10));''')
    

def Data_Entry3():
    a.execute('''INSERT INTO Stats VALUES("Virat Kohli",189,8257,28,43,120,"BAT");''')
    a.execute('''INSERT INTO Stats VALUES("Yuvraj Singh",86,3589,10,21,100,"BAT");''')
    a.execute('''INSERT INTO Stats VALUES("Ajinkya Rahane",158,5435,11,31,100,"BAT");''')
    a.execute('''INSERT INTO Stats VALUES("Shikhar Dhawan",25,565,2,1,85,"BAT");''')
    a.execute('''INSERT INTO Stats VALUES("MS Dhoni",78,2573,3,19,90,"WK");''')
    a.execute('''INSERT INTO Stats VALUES("Axar Patel",67,208,0,0,100,"BWL");''')
    a.execute('''INSERT INTO Stats VALUES("Hardik Pandya",70,77,0,0,75,"AR");''')
    a.execute('''INSERT INTO Stats VALUES("Ravindra Jadeja",16,1,0,0,85,"BWL");''')
    a.execute('''INSERT INTO Stats VALUES("Kedar Jadav",111,675,0,1,90,"AR");''')
    a.execute('''INSERT INTO Stats VALUES("Ravichandran Ashwin",136,1914,0,10,100,"AR");''')
    a.execute('''INSERT INTO Stats VALUES("Umesh Yadav",159,1234,0,3,80,"BWL");''')
    a.execute('''INSERT INTO Stats VALUES("Jasprit Bumrah",73,1365,0,8,90,"BWL");''')
    a.execute('''INSERT INTO Stats VALUES("Bhuvaneshwar Kumar",17,289,0,2,75,"AR");''')
    a.execute('''INSERT INTO Stats VALUES("Rohit Sharma",296,8701,15,52,120,"BAT");''')
    a.execute('''INSERT INTO Stats VALUES("Dinesh Karthick",11,111,0,0,75,"WK");''')
    Cricket.commit()
    a.close()
    Cricket.close()
  

def Create_match2():
   a.execute('''CREATE TABLE Match2(Player STRING (50),
Scored INTEGER (1000),Faced INTEGER (1000),Fours INTEGER (1000),
Sixes INTEGER (1000),Bowled INTEGER (1000),Maiden INTEGER (1000),
Given INTEGER (1000),Wickets INTEGER (1000),Catches INTEGER (1000),
Stumping INTEGER (1000),RunOut INTEGER (10));''')

def Create_match3():
   a.execute('''CREATE TABLE Match3(Player STRING (50),
Scored INTEGER (1000),Faced INTEGER (1000),Fours INTEGER (1000),
Sixes INTEGER (1000),Bowled INTEGER (1000),Maiden INTEGER (1000),
Given INTEGER (1000),Wickets INTEGER (1000),Catches INTEGER (1000),
Stumping INTEGER (1000),RunOut INTEGER (10));''')

def Create_match4():
   a.execute('''CREATE TABLE Match4(Player STRING (50),
Scored INTEGER (1000),Faced INTEGER (1000),Fours INTEGER (1000),
Sixes INTEGER (1000),Bowled INTEGER (1000),Maiden INTEGER (1000),
Given INTEGER (1000),Wickets INTEGER (1000),Catches INTEGER (1000),
Stumping INTEGER (1000),RunOut INTEGER (10));''')

def Create_match5():
   a.execute('''CREATE TABLE Match5(Player STRING (50),
Scored INTEGER (1000),Faced INTEGER (1000),Fours INTEGER (1000),
Sixes INTEGER (1000),Bowled INTEGER (1000),Maiden INTEGER (1000),
Given INTEGER (1000),Wickets INTEGER (1000),Catches INTEGER (1000),
Stumping INTEGER (1000),RunOut INTEGER (10));''')

Create_match1()
Data_Entry()
Create_table2()
Create_table3()   
Data_Entry3()
Create_match2()
Create_match3()
Create_match4()
Create_match5()
