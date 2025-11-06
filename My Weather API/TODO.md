to do:

1.[x] identify what data in reponse is useful and that is what we will be using
-address 
-timezone 
-datetime
-windspeed 

SOLUTION:
IN ORDER TO GET THE DATA NEEDED YOU HAVE TO ACCESS THE DICTIONARY INSIDE THE DAYS, BUT FOR NOW LETS JUST ACCESS THE CONVENIENT TO ACCESS DATAS

2.[x] enhance the caching, use exp

3.[x] implement api limiting 

3.a [x] learn how to deploy in flask

3.b [x] learn why the flask not getting the locaion value, does it require it to show in url

4. [x] understand how to add the response's data uin url like location and date

4.b [x] understand how the url is connected in the data that were getting

ANSWER(3,4): 
THE FLASK GET THE DATA FROM THE INPUT URL USING THE PORT 5000 AND THE REQUEST.ARGS.GET(DATA) THEN PASS IT IN THE API PROCESSING FUNCTION

5. [x] understand how logger works

problems:
[x] unable to check what kind of error
SOLUTION: 
USE TRACEBACK


[x]  URL Encoding: Encode location in URLs to handle spaces or special characters. (no need)

[] Use requests.raise_for_status(): Ensure HTTP errors (4xx/5xx) are caught before .json()

[]  Use params instead of f-strings for query strings: Safer handling of API keys and parameters.

[] Add request timeout: Prevent hanging requests (e.g., timeout=5).

[]  Handle exceptions in /weather route: Wrap request_data() in try/except to return JSON errors instead of server 500.

[] Fix 429 handler: Replace jsonify(error={e}) (set) with jsonify(error=str(e)).

[] Log messages correctly: Avoid passing jsonify() to logger; log strings instead.

[] Support optional date1 and date2: Pass them from Flask GET parameters to request_data().

[] Decode cached bytes: Ensure bytes from cache are decoded before json.loads(). (Already implemented)