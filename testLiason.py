from fitbitLiason import *

def printCallList():
    print """You may test any of the following calls:
        -call (makes an arbitrary call using the string you input)
        -getActivity
        -getSleep
        -getProfile
        -getAvgSteps
        -getAvgAwakenings
        -getSleep
        -getBodyMeasurements
        -getAvgMinToSleep
        """


if __name__ == '__main__':
    #create instance	
    tester = fitbitLiason() 

    #create some space to compensate for fitbit.py output
    print ' '
    print 'Initializing tests...'
    print 'Here is the generated URL: ' + tester.getURL()
    print 'Please visit that URL, then copy the OAuth verifer.'
    print 'It will look like this: &oauth_verifier=XXXXXXXXXXXXXXXX'
    print 'You want to copy the XXXXXXXXXXXX to your clipboard'

    #wait for user input
    verifier = raw_input("Now please input the verifer here: ")

    access = tester.retrieveAccessToken(verifier)
    print '... successfully retrieved the access token.'
        
    while True:
        #prompt user for input
        choice = raw_input("""Type in the name of an API call (such as getAvgSteps), "list" to see testable calls or "q" to exit: """)
        #received user input
        if (choice == 'call'):
            desiredCall = raw_input('Enter a string representing the desired call.')
            (tester.call(desiredCall))

        elif (choice == 'list'):
            printCallList()

        elif (choice=='getSleep'):
            print 'What date would you like to retrieve data for?'
            day = raw_input('Input date as yyyy-mm-dd: ')
            print tester.getSleep(day) 

        elif (choice=='getBodyMeasurements'):
            print 'What date would you like to retrieve data for?'
            day = raw_input('Input date as yyyy-mm-dd: ')
            tester.getBodyMeasurements(day)

        elif (choice=='getActivity'):
            print 'What date would you like to retrieve data for?'
            day = raw_input('Input date as yyyy-mm-dd: ')
            tester.getActivity(day)

        elif (choice=='getProfile'):
            tester.getProfile()

        elif (choice=='getAvgSteps'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input('What range of dates would you like to use? Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max... ') 
            tester.getAvgSteps(baseDate, period)

        elif (choice=='getAvgMinToSleep'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input('What range of dates would you like to use? Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max... ') 
            tester.getAvgMinToSleep(baseDate, period)

        elif (choice=='getAvgAwakenings'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input('What range of dates would you like to use? Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max... ') 
            tester.getAvgAwakenings(baseDate, period)

        elif (choice=='getEfficiencySeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getEfficiencySeries(baseDate, period)

        elif (choice=='getMinutesToFallAsleepSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getMinutesToFallAsleepSeries(baseDate, period)

        elif (choice=='getAwakeningsCountSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getAwakeningsCountSeries(baseDate, period)

        elif (choice=='getMinutesAsleepSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getMinutesAsleepSeries(baseDate, period)

        elif (choice=='getActiveScoreSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getActiveScoreSeries(baseDate, period)

        elif (choice=='getMinutesAsleepSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getMinutesAsleepSeries(baseDate, period)

        elif (choice=='getBodyMeasurementSeries'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print 'Bodyfat: '
            print tester.getBodyfatSeries(baseDate, period)
            print 'Bodyweight: '
            print tester.getBodyweightSeries(baseDate, period)
            print 'BMI: '
            print tester.getBMISeries(baseDate, period)

        elif (choice=='getBodyMeasurements'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd:')
            print tester.getBodyMeasurements(baseDate)

        elif (choice=='getBedtime'):
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd:')
            print tester.getBedtime(baseDate)

        elif choice=='getBedtimeSeries':
            print 'What is your base date?'
            baseDate = raw_input('Input date as yyyy-mm-dd or use the today keyword: ')
            period = raw_input("""What range of dates would you like to use?Choices are: 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max...""")
            print tester.getBedtimeSeries(baseDate, period)

        elif (choice=='q'): #exit condition
            print 'Terminating testing module...'
            break
        else:
            print 'Invalid syntax, please read the instructions carefully!'
