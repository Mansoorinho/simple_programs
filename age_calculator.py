import datetime
import time

#Please create instance of class and methods in order so the program works correctly
#IF YOU WANT MANAULLY CREATE INSTANCE AND RUN THE APP READ BELOW #
### IMPORTANT ###
"""
first of all create instance then use the methods inside the class age in order like below
get_input()-> to get input from terminal , if you dont use this method just initialize the class instance
users_day()
users_month()
users_year()
days_month()
days_dob_month()
month_between()
cmp_m_between()
days_in_year()
alldays()
minutes_lived()
"""
### IMPORTANT ###

#class age to calculate age
start = time.time()
class age:
    def __init__(self, DOB_year=None, DOB_Month=None, DOB_Day=None):
        self.DOB_year = DOB_year
        self.DOB_Month = DOB_Month
        self.DOB_Day = DOB_Day
        self.DOB_Monthh = DOB_Month #used for calculating minutes of age
        
        self.thone=[1,3,5,7,8,10,12]
        self.thirty=[4,6,9,11]
        self.tweight=[2]
        #importing today's date and by spliting and indexing
        onlydate=(str(datetime.datetime.today()).split(" "))[0].split("-")
        #separating today with "-"
        #extracting the exact year month day
        self.year=int(onlydate[0])
        self.month=int(onlydate[1])
        self.monthh=int(onlydate[1])   #for month      
        self.day=int(onlydate[2])
        self.dayy=int(onlydate[2])#for days in month
        self.m_days = 0
        self.n_days = 0
        self.days_year = 0


        
    #user's input
    def get_input(self):
        self.DOB_year=int(input("Enter the year of your birth date: "))
        self.DOB_Month= int(input("Good! now Enter the month of your birth date: "))
        self.DOB_Day=int(input("Good! finally Enter the Day of your birth date: "))

       
    #calcultaing users day of the age (both condtion in this funtion requires to check if the day is in the range of 0 - 31)
    def users_day(self):
        #if today's date is lower than the input day
        if (self.day < self.DOB_Day) and (self.DOB_Day in range(1,32)):
            #check if it is a thirty one day month
            if  (self.month in self.thone) :
                self.day = self.day + 31
            #check if it is a thirty day month
            elif (self.month in self.thirty):
                self.day = self.day + 30
            #if it is a twenty eight day month   
            elif self.day < self.DOB_Day:
                self.day = self.day + 28
            #the new day is the difference of todays and the input day
            self.day = self.day - self.DOB_Day
            #subtract one from month
            self.month = self.month-1

            return self.day
        #if today's date is greater than the input day do normal subtraction no need to subtract one from month
        elif (self.day > self.DOB_Day) and (self.DOB_Day in range(1,32)):
            self.day = self.day - self.DOB_Day
            return self.day

        else:
           return ("\n\n\n Wrong Input for 'day' !! \n\n") 
        #user's month
    def users_month(self):
        if (self.month < self.DOB_Month ) and (self.DOB_Month in range (1,13)):
            self.month = self.month + 12
            self.month = self.month - self.DOB_Month
            self.year = self.year - 1
       
        else:
            self.month = self.month - self.DOB_Month
            self.year = self.year - 1
        return self.month

    def users_year(self):
        if self.year < self.DOB_year:
            return ("Wrong input!")

        else:
            self.year = self.year - self.DOB_year
            return self.year
    #calculating remainder days of the input month
    def days_dob_month(self):
        if self.DOB_Monthh in self.thirty:
            self.new_db_day = 30 - self.DOB_Day
        elif self.DOB_Monthh in self.thone:
            self.new_db_day = 31 - self.DOB_Day
        elif (self.DOB_Monthh in self.tweight) and (self.DOB_Day in range(1,29)):
            self.new_db_day = 28 - self.DOB_Day
        self.DOB_Monthh = self.DOB_Monthh +1
        return self.new_db_day
    #calculating remainder days of the cmp month
    def days_month(self):
        if self.monthh in self.thirty:
            self.new_day = 30 - self.dayy
        elif self.monthh in self.thone:
            self.new_day = 31 - self.dayy
        elif (self.monthh in self.tweight) and (self.day in range(1,29)):
            self.new_day = 28 - self.dayy 
        self.monthh = self.monthh + 1        
        return self.new_day
    #calculating days of the input months till end
    def month_between(self):
        while(self.DOB_Monthh <= 12):
            if self.DOB_Monthh in self.thone:
                self.m_days = self.m_days + 31
            elif self.DOB_Monthh in self.thirty:
                self.m_days = self.m_days + 30
            elif self.DOB_Monthh in self.tweight:
                self.m_days = self.m_days + 28
            self.DOB_Monthh = self.DOB_Monthh + 1
        return self.m_days
    #calculating days of cmp months till end
    def cmp_m_between(self):
        while(self.monthh <= 12):
            if self.monthh in self.thone:
                self.n_days = self.n_days + 31
            elif self.monthh in self.thirty:
                self.n_days = self.n_days + 30
            elif self.monthh in self.tweight:
                self.n_days = self.n_days + 28
            self.monthh = self.monthh + 1
        return self.n_days
    #days in years
    def days_in_year(self):
        self.days_year = self.days_year + (self.year * 356)
        return self.days_year
    #all days of the age
    def alldays(self):
        self.day_lives = (int(self.new_day)+int(self.new_db_day)+int(self.days_year)+int(self.m_days)+int(self.n_days))
        return self.day_lives

    def minutes_lived(self):
        return (self.day_lives*24*60)


users_age = age(1995,11,17)
#users_age.get_input()
day=users_age.users_day()
month=users_age.users_month()
year=users_age.users_year()
day_in_m = users_age.days_month()
dyas=users_age.days_dob_month()
between=users_age.month_between()
ending=users_age.cmp_m_between()
dayyear=users_age.days_in_year()
alld=users_age.alldays()
minutes=users_age.minutes_lived()
print(year,"years",month,"months",day,"days","\n\n")
print(alld,"days lived until today\n")
print(minutes,"minutes lived\n")
end=time.time()
print("code run time is:",end-start)
