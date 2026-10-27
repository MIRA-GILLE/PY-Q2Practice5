from pyscript import document, display

def check_country(e):
    country = {
        "ph": "Philippines",
        "us": "United States",
        "ca": "Canada",
        "au": "Australia",
        "fr": "France",
    }

    country_code = document.getElementById("countries").value

    display(country.get(country_code, "Country code not found."), target="output1")