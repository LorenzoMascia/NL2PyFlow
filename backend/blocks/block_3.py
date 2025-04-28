def block_3(context: dict) -> dict:
    total_sales = 0
    for key, value in context.items():
        if isinstance(value, (int, float)):
            total_sales += value
    context["total_sales"] = total_sales
    return context