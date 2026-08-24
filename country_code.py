def country_code():
    status = True
    while status:
        country_code= input("enter name city: ")
        if len(country_code) != 2:
            print(" enter only country code ! ")
            continue
        if country_code == "":
            print(" the country code cannot be empty ! ")
            continue
        country_code = country_code.replace(" ","").upper()
        status = False 
        return country_code