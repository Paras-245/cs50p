import sys,requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
print(data)
