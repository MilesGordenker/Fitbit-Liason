import fitbit
import json

#Toggles verbosity of relevant methods
DEBUG=False

class fitbitLiason(): 
 
    # Methods for authentication and debugging

    # Intitializer appropriate for desktop applications
    def __init__(self):
        self.z = fitbit.FitBit()
        self.auth_url, self.auth_token = self.z.GetRequestToken()
              
    #The liason should be initialized AFTER grabbing the Oauth verifier
    #Especially with webdev
    @classmethod
    def withCredentials(cls, oauth_token, oauth_verifier):
        lia = cls()
	lia.auth_token = oauth_token
        lia.verifier = oauth_verifier
        lia.accessToken = lia.retrieveAccessToken(lia.verifier)
        return lia

    #Contact the Fitbit server to get access token
    def retrieveAccessToken(self, verifier):
        theVerifier = verifier #had to make a copy to resolve scoping issues
	self.accessToken = self.z.GetAccessToken(theVerifier, self.auth_token)
	return self.accessToken

    #Get a unique URL for authentication of the device
    def getURL(self):
        return self.auth_url      

    # Makes an arbitrary API call, then returns a dict
    def call(self, call):
        response = self.z.ApiCall(self.accessToken, call) 
        return response    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ONE-TIME RESOURCE ACCESS

    # Retrieves the profile of the user currently logged in
    def getProfile(self):
        if DEBUG:
            print self.call('/1/user/-/profile.json')
        return self.call('/1/user/-/profile.json')
        
    # Generic method for one time resource access. Returns a dict
    def getOneTime(self, resourcePath, date):
        #print '/1/user/-/{0}/date/{1}.json'.format(resourcePath, date)
        theCall = '/1/user/-/{0}/date/{1}.json'.format(resourcePath, date)
        return self.call(theCall)        

    #Retrieves sleep information for the date expressed as: yyyy-mm-dd 
    def getSleep(self, date):
       return self.getOneTime('sleep', date)

    #Retrieves the latest entries at the given date. Includes BMI, fat%, weight
    def getBodyMeasurements(self, date):
       return self.getOneTime('body', date)

    #Retrieves activity levels and self-reported activities
    def getActivity(self, date):
        return self.getOneTime('activities', date)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Methods for retrieving all entries within a given time range
    #baseDate: "The end date when period is provided, in the format yyyy-MM-dd or today; range start date when a date range is  provided.
    #period: "The date range period. One of 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y,max."

    def getSeries(self,resourcePath, baseDate, period):
        #call the appropriate resource
        response = self.z.ApiCall(self.accessToken,
        "/1/user/-/{0}/date/{1}/{2}.json".format(resourcePath, baseDate, period))
        if DEBUG:
            jsonified = json.loads(response)
            print json.dumps(jsonified, sort_keys=True, indent=2)
        return response

    def getStepsSeries(self, baseDate, period):
        return self.getSeries('activities/steps', baseDate, period)

    def getActiveScoreSeries(self, baseDate, period):
        return self.getSeries('activities/activeScore', baseDate, period)

    # retrieves start time for sleep
    def getStartTimeSeries(self, baseDate, period):
        return self.getSeries('sleep/startTime', baseDate, period)

    # retrieves time spent in bed
    def getTimeInBedSeries(self, baseDate, period):
        return self.getSeries('sleep/timeInBed', baseDate, period)

    def getMinutesAsleepSeries(self, baseDate, period):
        return self.getSeries('sleep/minutesAsleep', baseDate, period)

    def getAwakeningsCountSeries(self, baseDate, period):
        return self.getSeries('sleep/awakeningsCount', baseDate, period)

    def getMinutesToFallAsleepSeries(self, baseDate, period):
        return self.getSeries('sleep/minutesToFallAsleep', baseDate, period)

    def getEfficiencySeries(self, baseDate, period):
        return self.getSeries('sleep/efficiency', baseDate, period)
    # Below this marker add to testLiason
    def getMinutesAsleepSeries(self, baseDate, period):
        return self.getSeries('sleep/minutesAsleep', baseDate, period)

    def getBodyfatSeries(self, baseDate, period):
        return self.getSeries('body/fat', baseDate, period)

    def getBodyweightSeries(self, baseDate, period):
        return self.getSeries('body/weight', baseDate, period)

    def getBMISeries(self, baseDate, period):
        return self.getSeries('body/bmi', baseDate, period)

    def getBedtimeSeries(self, baseDate, period):
        return self.getSeries('sleep/startTime', baseDate, period)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Specialized methods 
    # All use variations of the following call:
    # => GET /<api-version>/user/<user-id>/<resource-path>/date/<base-date>/<period>.<response-format>

    """
    Generic method that allows you to obtain the average of any given resource
    in the Get-Time-Series API

    @param threshold: Only values greater than or equal to the threshold
    parameter will be accounted for in the output
   """ 

    def getAvg(self,resourcePath, baseDate, period, key, threshold):
        #call the appropriate resource
        response = self.z.ApiCall(self.accessToken,
        "/1/user/-/{0}/date/{1}/{2}.json".format(resourcePath, baseDate, period)) 
        jsonified = json.loads(response)
        if DEBUG:
            print json.dumps(jsonified, sort_keys=True, indent=2)
        #extract a dict of dict tuples
        series = jsonified.get(key)
        #initialize auxillary variables
        total = 0
        valid = 0
        #iterate through, and sum
        for i in series:
            cur = int(i.get('value'))
            if cur >= threshold:
                total += cur
                valid += 1
        if DEBUG:
            print "Total: {0}".format(total)
            print "Valid: {0}".format(valid)
        return total/valid

    # get average number of steps taken each day
    # Only days in which over 200 steps are taken are valid
    def getAvgSteps(self, baseDate, period):
        return self.getAvg("activities/steps",baseDate,period,'activities-steps',200)
            
    #get average minutes it takes to fall asleep
    def getAvgMinToSleep(self, baseDate, period):
        return self.getAvg("sleep/minutesToFallAsleep",baseDate,period,'sleep-minutesToFallAsleep',1)

    #get average awakenings count
    def getAvgAwakenings(self, baseDate, period):
        return self.getAvg("sleep/awakeningsCount",baseDate,period,'sleep-awakeningsCount', 1)

    # Get average sleep efficiency
    def getAvgSleepEfficiency(self, baseDate, period):
        return self.getAvg("sleep/efficiency",baseDate,period,'sleep-efficiency',1)
