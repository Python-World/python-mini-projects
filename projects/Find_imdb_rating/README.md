# Find IMDB Ratings 
<!--Remove the below lines and add yours -->
This script is used to fetch the Ratings and Genre of the films in your films folder that match with ones on IMDb, the data is scraped from IMDB's official website and store in a csv file. The csv file can be used for analysis then, sorting acc to rating etc. 

Input: -> Path of the directory which contains the films. 

Output: -> A new csv file is made - 'film_ratings.csv' which contains the ratings for the films in your directory. 

### Prerequisites
<!--Remove the below lines and add yours -->
This program uses and external dependency of 'BeautifulSoup' (for web scraping), 'requests' (for fetching content of the webpage), 'pandas' (to make the csv file), 'os' (to get data from directory). <br>
These libraries can be installed easily by using the following command: pip install -r requirements.txt

### How to run the script
<!--Remove the below lines and add yours -->
-> Install the requirements. <br>
-> Inside the find_IMDb_rating.py, update the directory path. <br>
-> Type the following command: python find_IMDb_rating.py <br>
-> A csv file with rating will be created in the same directory as the python file. <br>

### Screenshot/GIF showing the sample use of the script
<!--Remove the below lines and add yours -->
Folder :

![Screenshot 2020-09-15 at 6 20 55 PM](https://user-images.githubusercontent.com/44445191/93214776-375f7280-f783-11ea-90a3-dcd29a84d7fc.png)

CSV File:
![Screenshot 2020-09-15 at 6 28 24 PM](https://user-images.githubusercontent.com/44445191/93214767-32022800-f783-11ea-893d-7f45240b6dc5.png)


## *Author Name*
<!--Remove the below lines and add yours -->
[Utkarsh Bajaj](https://github.com/utkarshbajaj)
