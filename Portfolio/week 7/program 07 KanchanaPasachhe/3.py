def main():
    countries_capital = {
        'nepal' : 'Kathmandu',
        'usa':'Washington DC',    
        'england' : 'London',
        'france':'Paris',
        'china': 'Beijing',
        'canada':'Ottawa'
    }

    print("Welcome to the countries and capital program.")
    print("Type'exit' to terminate the program...")

    while True:
        country=input("Enter the name of a country:").strip()    

        if country.lower()=="exit":
            print("Exiting program...")
            break
        
        #for tackling case sensitivity
        new_country=country.lower()

        if new_country in countries_capital:
            capital=countries_capital[new_country]
            print(f"The capital of {country} is {capital}")
        else:
            capital=input(f"I do not know the capital of {country}. Please enter it:").strip()

            if capital.lower()=="exit":
                print("Exiting the program...")
                break
            
            countries_capital[new_country]=capital
            print(f"Thank you! I've recorded that the capital of {country} is {capital}.")
            
if __name__ == "__main__":
    main()
