# Worldwide-Cities-Prayer-Times
A Python script that scrapes Islamic prayer times from IslamicFinder.org for a specified city and displays them on a Polybar panel. It uses requests and Beautiful Soup libraries for HTTP requests and parsing HTML respectively. The script can be run periodically with a scheduler to keep the prayer times up-to-date.

This Python script allows users to get Islamic prayer times for a given city and country. It uses Beautiful Soup library to parse HTML content of the page and extracts prayer times from the website IslamicFinder.org.

Getting Started
Prerequisites
Python 3
requests library
beautifulsoup4 library
To install the required libraries, use the following command:

Copy code
pip install requests beautifulsoup4
Running the Script
To run the script, you need to modify the following variables according to your city and country:

country
city
Once you have modified the variables, run the script using the following command:

Copy code
python prayer_times.py
Sample Output
Copy code
Algeirs | 04:54 | 06:22 | 12:47 | 15:48 | 18:27 | 19:56
License
This project is licensed under the MIT License - see the LICENSE file for details.
