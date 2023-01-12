#prompt user
distance = float(input("enter distance travelled in km "))
duration = int(input("enter duration of your journey in hours"))

#calculating and displaying average speed
avg_speed = distance/ duration
print('the average speed is', avg_speed,'km/h')

#prompt user again for the fuel used
fuel_used = float(input("enter amount of fuel used for your journey today in litres"))

#calculating and displaying fuel price
fuel_price = fuel_used * 1.68
print('you paid RM',fuel_price,'for your fuel')

#calculating and displaying claimable mileage
c_mileage = distance * 0.80
print('claimable mileage : RM', c_mileage)

#calculating the difference between claimable mileage and fuel paid
diff_fp_cm = (fuel_price - c_mileage)

#displaying wether personnel gets more or less claim
if c_mileage > fuel_price :
    print('you will get more RM', diff_fp_cm)
else :
    print('you will get less RM', diff_fp_cm)





    