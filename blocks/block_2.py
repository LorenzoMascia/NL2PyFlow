def block_2(context: dict) -> dict:
    filtered_records = [record for record in context.get('records', []) if record.get('amount') > 1000]
    context['filtered_records'] = filtered_records
    return context