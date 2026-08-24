def name_city():
    status = True
    while status:
        city = input("enter name city: ")
        if city == "":
            print(" the city cannot be empty ! ")
            continue
        status =False
        return city
