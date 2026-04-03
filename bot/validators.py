def validate_side(side: str):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type: str):
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

def validate_quantity(qty: float):
    if qty <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(price, order_type):
    if order_type in ["LIMIT", "STOP_LIMIT"] and (price is None or price <= 0):
        raise ValueError("LIMIT/STOP_LIMIT require valid price")

def validate_stop_price(stop_price, order_type):
    if order_type == "STOP_LIMIT" and (stop_price is None or stop_price <= 0):
        raise ValueError("STOP_LIMIT requires stop price")