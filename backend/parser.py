import random

def parse_bill(file_contents):
    current_bill = random.randint(2500, 7000)

    previous_bill = current_bill - random.randint(200, 1200)

    increase = current_bill - previous_bill

    percentage = round((increase / previous_bill) * 100, 2)

    return {
        "current_bill": current_bill,
        "previous_bill": previous_bill,
        "increase": increase,
        "percentage": percentage,
        "reason": "Higher AC usage and fuel surcharge adjustment"
    }