
#the code is hosted on github.com/engineervinay if you wanted to make development in code visit profile and fork the code
#if you have any query related to this code you can contact me on github @engineervinay



from selenium.webdriver.common.keys import Keys #importing keys from selenium to enter the comments

from time import sleep #time library for sleepcommand

from random import randint #library to provide random integer values between range

from selenium import webdriver #the library for accesing chrome by our code


#window to accept inputs username, password, and hashtags
print("enter username:-")
user=input()
passw=input("enter password:-")
print("enter hashtags seperated by , :-")
hash=input()


# Change this to your own chromedriver path!
chromedriver_path = 'C:/Users/Vinay/Downloads/chromedriver_win32/chromedriver.exe' 
webdriver = wb.Chrome(executable_path=chromedriver_path)

sleep(2)
#opening instagram login page.
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(3)



username = webdriver.find_element_by_name('username')#finding username inputbox

username.send_keys(user)#passing username.

password = webdriver.find_element_by_name('password')
password.send_keys(passw)


#finding login button 
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child() > button')
#clicking on button 
button_login.click()

sleep(3)


#clicking on not now button which occurs when we logged in
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')

notnow.click()



hashtag_list1=hash.split(",")
for hashtag in hashtag_list1:

    sleep(5)
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

    sleep(5)

    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    first_thumbnail.click()

    sleep(randint(1, 2))



    for x in range(1, 200):

            #username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            #if username not in prev_user_list:
            # If we already follow, do not unfollow

            #if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

            #webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

            #new_followed.append(username)

            #followed += 1

            # Liking the picture
        sleep(randint(3,7))
        #finding the like button using xpath
        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

        button_like.click()#cliking on founded like button to like photo 

        comm_prob =randint(1,4)
        #to enable commenting box
        webdriver.find_element_by_xpath('/html/body/div[]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
        #clicking on comment box
        comment_box = webdriver.find_element_by_xpath('/html/body/div[]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
        sleep(randint(3,7))
        #code to post random comments
        if comm_prob == 1:   
            #this statement will send the comment to the comment box
            comment_box.send_keys('Really cool!')
            sleep(5)

        elif comm_prob == 2:

            comment_box.send_keys('Nice work :)')

            sleep(5)

        elif comm_prob == 3:

            comment_box.send_keys('Nice gallery!!')

            sleep(5)

        elif comm_prob == 4:

            comment_box.send_keys('So cool! :)')

            sleep(5)

                
        sleep(randint(4,6))
        comment_box.send_keys(Keys.ENTER)# Enter to post comment
        sleep(randint(22, 28))

        webdriver.find_element_by_link_text('Next').click()#clicking on next for next photo

        sleep(randint(25, 29))

###Developed by vinay patil



