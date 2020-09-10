# Website Summarization API

This project is carried out for the purpose of building a machine learning model for summarising a website from urls;

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Python distribution

```
Anaconda
```

### Installing

Install Anaconda python distribution on your system

Create a virtual environment called env.

```
python -m venv app
```

Activate the virtual environment

```
LINUX/Mac: source app/bin/activate

Windows: app\Scripts\activate
```

Upgrade to the latest pip

```
pip install --upgrade pip
```

Install dependencies using requirements file

```
pip install -r requirements.txt
``` 
**Note: Your virtual environment must always be activated before running any command**

## Deployment

Start app (Make sure to enter a valid website to an existing website)


Example of valid commands

```
python app.py simple --url https://facebook.com --sentence 1 --language english
python app.py simple --url https://facebook.com 
python app.py simple --url https://korapay.com
python app.py bulk --path ./csv/valid_websites.csv
```


### APIs

This are command options in full:

```
A command line utility for website Summarization.
-----------------------------------------------
These are common commands for this app.

positional arguments:
  action            This has to be 'summarize'

optional arguments:
  -h, --help            show this help message and exit
  --website PATH        website of the url to be summarised


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details

