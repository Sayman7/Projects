#Initializing global variables for creating calendar systematically
month=1
d=0
day=6
rep=1
#list containing names of all the months to be displayed on the calendar
m= ["January","February","March","April","May","June","July","August","September","October","November","December"]
a=list() #list to store calendar of a month
b=list() #list to store calendar of a week

def reset(): #function to clear list to generate calendar of next month or new year's month
   #calling global variables in the function
   global rep, day, d, month, m, a, b
   a=list()
   d=0
   month= month+1 #moving to the next month

def display(year): #function to display the calendar of a month
    #calling global variables in the function
    global rep, day, d, month, m, a, b
    a.append(b) #filling the calendar of last-halved week inside the list of month: b=list()
    if(rep==year): #printing the calendar of the entered year
     #designing the calendar using strings and new lines
     print()
     print("      "+m[month-1]) #displaying the name of month just before it's calendar
     print("--------------------")
     print("Su|Mo|Tu|We|Th|Fr|Sa") #displaying the name of days in a week
     print("--------------------")
     #printing the calendar of a month
     for i in a:
        for j in i:
           if(j==" "):
            print("   ",end= "")
           else:
             print(j+" ",end="")
        print() #changing lines of dates with a new week

def main(): #main function to generate calendar's
 #calling global variables
 global rep, day, d, month, m, a, b
 year= int(input("Enter a year in numeric to get its calendar: ")) #taking input of a year 
 while(rep<=year):                                                 #to display it's calendar
   month= 1  #changing the month to january=1 with change in year in process
   while(month<=12): 
    if(d==0):
      b= list() #clearing the last halved week from the list of previous month
      for i in range(day):
        b.append(" ") #filling the first week with blank dates
    d= d+1 #changing the dates in a month
    if((d==3) and (month==9) and (rep==1752)): #Skipping 11 days for year 1752 in history
      d=14
      day=4
    if(d<10): #converting dates 0 to 9 to double digit form
      b.append("0"+str(d))
    else:
      b.append(str(d))
    day= day+1 #changing days with the date
    if(day>6): #changing the week starting from sunday: day=0
       day=0
       a.append(b) #filling a complete week in list of month
       b= list() #clearing the list of week for dates of next week
    # Logic to change month for the month containing 31 days
    if((d==31)and((month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10))):
     display(year)
     reset()
    # Logic to change month for the month containing 30 days
    elif((d==30)and((month==4)or(month==6)or(month==9)or(month==11))):
     display(year)
     reset()
     # Logic to change month if the current month is February
    elif(month==2):
      #Logic for non-leap year February containg 28 days
      if((d==28)and(((rep%100!=0)and(rep%4!=0))or((rep%100==0)and((rep>1700)and(rep%400!=0))))):
       display(year)
       reset()
      #Logic for leap year February containg 29 days
      elif((d==29)and(((rep%100!=0)and(rep%4==0))or((rep%100==0)and(rep%400==0)and(rep>1700))or((rep%100==0)and(rep<=1700)))):
       display(year)
       reset()
    # Logic to change year with reseting the month to january: month=1 if the current month is December
    elif((month==12)and(d==31)):
       display(year)
       reset()
       rep= rep+1

if __name__=="__main__": # Running the main function as initial
 main()