def computepay(hrs, rate):
    if hrs > 40:
        return (40*rate)+(hrs-40)*(rate*1.5)
    else:
        return hrs*rate
hrs = input('Please enter your hours: ')
hrs = float(hrs)
rate = input ('Please enter your rate: ')
rate = float(rate)
p = computepay(hrs,rate)
print("Pay", p)
#editing test file for PCSUP
