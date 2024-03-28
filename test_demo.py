from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

class Test_Demo:
    #pytest tarafından tanımlanan bir method 
    #her test öncesi otomatik olarak çalıştırılır
    def setup_method(self):
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")  
        return driver

    
    def teardown_method(self):
        driver = self.setup_method()
        driver.quit()

    @pytest.mark.skip #tüm testler koşulurken "skip" şeklinde işaretlenen testlerimi atla
    def test_demo(self):
        print("x")
        text = "Hello"
        assert text == "Hello"

    def getData():
        return [("1","1"),("locked_out_user","secret_sauce"),("standard_user","secret_sauce")]
    
    def test_null_value(self):
        driver = self.setup_method()
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Username is required"
        print(f"Epic sadface: Username is required şeklinde uyarı mesajı gösterilmiştir = {testResult}")

    @pytest.mark.parametrize("username",getData())
    def test_null_password(self,username):
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput.send_keys(username)
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage =driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required şeklinde bir uyarı mesajı gösterilmiştir = {testResult}")

    @pytest.mark.parametrize("username,password",getData())
    def test_user_locked(self,username,password):
        if username != "locked_out_user" or password != "secret_sauce":
            pytest.skip()
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. şeklinde uyarı mesajı gösterilmiştir = {testResult}")


    @pytest.mark.parametrize("username,password",getData())
    def test_invalid_login(self,username,password):
        if username != "1" or password != "1":
            pytest.skip()
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage =WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Epic sadface: Username and password do not match any user in this service uyarı mesajı verildi: {testResult}")
        # assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_valid_login(self):
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #depoladığım aksiyonları çalıştır
        loginButton = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        baslik =WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        assert baslik.text == "Swag Labs"

    def test_products_list3(self):
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #depoladığım aksiyonları çalıştır
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        urunEkle = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        urunEkle1 = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesie']")))
        driver.execute_script("window.scrollTo(0,500)")
        urunEkle.click()
        urunEkle1.click()
        sleep(2)
        sepet = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        actions.click(sepet).perform()
        remove = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        actions.click(remove)
        checkout = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"checkout")))
        actions.click(checkout)
        actions.perform()
        firstName = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        lastName = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        zipCode = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        continueBtn = WebDriverWait(driver,2).until(ec.visibility_of_element_located((By.ID,"continue")))
        actions.send_keys_to_element(firstName,"Emir")
        actions.send_keys_to_element(lastName,"Yılmaz")
        actions.send_keys_to_element(zipCode,"41400")
        actions.click(continueBtn)
        actions.perform()
        finish = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.ID,"finish")))
        actions.click(finish).perform()
        sleep(2)
        baslik = WebDriverWait(driver,4).until(ec.visibility_of_element_located((By.CLASS_NAME,"complete-header")))
        testResult = baslik.text == "Thank you for your order!"
        print(f"Ödeme işlemi başarılı: {testResult}")

    def test_dropDown(self):
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions.click(loginButton)
        actions.perform() #depoladığım aksiyonları çalıştır
        #sıralam listesine tıklama
        dropDown = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        actions.click(dropDown)
        actions.perform()
        sleep(3)
        #sıralama listesinden indexe göre seçim yapma
        secme = WebDriverWait(driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        sleep(1)
        select = Select(secme)
        select.select_by_index(3)
        # select.select_by_visible_text("Price (high to low)")
        # select.select_by_value("hilo")
        sleep(2)
    def test_menu(self):
        driver = self.setup_method()
        userNameInput = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        loginButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions.click(loginButton)
        actions.perform()
        menuButton = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        actions.click(menuButton).perform()
        aboutLink = WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,"about_sidebar_link")))
        actions.click(aboutLink).perform()
        assert "saucelabs" in driver.current_url, "Yanlış sayfadasın."
        print("Sauce Labs Sayfası açıldı.")
        sleep(2)

    



        