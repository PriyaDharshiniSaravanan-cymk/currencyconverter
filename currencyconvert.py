import requests
from tkinter import *
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()

        if from_currency == to_currency:
            result_label.config(text="From and To currency cannot be the same.")
            return

        # Using a free API for currency conversion
        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(api_url)

        if response.status_code != 200:
            messagebox.showerror("Error", "Invalid currency code or API error.")
            return

        data = response.json()

        if to_currency not in data['rates']:
            messagebox.showerror("Error", "Invalid currency code.")
            return

        conversion_rate = data['rates'][to_currency]
        converted_amount = round(amount * conversion_rate, 2)

        result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# UI Design
root = Tk()
root.title("Currency Converter")
root.geometry("400x300")

Label(root, text="Amount:").pack()
amount_entry = Entry(root)
amount_entry.pack()

Label(root, text="From Currency (e.g., USD):").pack()
from_currency_entry = Entry(root)
from_currency_entry.pack()

Label(root, text="To Currency (e.g., INR):").pack()
to_currency_entry = Entry(root)
to_currency_entry.pack()

convert_button = Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()
