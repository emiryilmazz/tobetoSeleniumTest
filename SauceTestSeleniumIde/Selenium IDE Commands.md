Selenium IDE Commands

Selenium IDE komutları, web tarayıcılarını otomatikleştirmek için kullanılır. Bu komutlar, web sayfalarında gezinmenizi, formları doldurmanızı ve diğer eylemleri gerçekleştirmenizi sağlar.

Selenium IDE’de test senaryoları oluşturan komutlara Selenese komutları adı verilir. Selenese, Selenium WebDriver’ı kullanmayı kolaylaştırmak için kullanılan bir komut dosyası dilidir. Selenese komutları, web sayfalarında gezinmek, formları doldurmak ve diğer eylemleri gerçekleştirmek için kullanılabilir.

Selenium IDE komutları 3 kategoriye ayrılır:


1- Eylem Komutları:
Selenium IDE, web uygulamalarını test etmek için kullanılan bir otomasyon aracıdır. Kullanıcıların web tarayıcısında etkileşimli olarak kaydettikleri aksiyonları otomatikleştirmelerine ve bu etkileşimleri test senaryolarına dönüştürmelerine olanak sağlar. Bu komutlar, testin adımlarını belirtir ve Selenium WebDriver gibi diğer Selenium araçlarına benzer şekilde çalışırlar.

Eylem komutları, bir web uygulamasında kullanıcı tarafından gerçekleştirilen eylemleri taklit eder. Selenium IDE'de birçok eylem komutu mevcuttur, ancak en sık kullanılanlardan birkaçı şunlardır:

1-Tıklama (Click):
-Belirtilen öğeye fare ile tıklama işlemini simüle eder.
-Parametreler:
 -locator: Tıklanacak öğenin seçicisi.
 -offsetX: Tıklamanın öğenin sol kenarından ne kadar uzakta gerçekleşeceğini belirtir.
 -offsetY: Tıklamanın öğenin üst kenarından ne kadar uzakta gerçekleşeceğini belirtir.

2-Metin Gönderme (SendKeys):
-Belirtilen öğeye metin girer.
-Parametreler:
 -locator: Metnin girileceği öğenin seçicisi.
 -text: Gönderilecek metin.

3-Seçim Yapma (Select):
-Bir açılır listeden bir öğe seçer.
-Parametreler:
 -locator: Açılır listenin seçicisi.
 -option: Seçilecek öğenin metni veya değeri.

4-İşaretleme (Check):
-Bir onay kutusunu işaretler.
-Parametreler:
 -locator: Onay kutusunun seçicisi.

5-İşaretini Kaldırma (Uncheck):
-Bir onay kutusunun işaretini kaldırır.
-Parametreler:
 -locator: Onay kutusunun seçicisi.

6-Form Gönderme (Submit):
-Bir formu gönderir.
-Parametreler:
 -locator: Gönderilecek formun seçicisi.


Diğer Eylem Komutları:
-add selection: Bir liste kutusuna seçenek ekler.
-answer on next prompt: Bir sonraki giriş iletişim kutusuna cevap verir.
-assert: Bir öğenin belirli bir özelliğe sahip olduğunu doğrular.
-choose ok on next confirmation: Bir sonraki onay iletişim kutusunu kabul eder.
-choose cancel on next confirmation: Bir sonraki onay iletişim kutusunu iptal eder.
-choose cancel on next prompt: Bir sonraki giriş iletişim kutusunu iptal eder.
-clear: Bir metin girişini temizler.
-click: Bir elemente fare tıklamasını simüle eder.
-click at: Belirli bir konumda fare tıklamasını simüle eder.
-close: Geçerli pencereyi kapatır.
-double click: Bir elemente çift tıklamayı simüle eder.
-double click at: Belirli bir konumda çift tıklamayı simüle eder.
-drag and drop to object: Bir elementi sürükler ve başka bir elemente bırakır.
-debugger: JavaScript kodunu hata ayıklamak için bir noktaya ara ekler.
-do: Belirli bir bloğu belirli bir koşula göre yürütür.
-echo: Bir mesajı loga veya konsola yazdırır.
-edit content: Bir elementin içeriğini düzenler.
-end: Bir döngü veya koşullu ifadenin sonunu belirtir.
-execute async script: Asenkron JavaScript kodunu yürütür.
-mouse down: Fare düğmesini basılı tutar.
-mouse down at: Belirli bir konumda fare düğmesini basılı tutar.
-mouse move at: Belirli bir konumda fareyi hareket ettirir.
-mouse out: Fareyi bir elementin üzerinden çıkarır.
-mouse over: Fareyi bir elementin üzerine getirir.
-mouse up: Fare düğmesini bırakır.
-mouse up at: Belirli bir konumda fare düğmesini bırakır.
-open: Bir URL’yi açar.
-pause: Belirtilen süre kadar bekler.
-remove selection: Bir listeden seçimi kaldırır.
-repeat if: Belirli bir koşula göre belirli bir bloğu tekrarlar.
-run: Bir test senaryosunu yürütür.
-run script: JavaScript kodunu yürütür.
-select frame: Bir frame içine geçer.
-select window: Bir pencereyi seçer.
-set speed: Komut hızını ayarlar.
-set window size: Pencere boyutunu ayarlar.
-store attribute: Bir elementin özniteliğini saklar.
-store json: JSON verisini saklar.
-store text: Bir elementin metnini saklar.
-store title: Sayfa başlığını saklar.
-store value: Bir elementin değerini saklar.
-store window handle: Pencere tanımlayıcısını saklar.
-store xpath count: XPath ifadesinin sayısını saklar.
-type: Bir metin kutusuna metin yazar.
-uncheck: Bir onay kutusunun işaretini kaldırır.
-verify: Bir öğenin belirli bir özelliğe sahip olduğunu doğrular ve hata oluşursa testi durdurur.


Bekleme ve Görünürlük Komutları:
-wait for text: Belirli bir metni bekler.
-wait for element editable: Bir elementin düzenlenebilir olmasını bekler.
-wait for element not editable: Bir elementin düzenlenebilir olmamasını bekler.
-wait for element present: Bir elementin varlığını bekler.
-wait for element not present: Bir elementin var olmamasını bekler.
-wait for element visible: Bir elementin görünür olmasını bekler.
-wait for element not visible: Bir elementin görünür olmamasını bekler.


2 - Doğrulama Komutları:
Selenium IDE, web uygulamalarını otomatik olarak test etmek için kullanılan bir araçtır. Doğrulama komutları, test edilen uygulamanın beklenen şekilde çalışıp çalışmadığını kontrol etmek için kullanılır. Bu komutlar, test senaryolarına eklenerek testin sağlamlığını ve güvenilirliğini artırır.

Selenium IDE'de sık kullanılan doğrulama komutları:

Verification Commands(Doğrulama Komutları):
1-assert: Belirli bir koşulun doğru olduğunu doğrular. Koşul doğru değilse, test başarısız olur ve bir hata mesajı görüntülenir.
2-verify: Assert'e benzer, ancak koşul doğru değilse bile test yürütmesine devam eder. Bu, testin hangi aşamada hata oluştuğunu belirlemek için kullanılabilir.
3-verify title: Sayfa başlığını doğrular. Başlık beklenenle aynı değilse, test başarısız olur.
4-verify selected label: Seçili bir açılır menü etiketini doğrular. Etiket beklenenle aynı değilse, test başarısız olur.
5-verify checked: Bir onay kutusunun veya radyo düğmesinin seçili olduğunu doğrular. Seçim beklenenle aynı değilse, test başarısız olur.
6-verify not checked: Bir onay kutusunun veya radyo düğmesinin seçili olmadığını doğrular. Seçim beklenenle aynı değilse, test başarısız olur.
7-verify editable: Bir elementin düzenlenebilir olduğunu doğrular. Element düzenlenebilir değilse, test başarısız olur.
8-verify not editable: Bir elementin düzenlenebilir olmadığını doğrular. Element düzenlenebilirse, test başarısız olur.
9-verify element present: Bir elementin varlığını doğrular. Element mevcut değilse, test başarısız olur.
10-verify element not present: Bir elementin var olmadığını doğrular. Element mevcutsa, test başarısız olur.
11-verify value: Bir elementin değerini doğrular. Değer beklenenle aynı değilse, test başarısız olur.
12-verify selected value: Bir açılır menüde belirli bir değerin seçildiğini doğrular. Değer seçili değilse, test başarısız olur.
13-verify not selected value: Bir açılır menüde belirli bir değerin seçilmediğini doğrular. Değer seçiliyse, test başarısız olur.
14-verify text: Bir elementin metnini doğrular. Metin beklenenle aynı değilse, test başarısız olur.
15-verify not text: Bir elementin metninin belirli bir değer olmadığını doğrular. Metin beklenmedik değere sahipse, test başarısız olur.

Assertions(Doğrulamalar):
1-assert alert: Bir uyarının varlığını doğrular.
2-assert confirmation: Bir onay iletişim kutusunun varlığını doğrular.
3-assert prompt: Bir giriş iletişim kutusunun varlığını doğrular.
4-assert selected label: Bir açılır menüde belirli bir seçeneğin etiketle seçildiğini doğrular.
5-assert title: Geçerli sayfanın başlığını doğrular.
6-assert value: Bir elementin değerini doğrular.
7-assert selected value: Bir açılır menüde belirli bir değerin seçildiğini doğrular.
8-assert not selected value: Bir açılır menüde belirli bir değerin seçilmediğini doğrular.
9-assert checked: Bir onay kutusunun veya radyo düğmesinin seçili olduğunu doğrular.
10-assert not checked: Bir onay kutusunun veya radyo düğmesinin seçili olmadığını doğrular.
11-assert editable: Bir elementin düzenlenebilir olduğunu doğrular.
12-assert not editable: Bir elementin düzenlenebilir olmadığını doğrular.
13-assert element present: Bir elementin varlığını doğrular.
14-assert element not present: Bir elementin var olmadığını doğrular.
15-assert text: Bir elementin metnini doğrular.
16-assert not text: Bir elementin metninin belirli bir değer olmadığını doğrular.


Doğrulama komutlarını kullanırken dikkat edilmesi gerekenler:
-Doğrulama komutları, test edilen uygulamanın beklenen davranışını doğru şekilde yansıtmalıdır.
-Doğrulama komutlarının parametreleri doğru şekilde belirtilmelidir.
-Doğrulama komutları, test senaryosunun akışına uygun şekilde yerleştirilmelidir.


Doğrulama komutları ile ilgili örnekler:

assert elementPresent("id=username")
verify title "Hesap Oluştur"
verify selectedLabel "Seçiniz..."
verify checked "id=rememberMe"
verify not checked "id=newsletter"
verify editable "id=password"
verify not editable "id=email"
verify value "id=firstName" "John"
verify selectedValue "id=country" "TR"
verify not selectedValue "id=country" "US"
verify text "Hesap başarıyla oluşturuldu!"
verify not text "Hesap oluşturulamadı!"


3 - Akış Kontrol Komutları:
Selenium IDE Akış Kontrol Komutları
Selenium IDE, web tarayıcılarında otomatik testler oluşturmak için kullanılan bir araçtır. Test senaryolarını oluşturmak için sürükle ve bırak yöntemini kullanır ve komutları bir araya getirerek test akışını kontrol etmenizi sağlar.

Selenium IDE'de akış kontrolünü sağlayan 4 temel komut vardır:


1-If Komutu:
Bu komut, belirli bir koşulun doğru olup olmadığını kontrol eder ve koşulun sonucuna göre farklı test adımlarını yürütmenizi sağlar.

Kullanım:
-Koşul: Testin devam etmesi için gereken koşulu girin.
-Doğru: Koşul doğruysa yürütülecek test adımlarını ekleyin.
-Yanlış: Koşul yanlışsa yürütülecek test adımlarını ekleyin.

Örnek:
if (element.is_visible()) {
  click(element)
} else {
  log("Element görünür değil")
}


2-Else If Komutu:
Bir if komutunun ardından birden fazla else if komutu kullanarak birden fazla koşulu kontrol edebilirsiniz.

Kullanım:
-Koşul: Her else if komutu için testin devam etmesi için gereken koşulu girin.
-Doğru: Koşul doğruysa yürütülecek test adımlarını ekleyin.

Örnek:
if (element.is_enabled()) {
  click(element)
} else if (element.is_visible()) {
  log("Element tıklanabilir değil, ancak görünür")
} else {
  log("Element tıklanabilir veya görünür değil")
}


3-Switch Case Komutu:
Bir değişkenin değerine göre farklı test adımlarını yürütmenizi sağlar.

Kullanım:
-Değişken: Testin değerini kontrol edeceğiniz değişkeni seçin.
-Case: Her case için değişkenin olası değerlerini girin.
-Doğru: Her case için değişkenin o değere sahip olması durumunda yürütülecek test adımlarını ekleyin.

Örnek:
switch (element.text) {
  case "Başarılı":
    log("Test başarılı")
    break
  case "Başarısız":
    log("Test başarısız")
    break
  default:
    log("Beklenmedik durum")
}


4-While Döngüsü:
Belirli bir koşul doğru olduğu sürece bir test adımını veya bir grup test adımını tekrarlamanızı sağlar.

Kullanım:
-Koşul: Döngünün devam etmesi için gereken koşulu girin.
-Doğru: Koşul doğru olduğu sürece tekrarlanacak test adımlarını ekleyin.

Örnek:
while (element.is_not_visible()) {
  wait(1000)
}

click(element)


Selenium IDE'de komutları kullanmak için:
1.Selenium IDE'yi açın ve yeni bir test dosyası oluşturun.
2.Komut menüsünden istediğiniz komutu seçin.
3.Komutun parametrelerini girin.
4.Komutu test dosyasına ekleyin.
5.Test senaryonuzu çalıştırın.