<<<<<<< HEAD
import random

def block_1(context: dict) -> dict:
    context['random_number'] = random.randint(1, 6)
=======
import csv

def block_1(context: dict) -> dict:
    with open('sales.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if needed
        sales_records = [row for row in reader]
    
    context['sales_data'] = sales_records
>>>>>>> 0509bdd4d0034982a37bcaad665da08b797558b4
    return context