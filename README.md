# TemperatureAlert

### Description
TemperatureAlert is a program designed to periodically fetch temperature readings from https://openweathermap.org/api. It performs an analysis of the temperature data, monitoring for both high and low temperature values, and identifies the maximum and minimum temperature recorded. Should the temperature surpass predetermined thresholds, the notifier feature will promptly dispatch notifications to the user.

### Functions
1. Regular Temperature Monitoring: TemperatureAlert consistently monitors temperature data.

2. Low Temperature Notifications: Users are promptly notified if the temperature falls below the designated MIN_TEMPERATURE.

3. High Temperature Notifications: Users receive timely notifications if the temperature surpasses the set MAX_TEMPERATURE.

4. Data Logging: TemperatureAlert routinely saves temperature data to a log file for reference and analysis.

## API KEY
To utilize the OpenWeatherMap API, you need to obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys). Once you have the API key, place it in the `.env` file as follows:


Set the API KEY in the .env file as 
```
API_KEY=<Your API KEY>
```

## RUN PRIOJECT

1. Open the main.py file located in the src folder.

2. Configure the following settings according to your preferences:

    - Set the `CITY` variable to specify the city for temperature monitoring:
        ```
        CITY: str = 'Indore'
        ```

    - Define the `MIN_TEMP` and `MAX_TEMP` values to set the desired temperature thresholds:
        ```
        MIN_TEMP: float = 26.0
        MAX_TEMP: float = 35.0
        ```

    - Use the `NOTIFICATION` flag to control whether notifications are displayed (`True`) or not (`False`):
        ```
        NOTIFICATION: bool = True 
        ```

    d. Specify the `FILENAME` where you want to save the log data:
        ```
        FILENAME: str = './data.txt'
        ```

3. Open comandprompt or Terminial and be in the parent folder `./`

    - Run the command below, which will install all dependencies required by this project:

    Install `poetry` (If not alreadey installed)
    ```
    pip install poetry
    ```  

    open the `poetry shell` by running the following command
    ```
    poetry shell
    ```

    Install all the requriments 
    
    `NOTE: ` Make sure you are in the directory where `pyproject.toml` file is present
    ```
    poetry install
    ```


4. Run the project by typing

    chang the directory to `./src` or locate `main.py` and open `poetry shell` there 

    ```
    python main.py
    ```

## Things to remember
- Make sure you have turned on yout notifications in your system

- If you're running the program in an environment where notifications can't be shown, set `NOTIFICATION` to False in the main.py file.

    ```
    NOTIFICATION: bool = True 
    ```

- Ensure that your machine is connected to the internet for the API to function properly.

Follow these steps, and your project should run successfully, monitoring temperature based on your configured settings.

