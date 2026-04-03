import logging
from bot.client import get_client
from tenacity import retry, stop_after_attempt, wait_fixed

client = get_client()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        logging.info(f"Placing order", extra={
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price,
            "stop_price": stop_price
        })

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=str(price),
                stopPrice=str(stop_price),
                timeInForce="GTC",
                workingType="MARK_PRICE"
            )

        else:
            raise ValueError("Unsupported order type")

        logging.info("Order success", extra={"response": order})
        return order

    except Exception as e:
        logging.error("Order failed", extra={"error": str(e)})
        raise