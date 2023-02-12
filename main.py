from fastapi import FastAPI

def menu():
    menu = {}
    menu['1']="List all restaurants"
    menu['2']="List all customers"
    menu['3']="Show reviews for restaurant"
    menu['4']="Post a review"
    while True: 
        options=menu.keys()
        options.sort()
        for entry in options: 
            print entry, menu[entry]

        sel ection=raw_input("Please Select:") 
        if selection =='1': 
        
        elif selection == '2': 
            
        elif selection == '3':
      
        elif selection == '4': 
            break
        else: 
            print "Unknown Option Selected!" 

def main():    
    app = FastAPI();