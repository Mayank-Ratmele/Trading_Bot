# Binance Futures Testnet Trading Bot

A CLI-based Python trading bot that places MARKET, LIMIT, and STOP-LIMIT orders on Binance Futures Testnet (USDT-M).

---

## 🚀 Features

- Place MARKET, LIMIT, and STOP-LIMIT orders
- Supports BUY and SELL sides
- Interactive CLI mode for better UX
- Input validation and error handling
- Retry mechanism for API failures
- Structured JSON logging
- Clean modular architecture

---

## 🛠 Tech Stack

- Python 3.x
- python-binance
- Click (CLI)
- Tenacity (retry logic)
- dotenv (environment variables)

---

## 📁 Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│ ├── cli.py
│ └── init.py
│
├── logs/
│ └── bot.log
│
├── .env
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone <your-repo-url>
cd trading_bot

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Configure environment variables

Create a `.env` file:

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key

---

### 4. Get Binance Testnet API Keys

- Go to: https://testnet.binancefuture.com
- Create account
- Generate API keys from API Management
- Ensure Futures trading is enabled

---

## ▶️ Usage

### Interactive Mode (Recommended)

python -m bot.cli --interactive

---

### Market Order

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

---

### Limit Order

python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

### Stop-Limit Order

python -m bot.cli
--symbol BTCUSDT
--side BUY
--type STOP_LIMIT
--quantity 0.001
--price 65000
--stop_price 64000

---

## 🧾 Logging

Logs are stored in:

logs/bot.log

Format: JSON structured logs including request, response, and errors.

---

## ⚠️ Notes

- Uses Binance Futures **Testnet only** (no real funds involved)
- Ensure sufficient testnet balance before placing orders
- STOP-LIMIT orders require both `price` and `stop_price`

---

## ✅ Assignment Coverage

- ✔ Market & Limit orders
- ✔ BUY/SELL support
- ✔ CLI input handling
- ✔ Validation & error handling
- ✔ Logging system
- ✔ Modular code structure
- ✔ Bonus: Stop-Limit + Interactive CLI + Retry logic

---

## 📌 Assumptions

- User has valid Binance Futures Testnet API keys
- Symbol format follows Binance standards (e.g., BTCUSDT)
- Network connectivity is stable