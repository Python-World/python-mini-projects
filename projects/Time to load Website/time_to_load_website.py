from urllib.request import urlopen
import time


def get_load_time(url):
    """This function takes a user defined url as input
    and returns the time taken to load that url in seconds.

    Args:
        url (string): The user defined url.

    Returns:
        time_to_load (float): The time taken to load the website in seconds.
    """

    if ("https" or "http") in url:  # Checking for presence of protocols
        open_this_url = urlopen(url)  # Open the url as entered by the user
    else:
        open_this_url = urlopen("https://" + url)  # Adding https to the url
    start_time = time.time()  # Time stamp before the reading of url starts
    open_this_url.read()  # Reading the user defined url
    end_time = time.time()  # Time stamp after the reading of the url
    open_this_url.close()  # Closing the instance of the urlopen object
    time_to_load = end_time - start_time

    return time_to_load


if __name__ == '__main__':
    url = input("Enter the url whose loading time you want to check: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.")
