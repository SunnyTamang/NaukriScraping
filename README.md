# Naukri Scraping

It takes job title and scraps the related information such as company name, job title, salary, location etc. Once scraped we can download it in csv format.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt first.

```bash
pip install -r requirements.txt
```

## Usage

If using any IDE, directly run the app.py file and open the given url in browser.
```python
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 318-947-053
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
> Open the http://127.0.0.1:5000/ in your browser.


If no IDE is being used then open terminal and browse to the directory of the project where app.py file is present and run it using below command.

```bash
> python app.py
```

## Important Note

Please change the time.sleep(5) value in app.py accordingly. It scraps the first 22 records

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Open Source