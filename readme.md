## URL Shortening Service 

This Flask application simplifies the process of shortening URLs by offering an API endpoint for transforming lengthy URLs into shorter versions. Additionally, it seamlessly redirects these shortened URLs back to their original.

## Installation 

1. Navigate to Project Directory:
    - Open a terminal window and move into the project directory.

2. Install the Required Modules:
    - Run `pip install Flask` to install the required modules.

3. Run the Application:
    - Execute `python app.py` to start the Flask application.



## Usage 
1. Run the Flask application: 
    - Use this command: `python app.py`. 

2. The application will run on: 
    - `http://localhost:5000`.

3. Use Postman or any other HTTP client to interact with the API.


## Endpoints 

1. **Shorten URL**

    Formulate a POST request directed to the `/shorten` endpoint, including within its JSON payload the URL you wish to shorten. Afterwards, validate the response received to ensure it includes a newly generated shortcode.

    ```json
    {
        "url": "YOUR_LONG_URL",
        "shortcode": "YOUR_CUSTOM_SHORTCODE" (optional)
    }
    ```

2. **Redirect to Long URL Endpoint**

    Upon accessing the URL endpoint `/shortcodes`, implemented with the GET method, the service checks for the existence of the provided shortcode. If the shortcode is found within the system, the client is seamlessly redirected to the corresponding original long URL associated with the shortcode.

