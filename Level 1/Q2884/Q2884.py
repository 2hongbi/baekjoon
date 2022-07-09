hour, minute = map(int, input().split())
if minute < 45:
    minute = minute + 15
    if hour == 0:
        hour = 24
    hour = hour - 1
else:
    minute = minute - 45
print("{0} {1}".format(hour, minute))