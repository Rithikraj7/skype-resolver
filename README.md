# skype IP Resolver

This is a Python script that retrieves the reverse IP for a given domain name using the "resolvethem.com" website. It utilizes the `requests` and `beautifulsoup4` libraries for web scraping and HTML parsing.

## Requirements

- Python 3.x
- requests library: Install using `pip install requests`
- beautifulsoup4 library: Install using `pip install beautifulsoup4`

## Usage

1. Run the script by executing the `main.py` file.
2. Enter the domain name you want to resolve the reverse IP for in the `name_to_resolve` variable.
3. The script will retrieve the reverse IP using the "resolvethem.com" website.
4. If the reverse IP is found, it will be displayed in the console.
5. If the reverse IP is not found or any errors occur, an appropriate message will be displayed.

Note: The accuracy of the reverse IP resolution depends on the data provided by the "resolvethem.com" website. Make sure the website is accessible and returns the expected HTML content.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

