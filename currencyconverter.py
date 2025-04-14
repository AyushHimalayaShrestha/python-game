import requests
def convert_currency(amount,from_currency, to_currency):
    url =f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response= requests.get(url)

    if response.status_code ==200:
        data =response.json()
        result =data["result"]
        print(f"\n{amount} {from_currency} ={round(result, 2)} {to_currency}")
    else:
        print("Error fetching exchange rate.")

# Get input from user
amount = float(input("Enter amount: "))
from_currency =input("From currency (eg: USD, EUR, NPR): ").upper()
to_currency = input("To Currency (eg: USD, EUR, NPR): ").upper()

convert_currency(amount,from_currency,to_currency)