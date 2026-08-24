def country_code():
    country_code= input("enter name city: ")
    if len(country_code) > 2:
        print(" enter only country code ! ")
    if country_code == "":
        print(" the country code cannot be empty ! ")
        return False    
    country_code = country_code.replace(" ","").upper() 
    return country_code