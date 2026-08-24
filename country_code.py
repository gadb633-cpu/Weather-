def country_code():
    status = True
    while status:
        country_code= input("enter country code: ")
        if len(country_code) != 2:
            print(" enter only country code ! ")
            continue
        if country_code == "":
            print(" the country code cannot be empty ! ")
            continue
        if country_code == "US":
            if len(country_code) != 2:
                print(" enter only country code ! ")
                continue
            else:
                country_code_inside_US = input("enter country code inside US: ")
                country_code_inside_US = country_code_inside_US.replace(" ","").upper()
                status = False
                return country_code_inside_US
        country_code = country_code.replace(" ","").upper()
        status = False 
        return country_code