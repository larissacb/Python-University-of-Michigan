hrs = input("Enter Hours:")
h = float(hrs)
perhour = input("Enter per hour:")
ph = float (perhour)

if(h > 40.0):
    result = (h-40.0)*(0.5*ph)
    result = result + (h*ph)
    print(result)
