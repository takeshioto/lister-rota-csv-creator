# lister-rota-csv-creator

A python script to turn a work excel rota into a google calendar csv

HOWTO

Format using Microsoft Excel your rota line into the format shown in the example rotadata.csv. This will require a little bit of work on your end but shouldn't take long.

Make sure to format the dates into YYYY-MM-DD (select the column and press 'control'+'1' in Microsoft Excel)

Save said file as a .csv file named rotadata.csv

Install Python

Place the script and YOUR newly created .csv file into the same working directory

Make sure to delete the existing rotadata.csv file if you've downloaded it from GitHub as this is my rota, not yours

Run the script

Import the created gCalendarImportFile.csv into your Google Calendar. I HIGHLY HIGHLY HIGHLY recommend creating a new Google Calendar to import the file to (so you can delete it if it goes wrong rather than importing the file to your main calendar, then you have to delete each event individually if it's not correct)

IMPORTANT: The second column in the .csv needs to be in the format of D/LD/Night/EDT

If theres a problem with the dates it's probably Excel displaying the format in a UK local format DD-MM-YYY while the underlying data is in the universal YYYY-MM-DD

Or you need to ensure the .csv file is saved as the correct unicode format - .csv without UTF-8 formatting
