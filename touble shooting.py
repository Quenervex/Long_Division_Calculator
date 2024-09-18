def long_div(ini,out):
    # handful of variables that will need to be stored globally
    rem = ""
    #converts inside number into string to find out how many characters long it is
    ini_s = str(ini)
    length = len(ini_s)

    #generates the last characters to add on to end of remainder
    for i in range(0, length):
        i = ini_s[-1:i + 1]
        end_numbers = i

    # generates the caracters one by one in order of first to last, in order to be subtracted like long division
    for i in range(0, length):
        i = ini_s[0:i+1]
        ascending_numbers = int(i)
        rem_s = str(int(ascending_numbers - out))
        remainder_1 = int(ascending_numbers - out)
        remainder_2 = int(rem_s + end_numbers)

        #Honestly got no idea if this even works, but it cuts out the numbers that are less than 0 or greater than the
        #inside number so it doesnt show stupid numbers like 144 - 8 = -7
        if remainder_2 > ini or remainder_2 < 0:
            pass
        else:
            rem = rem_s + end_numbers
        if remainder_1 > 0:
            pass
        elif remainder_1 > remainder_2:
            pass

        # shows the math behind if a number is divisible and how many times it is divisible by
        print(f"{ascending_numbers} is divisible by {int(out)}, {int(ascending_numbers/int(out))} times")
        # shows how much each subtraction needed during the process will equal, including useless once that i don't know
        #how to get rid of
        print(f"{ascending_numbers} minus {out} = {ascending_numbers-out}")

        # Really weird way to show the math like its on paper, no idea how to do better but it kind of works
        print(f"""
   {int(ascending_numbers/out)}
  _____
{out}/{ini}
   -{out}
   {rem}""")


long_div(144,8)