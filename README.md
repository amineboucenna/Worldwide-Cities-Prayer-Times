This script fetches the daily prayer times for a given city from the [IslamicFinder](https://www.islamicfinder.org) website. The user specifies the country and city for which they want to get the prayer times. The script then retrieves the prayer times for the entire country and searches for the specified city. If the city is found, the script prints out the prayer times for the current day.

## Requirements

- Python 3.x
- requests library
- Beautiful Soup 4 library

You can install the required libraries by running the following command:

```
pip install requests
pip install bs4
```

Once you have the necessary libraries installed, you can simply clone the project from GitHub:
``
git clone https://github.com/amineboucenna/Worldwide-Cities-Prayer-Times.git
cd Worldwide-Cities-Prayer-Times/
``
## Usage

1. visit [IslamicFinder](https://www.islamicfinder.org/world) and choose your country and your city
2. edit the `city_prayers_times.py` by changing the country and the city
3. Run the script using the command `python city_prayers_times.py`.
4. The script will print out the prayer times for the current day, if the specified country and city are found.

## Example

```bash
$ python city_prayers_times.py
Algiers | Fajr 04:25 | Sunrise 06:09 | Dhuhr 12:49 | Asr 16:25 | Maghrib 19:02 | Isha 20:15
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

