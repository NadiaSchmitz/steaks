# After the personal contest, happy but hungry programmers dropped into the restaurant “Super Steaks”
# and ordered n specialty steaks. Each steak is cooked by frying each of its sides on
# a frying pan for one minute.
# Unfortunately, the chef has only one frying pan, on which at most k steaks
# can be cooked simultaneously. Find the time the chef needs to cook the steaks.
# Input
# The only input line contains the integers n and k separated with a space (1 ≤ n, k ≤ 1000).
# Output
# Output the minimal number of minutes in which the chef can cook n steaks.

time = 0
i = 0

while i == 0:
    n = int(input("Enter a number of Steaks in order: "))
    k = int(input("Enter a Number of Steaks in frying pan: "))
    if n <= 0 or k <= 0:
        print("Wrong number.")
    else:
        i = 1
        if n % k > 0:
            time = (n // k + 1) * 2
        else:
            time = (n // k) * 2
print(time)