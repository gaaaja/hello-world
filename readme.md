# URL Shortening Service 

This Flask application simplifies the process of shortening URLs by offering an API endpoint for transforming lengthy URLs into shorter versions. Additionally, it seamlessly redirects these shortened URLs back to their original.

## Installation 

1- Navigate to project directory 
 - open a terminal window and move into the project directory. 

2- Install the required modules : pip install Flask

3- Run the application :
 - Execute "python app.py" to start the Flask application .


## Usage 
1- Run the Flask application : use this command "python app.py".**
2- The application will run on "http://localhost:5000"**
3- Use Postman or any other HTTP client to interact with the API

## Endpoints 
1 - Shorten URL 

Formulate a POST request directed to the /shorten endpoint, including within its JSON payload the URL you wish to shorten. Afterwards, validate the response received to ensure it includes a newly generated shortcode(201)

json
{
    "url": "YOUR_LONG_URL",
    "shortcode": "YOUR_CUSTOM_SHORTCODE" (optional)
}

2 - Redirect to long URL endpoint

Upon accessing the URL endpoint /shortcodes, implemented with the GET method, the service checks for the existence of the provided shortcode. If the shortcode is found within the system, the client is seamlessly redirected to the corresponding original long URL associated with the shortcode.
