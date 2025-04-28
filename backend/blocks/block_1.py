def block_1(context: dict) -> dict:
    import csv
    
    if 'sales.csv' in context:
        file_path = context['sales.csv']
    else:
        file_path = 'sales.csv'
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        records = [row for row in reader]
    
    context['sales_records'] = records
    return context