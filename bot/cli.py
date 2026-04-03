import click
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

setup_logger()


def interactive_mode():
    click.echo("\n🚀 Interactive Trading Bot\n")

    symbol = click.prompt("Enter Symbol (e.g., BTCUSDT)")
    side = click.prompt("Enter Side (BUY/SELL)").upper()

    click.echo("\nOrder Types:")
    click.echo("1. MARKET")
    click.echo("2. LIMIT")
    click.echo("3. STOP_LIMIT")

    choice = click.prompt("Select option (1/2/3)")

    order_map = {"1": "MARKET", "2": "LIMIT", "3": "STOP_LIMIT"}
    order_type = order_map.get(choice)

    if not order_type:
        raise ValueError("Invalid order type selection")

    quantity = float(click.prompt("Enter Quantity"))

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = float(click.prompt("Enter Price"))

    if order_type == "STOP_LIMIT":
        stop_price = float(click.prompt("Enter Stop Price"))

    return symbol, side, order_type, quantity, price, stop_price


@click.command()
@click.option("--interactive", is_flag=True, help="Run in interactive mode")
@click.option("--symbol")
@click.option("--side")
@click.option("--type", "order_type")
@click.option("--quantity", type=float)
@click.option("--price", type=float)
@click.option("--stop_price", type=float)
def main(interactive, symbol, side, order_type, quantity, price, stop_price):
    try:
        if interactive:
            symbol, side, order_type, quantity, price, stop_price = interactive_mode()

        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)
        validate_stop_price(stop_price, order_type)

        click.echo("\n--- ORDER SUMMARY ---")
        click.echo(f"{symbol} | {side} | {order_type} | Qty: {quantity}")
        if price:
            click.echo(f"Price: {price}")
        if stop_price:
            click.echo(f"Stop Price: {stop_price}")

        order = place_order(symbol, side, order_type, quantity, price, stop_price)

        # ✅ Proper validation
        if not isinstance(order, dict) or "orderId" not in order:
            raise Exception(f"Invalid response from Binance API: {order}")

        click.echo("\n--- RESPONSE ---")
        click.echo(f"Order ID: {order.get('orderId')}")
        click.echo(f"Status: {order.get('status')}")
        click.echo(f"Executed Qty: {order.get('executedQty')}")
        click.echo(f"Avg Price: {order.get('avgPrice')}")

        click.echo("\n✅ Order placed successfully")

    except Exception as e:
        click.echo(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()