###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day == 30:
        month += 1
        day = 1
        if month == 13:
            year += 1
            month = 1
            return str(year) + ", " + str(month) + ", " + str(day)
        else:
            return str(year) + ", " + str(month) + ", " + str(day)
    else:
        return str(year) + ", " + str(month) + ", " + str(day+1) 
        
#print nextDay(2008, 7, 25)
#print nextDay(1999, 12, 30)
#print nextDay(2013, 1, 30)
#print nextDay(2012, 12, 30)
print nextDay(2012, 1, 1)
print nextDay(2012, 4, 30)
print nextDay(2012, 12, 1)
print nextDay(1999, 12, 30)
print nextDay(2012, 12, 30)
