# Found on codewars.com
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)

def make_readable(seconds):
    ss = seconds%60
    mm = (seconds-ss)/60
    hh = ("{:02d}".format(int(mm/60)))
    mm = ("{:02d}".format(int(mm%60)))
    ss = ("{:02d}".format(int(ss)))
    return(f"{hh}:{mm}:{ss}")

print(make_readable(124))