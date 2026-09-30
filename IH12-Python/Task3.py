a = float(input ("Enter the real number: "))
b = float(input ("Enter the imaginary number: "))

my_number = a - b*1j

if my_number.imag > my_number.real:
    print(f"The imaginary part is greater than the real part by {my_number.imag - my_number.real}.")
elif my_number.imag < my_number.real:
    print(f"The real part is greater than the imaginary part by {my_number.real - my_number.imag}.")
elif my_number.imag == my_number.real:
    print("The real and imaginary parts are equal.")
elif my_number.imag == 0 and my_number.real == 0:
    print("The number is zero.")