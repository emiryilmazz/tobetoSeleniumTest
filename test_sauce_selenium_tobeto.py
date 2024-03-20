from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
sleep(2)

class Test_Sauce: 
    def test_invalid_login(self):  
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        #print(errorMessage.text)
        testResult = errorMessage.text == "ERROR!!! Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

#Case 1     
#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
        
    def test_null_value(self):
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required uyarı mesajı gösterilmiştir = {testResult}")
        sleep(2)
#Case 2
#-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def test_null_password(self):
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required uyarı mesajı gösterilmiştir = {testResult}")
        sleep(2)
#case 3
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_user_locked(self):
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. uyarı mesajı gösterilmiştir = {testResult}")
        sleep(3)
#case 4
#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_products_list(self):
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(productList)} adettir.")
        sleep(3)    


testClass = Test_Sauce()
testClass.test_products_list()
#testClass.test_user_locked()
# testClass.test_null_password()
# testClass.test_null_value()
# testClass.test_invalid_login()

