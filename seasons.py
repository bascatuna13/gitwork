def seasons():
    while True:
        month = int(input("enter number of month"))
        if month <1 or month >12:
            print("enter 1-12 range")
            continue
        if month in(12,1,2):
            print("Winter")
            break

        if month in(9,10,11):
            print("Autumn")
            break

        if month in(3,4,5):
            print("Spring")
            break
        add-autumn
        if month in(6,7,8):
            print("Summer")
            break
seasons()

