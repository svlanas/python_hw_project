try:
    sum_loan = int(input("Enter the required loan amount "))
    print("Loan term 1 year")
    print("{:^5} {:^14} {:^15}".format("Month", "Payment amount", "Interest amount"))
    for i in range(1, 13):
        sum_month = sum_loan / 12
        sum_perc = sum_month * (13 - i) * 0.02
        sum_paym = sum_month + sum_perc
        print("{:>5} {:>14.2f} {:>15.2f}".format(i, sum_paym, sum_perc))

    print("\nLoan term 5 year")
    print("{:^5} {:^14} {:^15}".format("Month", "Payment amount", "Interest amount"))
    for j in range(1, 61):
        sum_month = sum_loan / 60
        if j < 24:
            sum_perc = sum_month * (61 - j) * 0.02
        else:
            sum_perc = sum_month * (61 - j) * 0.04
        sum_paym = sum_month + sum_perc
        print("{:>5} {:>14.2f} {:>15.2f}".format(j, sum_paym, sum_perc))
except ValueError:
    print("You entered an incorrect value")


