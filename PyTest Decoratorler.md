-PyTest Decoratorleri-

PyTest ,Python programları için bir test çerçevesidir. Yazılım projelerinde testlerin yazılması ve çalıştırılması için kullanılır.
PyTest, basit test senaryolarından karmaşık test süitlerine kadar çeşitli testleri destekler.
Decoratorler, pytest test çerçevesini daha esnek ve güçlü kılan özelliklerden sadece birkaç tanesidir.
Her decoratorün belirli bir kullanım amacı vardır ve belirli durumlar için test yazımını kolaylaştırmak için tasarlanmıştır.

PyTest Decoratorleri Kullanmanın Faydaları:

-Test kodunuzu daha organize ve okunabilir hale getirir.
-Testlerinizin tekrarlanabilir ve bağımsız olmasını sağlar.
-Hataları ve uyarıları daha kolay tespit etmenize yardımcı olur.
-Test kodunuzun kapsamını ve karmaşıklığını azaltır.


En Yaygın Kullanılan Decoratorler:



1. @pytest.fixture: Bu decorator, test fonksiyonları tarafından kullanılabilecek geçici kaynaklar oluşturmak için kullanılır. 
Fixture'lar, testlerinizin tekrarlanabilir ve bağımsız olmasını sağlar.

---Örnek olarak---

import pytest

@pytest.fixture
def my_user(request):
  """Bu fonksiyon her test fonksiyonundan önce çalıştırılır ve bir kullanıcı nesnesi oluşturur."""
  username = request.config.getoption("username")
  password = request.config.getoption("password")
  return User(username, password)

def test_login(my_user):
  """Bu test fonksiyonu my_user fonksiyonunun oluşturduğu kullanıcı nesnesini kullanır."""
  assert my_user.login() is True


@pytest.fixture Faydaları:
-Test kodunu daha modüler ve okunabilir hale getirir.
-Test verilerini ve test ortamını yönetmek için kullanılabilir.
-Tekrar eden kodları ortadan kaldırır.



2. @pytest.mark.parametrize: Bir test fonksiyonunun birden fazla veri seti ile çalıştırılmasını sağlayan bir dekoratördür. 
Bu sayede, her veri seti için ayrı bir test fonksiyonu yazmaya gerek kalmadan, aynı fonksiyonu farklı parametrelerle tekrar tekrar çalıştırabilirsiniz.

---Örnek olarak---

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (7, 8, 15),
])
def test_add(x, y, expected):
    assert x + y == expected

Açıklama:

Bu örnekte, test_add fonksiyonu üç kez çalıştırılacaktır. Her çalıştırmada, x ve y parametreleri @pytest.mark.parametrize dekoratöründe belirtilen veri setlerinden birer değer alacaktır.
Fonksiyonun beklenen sonucu, expected parametresi ile belirtilir. Test, fonksiyonun çıktısının expected ile eşit olup olmadığını kontrol eder.
@pytest.mark.parametrize dekoratörünün kullanımı, test kodunuzu daha kısa ve daha okunabilir hale getirir. Ayrıca, farklı veri setleri ile test yapmak, kodunuzun daha sağlam olmasını sağlar.

Ekstra:
@pytest.mark.parametrize dekoratörü, sadece test fonksiyonları için değil, fixture fonksiyonları için de kullanılabilir.
@pytest.mark.parametrize dekoratörünün ids parametresi ile her test çalıştırması için özel bir ad belirtebilirsiniz.
@pytest.mark.parametrize dekoratörünün indirect=True parametresi ile fixture fonksiyonlarının dolaylı olarak kullanılmasını sağlayabilirsiniz.



3. @pytest.mark.skip: Belirli testlerin belirli koşullar altında atlanmasını sağlayan bir pytest dekoratörüdür. 
Bu dekoratör, test kodunu çalıştırmadan atlama işlemini gerçekleştirdiği için test süresini kısaltmaya yardımcı olur.

---Örnek olarak---

import pytest

@pytest.mark.skip
def test_skip_this_test():
    assert False, "Bu test atlandı."

def test_run_this_test():
    assert True, "Bu test çalıştırıldı."

Açıklama:

Bu kodda, test_skip_this_test fonksiyonu @pytest.mark.skip dekoratörü ile işaretlenmiştir. 
Bu nedenle, bu test fonksiyonu çalıştırılmadan atlandı. test_run_this_test fonksiyonu ise normal şekilde çalıştırılır ve assert ifadesi doğrulanır.

@pytest.mark.skip dekoratörünü kullanmanın birkaç farklı yolu vardır:

-Dekoratörü test fonksiyonunun önüne eklemek:

@pytest.mark.skip
def test_skip_this_test():
    ...

-Dekoratöre bir reason argümanı eklemek:

@pytest.mark.skip(reason="Bu test henüz tamamlanmadı.")
def test_skip_this_test():
    ...

-Dekoratörü bir condition argümanı ile kullanmak:

import sys

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Python 3.8 veya üzeri gerekli.")
def test_skip_this_test():
    ...


--Ek Örnekler--

-Belirli bir işletim sistemi için testi atlamak:

import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Bu test sadece Linux için geçerlidir.")
def test_skip_this_test():
    ...

-Belirli bir kütüphane yüklü değilse testi atlamak:

import pytest

try:
    import requests
except ImportError:
    pytest.mark.skip("requests kütüphanesi yüklü değil.")

def test_skip_this_test():
    ...



4. @pytest.mark.xfail: Bu decorator, belirli bir test fonksiyonunun beklenen şekilde başarısız olmasını sağlar.

---Örnek olarak---

@pytest.mark.xfail
def test_fonksiyon():
    assert False, "Bu testin başarısız olması bekleniyor."

Açıklama:

-@pytest.mark.xfail dekoratörü, test fonksiyonunun başarısız olmasının beklendiğini gösterir.
-assert False ifadesi, test fonksiyonunun kasıtlı olarak başarısız olmasını sağlar.
-Bu test fonksiyonu çalıştırıldığında, "XFAIL" olarak işaretlenir.


@pytest.mark.xfail'in Kullanım Alanları:
-Henüz tamamlanmamış bir özelliğin test edilmesi
-Düzeltme bekleyen bir hatanın test edilmesi
-Belirli platformlarda veya Python sürümlerinde başarısız olması beklenen bir testin kontrol edilmesi


@pytest.mark.xfail ile İlgili Dikkat Edilmesi Gerekenler:
-@pytest.mark.xfail ile işaretlenmiş bir test fonksiyonu gerçekten başarısız olursa, test süiti başarısız sayılmaz.
-strict=True parametresi ile birlikte kullanıldığında, testin beklenmedik şekilde başarılı olması durumunda test süiti başarısız sayılır.



5. @pytest.mark.timeout: PyTest kütüphanesinde testlerin yürütme süresini sınırlamak için kullanılan bir dekoratördür. 
Bu dekoratör, testlerin belirli bir zaman sınırı içinde tamamlanmasını sağlayarak, sonsuz döngüye giren veya 
beklenmedik şekilde uzun süren testleri tespit etmenize yardımcı olur.

---Örnek olarak---

@pytest.mark.timeout(5)
def test_uzun_sureli_islem():
    for i in range(100000):
        # ... işlem ...

    assert True

def test_kisa_islem():
    assert True

Açıklama:

Bu örnekte, test_uzun_sureli_islem fonksiyonu 5 saniye içinde tamamlanmak zorundadır. 
Aksi takdirde, test başarısız sayılır. test_kisa_islem fonksiyonu ise herhangi bir zaman sınırı olmadan çalıştırılır.

Dikkat Edilmesi Gerekenler:

-Timeout süresi, testin başlangıcından itibaren hesaplanır.
-Testiniz birden fazla aşamadan oluşuyorsa, her aşama için ayrı bir timeout değeri belirleyebilirsiniz.
-Timeout süresi aşılırsa, test TimeoutError istisnası ile sonlanır.
-pytest-timeout eklentisini kullanarak, tüm testler için varsayılan bir timeout süresi belirleyebilirsiniz.

--Ek Örnekler--

@pytest.mark.timeout(10)
def test_yavas_fonksiyon():
    # ... kodunuz ...

def test_hizli_fonksiyon():
    # ... kodunuz ...


Açıklama:

Bu örnekte, test_yavas_fonksiyon 10 saniye içinde tamamlanmak zorundadır. 
Aksi takdirde, test başarısız sayılır. test_hizli_fonksiyon ise herhangi bir zaman sınırı olmadan çalıştırılır.



Daha Az Kullanılan Decoratorler:

@pytest.allure.step: Test adımlarını allure raporlarında görselleştirmek için kullanılır.
@pytest.mark.flaky: Belirli bir test fonksiyonunun istikrarsız olduğunu gösterir.
@pytest.mark.slow: Belirli bir test fonksiyonunun diğer testlerden daha uzun sürdüğünü gösterir.
@pytest.mark.order: Test fonksiyonlarının çalıştırılma sırasını belirlemek için kullanılır.
@pytest.fixture(scope="session"): Oturum kapsamında tek bir kez oluşturulan bir fixture'ı tanımlar.
@pytest.fixture(scope="module"): Modül kapsamında tek bir kez oluşturulan bir fixture'ı tanımlar.
@pytest.fixture(scope="class"): Sınıf kapsamında tek bir kez oluşturulan bir fixture'ı tanımlar.



Kullanılan Diğer Decoratorler:


1. @pytest.fixture(autouse=True): Bu decorator, bir fixture'ın test sınıfındaki her test fonksiyonu tarafından otomatik olarak kullanılmasını sağlar.

---Örnek olarak---

import pytest

@pytest.fixture(autouse=True)
def autouse_fixture():
    print("Her test fonksiyonundan önce çalışır.")
    yield
    print("Her test fonksiyonundan sonra çalışır.")

def test_func1():
    print("Test fonksiyonu 1")

def test_func2():
    print("Test fonksiyonu 2")


Çıktı:
Her test fonksiyonundan önce çalışır.
Test fonksiyonu 1
Her test fonksiyonundan sonra çalışır.
Her test fonksiyonundan önce çalışır.
Test fonksiyonu 2
Her test fonksiyonundan sonra çalışır.

Açıklama:

@pytest.fixture(autouse=True) dekoratörü, bir fonksiyonu her test fonksiyonundan önce ve sonra otomatik olarak çalıştırmak için kullanılır.
Bu örnekte, autouse_fixture fonksiyonu her test fonksiyonundan önce ve sonra "Her test fonksiyonundan önce/sonra çalışır." mesajını yazdırır.

Faydaları:

-Otomatik olarak çalıştırılan kod parçacıkları oluşturmak için kullanılabilir.
-Test fonksiyonlarında tekrar eden kodları önleyebilir.
-Test kodunu daha okunabilir ve anlaşılır hale getirebilir.

Dikkat edilmesi gerekenler:

-autouse fixture'ları her test fonksiyonundan önce ve sonra çalıştırıldığından, test fonksiyonlarının yürütme süresini etkileyebilir.
-autouse fixture'ları dikkatli bir şekilde kullanılmalıdır, aksi takdirde testlerde hatalara neden olabilir.



2. @pytest.yield_fixture: Bu decorator, bir fixture'ın test fonksiyonu tarafından kullanıldıktan sonra serbest bırakılmasını sağlar.

---Örnek olarak---

import pytest

@pytest.yield_fixture
def db():
    """Veritabanı bağlantısı oluşturur ve testler bittikten sonra kapatır."""
    connection = sqlite3.connect("test.db")
    yield connection
    connection.close()

def test_something(db):
    """Veritabanı bağlantısını kullanır."""
    # ... test kodunuz ...


Bu örnekte:

-@pytest.yield_fixture dekoratörü db fonksiyonunu bir "yield fixture" olarak tanımlar.
-db fonksiyonu bir veritabanı bağlantısı oluşturur ve yield anahtar sözcüğünden önce durur.
-Test fonksiyonu test_something db fixture'ı argüman olarak alır.
-Test fonksiyonu veritabanı bağlantısını kullanır.
-Test fonksiyonu tamamlandıktan sonra db fonksiyonunun kalanı (yield anahtar sözcüğünden sonra) çalışır ve veritabanı bağlantısını kapatır.

Yield fixture'ların avantajları:

-Testler için gerekli kaynakları (veritabanı bağlantıları, dosyalar, ağ bağlantıları vb.) oluşturmak ve yönetmek için daha basit ve daha okunabilir bir yol sağlar.
-Her test için ayrı bir kaynak örneği oluşturarak testlerin izole edilmesini sağlar.
-Testler bittikten sonra kaynakların düzgün şekilde kapatılmasını garanti eder.



3. @pytest.raises: Bu decorator, belirli bir kodun belirli bir hatayı oluşturmasını sağlar.

---Örnek olarak---

def fonksiyon(x):
  if x < 0:
    raise ValueError("x negatif olamaz!")
  return x

- fonksiyonun negatif bir sayı ile çağrıldığında ValueError hatası fırlatacağını test eder
def test_fonksiyon_negatif_sayi():
  with pytest.raises(ValueError):
    fonksiyon(-1)

- fonksiyonun pozitif bir sayı ile çağrıldığında hata fırlatmadığını test eder
def test_fonksiyon_pozitif_sayi():
  assert fonksiyon(1) == 1

Açıklama:

@pytest.raises dekoratörü bir fonksiyonun belirli bir hata türü fırlatıp fırlatmadığını test etmek için kullanılır.
with bloğu içinde fonksiyon çağrılır ve hata fırlatılıp fırlatılmadığı kontrol edilir.
Hata fırlatılırsa test başarılı olur, fırlatılmazsa test başarısız olur.

Bu örnekte:

-fonksiyon fonksiyonu, x negatifse ValueError hatası fırlatacak şekilde tanımlanmıştır.
-test_fonksiyon_negatif_sayi testi, fonksiyon fonksiyonunun -1 ile çağrıldığında ValueError hatası fırlatıp fırlatmadığını test eder.
-test_fonksiyon_pozitif_sayi testi, fonksiyon fonksiyonunun 1 ile çağrıldığında hata fırlatmadığını test eder.

Ek bilgiler:

-@pytest.raises ile birlikte match parametresi kullanılarak hata mesajının içeriği de kontrol edilebilir.
-Birden fazla hata türü test edilecekse pytest.raises dekoratörü ile birlikte tuple kullanılabilir.



4. @pytest.warns: Dekoratörü, bir test fonksiyonunun yürütülmesi sırasında belirli bir uyarı türünün veya mesajının tetiklenip tetiklenmediğini kontrol etmenizi sağlar.

---Örnek olarak---

import pytest

def test_my_function():
    # Uyarı tetikleyen kod
    warnings.warn("Bu bir uyarıdır.")

@pytest.warns(UserWarning)
def test_my_warning():
    # Uyarı tetikleyen kod
    warnings.warn("Bu bir uyarıdır.")

Açıklama:

-test_my_function fonksiyonu herhangi bir uyarı tetiklemez, bu nedenle test geçer.
-test_my_warning fonksiyonu UserWarning türünde bir uyarı tetikler, bu nedenle test de geçer.

Daha Fazla:

-Dekoratöre parametreler ekleyebilirsiniz:
-match parametresi: Uyarı mesajının bir kısmını veya tamamını eşleştirmek için kullanılır.
-category parametresi: Uyarı türünü belirlemek için kullanılır.



5. @pytest.deprecated: Bir test fonksiyonunun veya fikstürün eski olduğunu ve gelecekteki sürümlerde kaldırılabileceğini belirtmek için kullanılır. 
Bu fonksiyonu kullanarak, test kodunuzdaki eski kodları daha yeni ve daha iyi alternatiflerle değiştirmeniz gerektiği konusunda uyarı alabilirsiniz.

---Örnek olarak---

@pytest.deprecated("Kullanılmayan fonksiyon. Yeni fonksiyon `yeni_fonksiyon`'u kullanın.")
def eski_fonksiyon():
    pass

def test_eski_fonksiyon():
    with pytest.deprecated_call():
        eski_fonksiyon()

def yeni_fonksiyon():
    pass

def test_yeni_fonksiyon():
    yeni_fonksiyon()

Bu örnekte:

-eski_fonksiyon fonksiyonu, @pytest.deprecated fonksiyonu ile eski olarak işaretlenmiştir.
-test_eski_fonksiyon testi, eski_fonksiyon fonksiyonunu çalıştırdığında, bir uyarı mesajı görüntülenecektir.
-yeni_fonksiyon fonksiyonu, eski_fonksiyon fonksiyonuna alternatif olarak sunulmuştur.
-test_yeni_fonksiyon testi, yeni_fonksiyon fonksiyonunu çalıştırdığında, herhangi bir uyarı mesajı görüntülenmeyecektir.

Ek bilgiler:

-@pytest.deprecated fonksiyonu, bir mesaj parametresi alabilir. Bu parametre, kullanıcıya gösterilecek uyarı mesajını belirtir.
-@pytest.deprecated fonksiyonu, strict parametresi de alabilir. Bu parametre True olarak ayarlanırsa, eski fonksiyonun kullanımı bir hata olarak değerlendirilir.

Faydaları:

-Eski kodları daha yeni ve daha iyi alternatiflerle değiştirmenize yardımcı olur.
-Kodunuzun daha temiz ve daha bakımı kolay olmasını sağlar.
-Gelecekteki sürümlerde oluşabilecek hataları önceden haber vererek kodunuzun daha sağlam olmasını sağlar.