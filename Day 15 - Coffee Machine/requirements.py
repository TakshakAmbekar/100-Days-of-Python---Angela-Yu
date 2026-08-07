'''
Coffee types: 
    Espresso: 50ml water, 18g coffee, $1.50
    Latte: 200ml water, 24g coffee, 150ml milk, $2.50
    Cappuccino: 250ml water, 24g coffee, 100ml mils, $3.00
    
Machine resources:
    water: 300ml
    milk: 200ml
    coffee: 100g
    money: $0.00

Coins:
    penny: $0.01
    nickel: $0.05
    dime: $0.10
    quarter: $0.25
    
Program requirements:
    1. Print resources
    2. Check if sufficient resources
    3. Let user input number of coins, and return the change
    4. Check if the transaction was successful
    
use :.2f in an f-string to get exactly 2 decimal places
'''

MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte":{
            "ingredients":{
                "water": 200,
                "milk": 150,
                "coffee": 24
            },
            "price": 2.5
        },
    "cappuccino":{
            "ingredients":{
                "water": 200,
                "milk": 100,
                "coffee": 24
            },
            "price": 3.0
        }
}

COINS = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

resources = {
    "water": {
        "quantity": 1000,
        "unit": "ml"
    },
    "milk": {
        "quantity": 500,
        "unit": "ml"
    },
    "coffee": {
        "quantity": 200,
        "unit": "gm"
    },
    "money": {
        "quantity": 0,
        "unit": "$"
    }
}
