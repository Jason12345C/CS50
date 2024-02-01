# expect user to specify as a command-line argument the number of bitcoins, n
import requests
import sys
import json

try:
    number_bitcoins = float(sys.argv[1])
    # query API for coindesk bitcoin price index
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = float(o["bpi"]["USD"]["rate"].replace(",", ""))
    cost_bitcoin = float(number_bitcoins * rate)

# if argument cannot be turned to float, sys.exit with error message
except ValueError:
    sys.exit("command-line argument should be a number")
# catch request exception
except requests.RequestException:
    sys.exit()
except IndexError:
    sys.exit("missing command-line argument")

# output the current cost of n bitcoins is USD to four decimal places, using , as a
# thousands separator
print(f"${cost_bitcoin:,.4f}")
