import requests  # Import the requests library to send HTTP requests
import bs4  # Import the Beautiful Soup library for parsing HTML

# Specify the URL of the web page to be scraped, including the language, country, and city
city_code = ""  # Not used in this code, can be ignored
separator = " | "  # A separator string to be used when joining prayer times
country = "Algeria"
city = "Algiers"
url = f"https://www.islamicfinder.org/world/{country}/"

# Send a GET request to the specified URL and get the response object
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup and create a BeautifulSoup object
soup = bs4.BeautifulSoup(response.content, "html.parser")

# Find all paragraph elements with the "xs" class, which contain the full hijri date
full_hijri_date = soup.find_all("p",{"class":"xs"})

# Find the table element containing prayer times for all cities in the country
prayers_table = soup.find("table")

# Assume no city is found until we actually find it in the table
no_city_found = True

try :
    # Find all anchor elements with the "underlined" class, which link to cities
    table_cities_rows = prayers_table.find_all("a",{"class":"underlined"})
except AttributeError:
    # If there's no prayers table, there are no cities to find, so exit
    print("No Country Found!")
    exit(-1)

# Loop through all the cities in the table and try to find the requested city
for table_city in table_cities_rows :
    if table_city.text == city :
        # Initialize a string with the city name
        final_string = city + ''
        # Get the full row of prayer times for the city
        city_full_row = table_city.find_parent()
        for index , prayer in enumerate(city_full_row.findNextSiblings()) :
            # Sunrise and Qiyam prayers are hidden, so ignore them
            if index != 0 and index != 6 :
                # Append each prayer time to the final string, separated by the separator string
                final_string = final_string + separator + prayer.text
        # Mark the city as found and print the final string
        no_city_found = False
        print(final_string)
        break
    
if no_city_found :
    # If the city wasn't found, print a message to let the user know
    print("No City Found!")