def block_3(context: dict) -> dict:
<<<<<<< HEAD
    total_sales = sum(context.get(key, 0.0) for key in context if key.startswith('amount_'))
=======
    total_sales = sum(context.get(key, 0) for key in context if key.startswith('amount_'))
>>>>>>> 0509bdd4d0034982a37bcaad665da08b797558b4
    context["total_sales"] = total_sales
    return context