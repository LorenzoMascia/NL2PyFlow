def block_2(context: dict) -> dict:
    filtered_records = {k: v for k, v in context.items() if v > 1000}
    context.update(filtered_records)
    return context