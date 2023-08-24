import csv
import datetime
from datetime import timedelta

#CONSTANTS
sStart = '08:00'
sEnd = '17:00'
cStart = '08:00'
cEnd = '20:30'
nStart = '20:00'
nEnd = '08:30'
shiftDescription = '#work'

# A function to add an entry into the calendar CSV
def addShift (subject, startDate, startTime, endDate, endTime, description):
    with open('gCalendarImportFile.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([subject, startDate, startTime, endDate, endTime, description])

# A function that takes a string inputDate in the format YYYY-MM-DD and returns
# a string in format YYYY-MM-DD which is a day later than the input date
# requires use of datetime for the adding of the singular day
# this is needed for night shifts that end a day later than the start date
def addDay (inputDate):
    outputDate = datetime.datetime(int(inputDate[0:4]), int(inputDate[5:7]), int(inputDate[8:10]))
    outputDate += timedelta(days=1)
    output = outputDate.strftime('%Y' + '-' + '%m' + '-' + '%d')
    print(output)
    return output

# Create a new CSV file with calendar suitable header
with open('gCalendarImportFile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Start date', 'Start time', 'End date', 'End time', 'Description'])

# open the CSV file which has been renamed rotadata.csv
with open('rotadata.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # A loop to add the CSV calendar rows
    for row in readCSV:

        # Create a Date object
        # nb/ the date has to be in the format 2020-12-01 in the CSV file!
        date = row[0]
        print(date)

        shiftType = row[1]

        # Initialise an endDate
        endDate = ''

        if shiftType == 'D':
            shiftType = 'Normal Day'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'LD':
            shiftType = 'Day On Call'
            startTime = cStart
            print(startTime)
            endTime = cEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'Night':
            shiftType = 'Night On Call'
            startTime = nStart
            print(startTime)
            endTime = nEnd
            print(endTime)
            # using the addDay() function to add a day (night shifts end a day later)
            endDate = addDay(date)
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'EDT':
            shiftType = 'Educational Development Time'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'SL':
            shiftType += 'Study leave'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
        elif shiftType == 'AL':
            shiftType = 'Annual leave'
            startTime = sStart
            print(startTime)
            endTime = sEnd
            print(endTime)
            endDate = date
            addShift(shiftType, date, startTime, endDate, endTime, shiftDescription)
            