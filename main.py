from pyscript import document, display

def check_country(e):
    country = {
        "ph": "Philippines",
        "us": "United States",
        "ca": "Canada",
        "au": "Australia",
        "fr": "France",
    }

    document.getElementById("output1").innerHTML = ""
    
    country_code = document.getElementById("countries").value

    #add a country
    country["ca"] = "Canada"

  
    display(country.get(country_code, "Country code not found."), target="output1")