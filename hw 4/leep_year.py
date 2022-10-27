try:
    year = int(
        input("Enter the year to check whether it is leap or not* \n(*you can only check the years from 1900) \n")
        )

    if year < 1900 or year > 1000000:
        print("The year value you enter doesn't meet the conditions")
    elif year % 4 == 0:
        if year % 100 != 0:
            print(year, "is leep year")
        elif year % 400 == 0:
            print(year, "is leep year")
        else:
            print(year, "is not leep year")
    else:
        print(year, "is not leep year")

except ValueError:
    print("The entered value is not correct")
