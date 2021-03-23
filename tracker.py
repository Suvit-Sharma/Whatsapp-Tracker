from selenium import webdriver
import time
import datetime
from selenium.common.exceptions import NoSuchElementException


date_for_file = datetime.datetime.now()
victim = input("please enter correct name whose online status you want to \ntrack as saved in your contacts : ")
file_name = input("Please Enter a File Name To Save Data : ")
file_dir = file_name + "-" + str(date_for_file.year) + "-" + str(date_for_file.strftime("%A")) + "-" + str(date_for_file.strftime("%H")) + "-" + str(date_for_file.strftime("%M")) + "-" + str(date_for_file.strftime("%S"))
print("Your file will be saved in directory in which this app resides, \nby name : " + file_dir + ".txt")
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\PycharmProjects\\Whatsapp_Tracker\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


print("finding user, please wait for some time..... ")

time.sleep(15)
update_timer = 200

while not check_exists_by_xpath("//span[@title='{}']".format(victim)):
    driver.execute_script("document.getElementById('pane-side').scrollTo(0," + str(update_timer) + ")")
    update_timer = int(update_timer) + 150
    time.sleep(0.3)


driver.find_element_by_xpath("//span[@title='{}']".format(victim)).click()


print("now recording .....")

session = 0
time.sleep(3)
while True:
    stateString = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header").text
    if "online" in stateString:
        session += 1
        online_from = datetime.datetime.now()
        online_start_time = time.time()
        while "online" in stateString:
            stateString = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header").text
            pass

        online_end_time = time.time()
        online_to = datetime.datetime.now()
        # Opening file goes here
        file1 = open(file_dir + ".txt", "a")
        data = ["Session : " + str(session) + "\n",
                "online from :" + str(online_from) + "\n",
                "For Duration : " + str(round(online_end_time-online_start_time)) + " Seconds" + "\n",
                "Went offline at : " + str(online_to) + "\n",
                "\n===X===X===X===X===X===X===\n"]
        file1.writelines(data)
        file1.close()
        print("Session : " + str(session))
        print("online from :" + str(online_from))
        print("For Duration : " + str(round(online_end_time-online_start_time)) + " Seconds")
        print("Went offline at : " + str(online_to))
        print("===X===X===X===X===X===X===")


