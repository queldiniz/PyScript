import pandas as pd
from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console

title = "Uso de pyscript com pandas"
page_message = "This example loads a remote CSV file into a Pandas dataframe, and displays it."
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

pydom["title#header-title"].html = title
pydom["a#page-title"].html = title

pydom["input#txt-url"][0].value = url

def log(message):
    # log to pandas dev console
    print(message)
    # log to JS console
    console.log(message)

def loadFromURL(event):
    pydom["div#pandas-output-inner"].html = ""
    url = pydom["input#txt-url"][0].value

    log(f"Trying to fetch CSV from {url}")
    df = pd.read_csv(open_url(url))

    pydom["div#pandas-output"].style["display"] = "block"
    pydom["div#pandas-dev-console"].style["display"] = "block"

    display(df, target="pandas-output-inner", append="False")
