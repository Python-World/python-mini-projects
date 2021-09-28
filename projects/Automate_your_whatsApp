# Automate-your-whatsapp
Using this selenium code you can automate your whatsApp easily and it is vey awesome must try it
You just need to do three thing before executitng this code
1. Download ChromeDriver.exe file to control your chrome go int this given link to donwlaod chromeDriver ==> https://chromedriver.chromium.org/downloads

2. And just setup web.whatsapp.com, You need to remember this things that you have to login every time when you excute this code
3. And last thing in this code may be you span-path and send-button-path are diffrent fix by trying to execute and help of error
4. And enjoy your code. It really Works. 


#Code
------------------------------------

    #Imporiting esential modules for this code

    import time
    from selenium import  webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    #setup up driver or drive code

    driver = webdriver.Chrome("D:\\main\\Imp soft\\Softwares\\chromedriver_win32 (1)\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://web.whatsapp.com/")


    #main function to automate you whatsapp
    def msg():
        name = input('\nEnter user name: ')
        message = input("Enter your message to group/user")
        count = int(input("Enter the message to count: "))

        #find who to message
        user = driver.find_element_by_xpath(
            '//span[@title="{}"]'.format(name)
            )

        user.click()

        text_box = driver.find_element_by_class_name('p3_M1')

        #send button
        for i in range(count):
            text_box.send_keys(message)
            driver.find_element_by_class_name('_4sWnG').click()

    def reps():
        print("DO you want to send more msg to anyone")
        aksUSer = input("Press Y for Yes and N for No: ")
        if (aksUSer == 'Y' or aksUSer == 'y'):
            msg()
            reps()
        elif (aksUSer=='N' or aksUSer=='n'):
            print("Thank you see you soon")
        else:
            print("please eneter valid options: \n")
            reps()


    #calling funtions
    msg()
    reps()
