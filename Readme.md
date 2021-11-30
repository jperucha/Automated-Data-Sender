# Automated data sender over REST

clean_data.py helps preparing the file to be a valid JSON that could be send.
send_data.py reads the file passed as parameter and sends all the content grouped by the number of MAX_DATA_ROWS_OVER_PETITIONS configured with a POST to the 

## How to run it

To use Pipfile pipenv is required, it could be installed with:
> brew install pipenv

To install Pipfile dependencies execute
> pipenv install

Another way to do it could be using an IDE like IntelliJ and setting the Python SDK >=3.6 to execute the code
Also any Python >=3.6 venv could be used to execute it 

## Configure

Add the value of URL and AUTH_TOKEN variables
Change the name/path of the file to clean or send
