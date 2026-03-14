PYTHON WEATHER APP USING API:
# python-weather-app

APP DETAIL :

     A simple weather application built using Python and the OpenWeatherMap API.  This application retrieves and displays weather details for any city in the world requested by the user.

FEATURES :

      * Fetches real-time weather data.   
      * Displays temperature.
      * Displays humidity.
      * Displays weather condition.

Technologies Used:

                * Python.
                * Requests library.
                * OpenWeatherMap API.

HOW TO RUN :

        * Install requests library.
        * Run the Python Code.
        * Enter a city name to get weather details.

WORKING :

       * import requests - This line helps python to import request library.
        why should we use request ?
              Because it allows Python to send requests to websites/APIs. The program asks the weather server for data.
       * Next , it prints a heading
       * api_key - This contains your api_key value from OpenWeatherMap API.
        why should we use OpenWeatherMap API and what is the need of api_key ?
               OpenWeatherMap API is  easy to use for a beginner. The api_key helps to identify who is using the API , to tracks request , and also prevents misuse.
       * Now , it takes input from the user to fetch details.
       * url - This creates the API request URL.
       * response = requests.get(url).This line sends a request to the web server.
       * data = response.json(). The data that is received from the server in the format of a JSON file.
       * In the next line "cod" represent the "status code" if the code(cod) == 200 it means the status is "success".
        What is the use of sys , main , wind ?
              This keys are already defined in the OpenWeatherMap API. If we made any changes to this it results in keyerror.
       * Now , it extract the information of the city followed by country , next temperature , then humidity, weather and wind.
       * Next , it prints the weather report , followed by city name , country , next temperature , humidity , condition and wind.
       * If the city entered by the user doesn't found , then it prints the else part ("City not found ").

AUTHOR:

Sajiyya Fathima N

BE CSE Student | Python Beginner | Learning APIs 

Oasis Internship | Easwari Engineering College


        
