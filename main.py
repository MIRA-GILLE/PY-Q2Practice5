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
    country["nz"] = "New Zealand"

  
    display(country.get(country_code, "Country code not found."), target="output1")

def show_country(e):
    document.getElementById("output1").innerHTML = "" 
country = {
        "ph": "Philippines",
        "us": "United States",
        "ca": "Canada",
        "au": "Australia",
        "fr": "France",
    }

country_code = document.getElementById("countries").value

show_country = country_code in country
list_country = list(country.keys()) #the country abbreviations
#list_country = list(country.values()) (for the actual values)

display("The number of countries is", len(country), target="output1")
display("Is it in the dictionary?", show_country, target = "output1")
display("What are the countries in the list?", list_country, target= "output1")
