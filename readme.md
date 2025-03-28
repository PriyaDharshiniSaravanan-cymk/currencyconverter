# 💰 Currency Converter

A simple Python-based Currency Converter application using Tkinter for the GUI and requests for API calls to fetch real-time exchange rates.

## ✨ Features

- 📈 Convert currency from one type to another using live exchange rates.
- 📢 User-friendly interface using Tkinter.
- 🔄 Real-time conversion using the ExchangeRate-API.
- ⚠️ Error handling for invalid input or API issues.

## 📝 Prerequisites

- 💻 Python 3.x
- 📀 Internet connection for API access

## ⚙️ Installation

1. Clone the repository or download the project files.

```
git clone https://github.com/your-repo/currency-converter.git
```

2. Install required dependencies using pip:

```
pip3 install requests
```

3. Run the application:

```
python3 currencyconvert.py
```

## 🛠 API Configuration

- This project uses [ExchangeRate-API](https://www.exchangerate-api.com/) for currency conversion.
- Obtain your free API key and update the code by replacing `API_URL` with your API key.

```python
api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
```

## 💳 Usage

1. Enter the amount in the input field.
2. Provide the currency codes (e.g., USD, INR, EUR).
3. Click on **Convert** to get the converted amount.

## 👍 Example

- **Amount:** 100
- **From Currency:** USD
- **To Currency:** INR
- **Output:** `100 USD = 8300 INR` (Based on real-time rates)

## ⚡ Troubleshooting

- Ensure you have a stable internet connection.
- Verify your API key is correct.
- Install missing dependencies using:

```
pip3 install -r requirements.txt
```

## 📚 License

This project is licensed under the MIT License.

## 👤 Contact

For further inquiries, contact \*\*Priya Dharshini\*\* or raise an issue in the GitHub repository.

