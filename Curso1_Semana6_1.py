def computepay(h,r):
    if(h>40.0):
        result =(h-40.0)*(0.5*r)
        result = result+(h*r)
    return result

hrs = float(input("Enter Hours: "))
pay = float(input("Enter the payment: "))

p = computepay(hrs,pay)
print("Pay",p)
