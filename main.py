from fastapi import FastAPI


#def menu():
#    menu = {}
#   menu['1']="List all restaurants"
#   menu['2']="List all customers"
#    menu['3']="Show reviews for restaurant"
#    menu['4']="Post a review"
#    while True: 
#        options=menu.keys()
#        options.sort()
#        for entry in options: 
#            print entry, menu[entry]
#
#        sel ection=raw_input("Please Select:") 
#        if selection =='1': 
#        
#        elif selection == '2': 
#            
#        elif selection == '3':
 #     
#        elif selection == '4': 
#            break
#        else: 
#            print "Unknown Option Selected!" 


app = FastAPI()
    
@app.get("/")
def root():
    return "Hello World"

#def populate_database():
#    db_connection = psycopg2.connect(
#database="python_assignment",
#user="admin",
#password="20MaximiLLiaN12",
#host="localhost",
#port= '5432'
#)
#cursor_obj = db_connection.cursor()
#ith cursor_obj.connection as cursor:
#    cursor.execute(open("setupDB.sql", "r").read())
#    cursor.close()
#    cursor.connection.commit()
#    cursor.connection.close()
