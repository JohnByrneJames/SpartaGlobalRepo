# import json json
# Create class ExchangeRates with required attributes
# Fetch the data from the json file using the read function
# display the data and the type of the data
# method to return the exchange rates
# display exchange rates with specific currencies
# give full path of the location if saved any where else

import json

class ExchangeRates:
    rates = None  # declaring attribute
    rates_breakdown = None  # declaring attribute

    def get_exchange_rates(self):  # method
        with open("exchange_rates.json") as jsonfile:
            self.rates = json.load(jsonfile)
            return self.rates

    def display_exchange_rates(self):  # method
        if self.rates is None:
            print("Sorry there are no rates loaded. [First get the exchange rates] for today's date.")
            return None
        else:
            print(
                "\n These rates were documented on " + self.rates["date"] + " in comparison to " + self.rates["base"] +
                " as the base currency \n")

            self.rates_breakdown = self.rates["rates"]  # breaks down the data by storing the nested dict in another var

            # print out types of variables we have, the data has been converted into two dictionaries
            print(type(self.rates))
            print(type(self.rates_breakdown))

            for key, value in self.rates_breakdown.items():
                if value == int:  # If the value is a integer
                    print("1", self.rates["base"], "=", key, ":", int(value))
                    continue
                if value == bool:  # If the value is a boolean
                    print(key, ":", bool(value))
                    continue
                # If the value is a string then just print it as normal
                print("1", self.rates["base"], "=", key, ":", value, "/", type(key), "/", type(value))

    def fetch_exchange_rate(self):  # method
        self.get_exchange_rates()  # in case the class get_exchange_rates hasn't been run, run it here

        self.rates_breakdown = self.rates["rates"]  # breaks down the data by storing the nested dict in another var
        user_selection = input("What kind of Currency do you want to convert to? :  ")
        if user_selection.upper() in self.rates_breakdown:  # make sure it is UPPER case
            print("1 " + self.rates["base"] + " = " + str(self.rates_breakdown[user_selection]) + " " + user_selection)
        else:  # if there is no match return them out of the method.
            print("There is no currency with the acronym " + user_selection)


june_rates = ExchangeRates()  # Create instance of ExchangeRates class
june_rates.get_exchange_rates()  # Get the exchange rates from the instance
june_rates.display_exchange_rates()  # Display the exchange rates
june_rates.fetch_exchange_rate()  # Display a particular exchange rate based on input
