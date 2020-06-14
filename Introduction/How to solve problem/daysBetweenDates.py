#!/usr/bin/env python
# coding: utf-8

# # Days Between Dates
# 
# This lesson will focus on one problem: calculating the number of days between two dates. 
# 
# This workspace is yours to use in whatever way is helpful. You might want to keep it open in a second tab as you go through the videos. 
# 
# 

# In[1]:


def isleapyear(year):
    if year%100==0:
        if year%400==0:
            return 29
    elif year%4==0:
        return 29
    else:
        return 28
def daysInmonth(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return isleapyear(year)
def nextday(year,month,day):
    if day<daysInmonth(year,month):
        return year,month,day+1
    elif month<12:
        return year,month+1,1
    else:
        return year+1,1,1
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    counter=0
    while(year1<year2 or month1<month2 or day1<day2):
        year1,month1,day1=nextday(year1,month1,day1)
        counter+=1
    
    return counter

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()


# In[ ]:




