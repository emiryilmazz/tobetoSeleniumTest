HTML Locators Özet

HTML locators, web sayfalarındaki öğeleri bulmak ve onlarla etkileşim kurmak için kullanılan önemli bir araçtır. Doğru locator'ı seçmek ve kullanmak, test senaryolarınızın başarısı için önemlidir.Farklı türde locators'lar mevcuttur ve her birinin kendine özgü avantajları ve dezavantajları vardır.

Selenium, web tarayıcılarını otomatikleştirmek için kullanılan bir açık kaynak kodlu araçtır. Web sayfalarındaki öğeleri bulmak ve onlarla etkileşim kurmak için HTML locators'ları kullanır.

***Locator Türleri***

ID: Her HTML öğesi için benzersiz bir kimlik tanımlayıcısıdır. En hızlı ve en güvenilir locator türüdür.
Class: Bir veya birden fazla HTML öğesine atanabilir. Birden fazla öğeyi bulmak için kullanılabilir.
Name: Form elementleri için kullanılır.
CSS Selector: CSS seçicileri kullanarak öğeleri seçmenizi sağlar. Karmaşık elementleri bulmak için idealdir.
XPath: Karmaşık elementleri ve XML belgelerini bulmak için kullanılır.
***Locator Seçimi***
Locator'lar, web otomasyon testlerinde çok önemli bir rol oynar. Doğru locator'ları seçmek ve kullanmak, test senaryolarınızın daha hızlı ve daha güvenilir bir şekilde çalışmasını sağlayabilir.
Doğru locator'ı seçmek, test senaryolarınızın başarısı için önemlidir. Bir locator seçerken aşağıdakileri göz önünde bulundurun:

Locator, aradığınız öğenin türüne uygun olmalıdır.
Locator, aradığınız öğeyi benzersiz bir şekilde tanımlamalıdır.
Locator'ın güncellenmesi ve bakımı kolay olmalıdır.

***Locator Örnekleri***

#element_id (ID locator)
.element_class (Class locator)
input[name="username"] (Name locator)
div.container h1 (CSS selector)
//div[@id="main-content"]//p (XPath locator)

By CSS ID: find_element_by_id
By CSS class name: find_element_by_class_name
By name attribute: find_element_by_name
By DOM structure or Xpath: find_element_by_xpath
by tagName: find_element_by_tag_name()
By link text: find_element_by_link_text
By partial link text: find_element_by_partial_link_text
By HTML tag name: find_element_by_tag_name

Locators'lar, sadece web sayfalarındaki öğeleri bulmak için değil, aynı zamanda onlarla etkileşim kurmak için de kullanılabilir. Örneğin, bir butona tıklamak veya bir metin kutusuna metin girmek için locator'lar kullanılabilir.

***Locator'ları Kullanma***

Locator'lar, Selenium WebDriver gibi web otomasyon araçları tarafından web sayfalarındaki öğeleri bulmak ve onlarla etkileşim kurmak için kullanılır. 

***ÖRNEK***
Python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

username_field.send_keys("kullanıcı_adı")
password_field.send_keys("şifre")

login_button = driver.find_element_by_id("login_button")
login_button.click()

***Locator'ları Kullanırken Dikkat Edilmesi Gerekenler***

Locator'lar, web sayfasındaki HTML koduna bağlıdır. HTML kodunda bir değişiklik olursa, locator'lar da güncellenmelidir.
Locator'lar, seçilen öğenin türüne ve özelliklerine göre seçilmelidir.
Locator'lar, mümkün olduğunca basit ve anlaşılır olmalıdır.

***Selenium ile HTML Locators Kullanmanın Avantajları***

Test senaryolarını daha hızlı ve daha kolay yazmanıza yardımcı olur.
Test senaryolarınızı daha güvenilir hale getirir.
Web sayfalarındaki değişikliklere karşı test senaryolarınızı daha uyumlu hale getirir.

***Selenium ile HTML Locators Kullanmanın Dezavantajları***

Locator'lar, web sayfasındaki HTML koduna bağlıdır. HTML kodunda bir değişiklik olursa, locator'lar da güncellenmelidir.
Locator'lar, seçilen öğenin türüne ve özelliklerine göre seçilmelidir.
