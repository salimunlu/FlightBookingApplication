# FlightBookingApplication

FlightBookingApplication, kullanıcıların uçuş arayabileceği, rezervasyon yapabileceği ve mevcut rezervasyonlarını görüntüleyebileceği bir uçak bileti rezervasyon sistemidir. Bu uygulama Python ile SQLite veritabanı kullanılarak geliştirilmiştir ve hem komut satırı arayüzü hem de basit bir grafik kullanıcı arayüzü (GUI) sunmaktadır.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Geliştirici Notları](#geliştirici-notları)
- [Gereksinimler](#gereksinimler)

## Özellikler

- **Kullanıcı Yönetimi:** Kullanıcılar sisteme kayıt olabilir ve giriş yapabilir.
- **Uçuş Arama:** Kalkış ve varış şehirlerine göre uçuş arayabilir.
- **Rezervasyon Yapma:** Mevcut uçuşlara rezervasyon yapabilir.
- **Rezervasyonları Görüntüleme:** Kullanıcılar yaptıkları rezervasyonları listeleyebilir.
- **Veritabanı Yönetimi:** SQLite veritabanı kullanarak kullanıcı, uçuş ve rezervasyon verilerini saklar.

## Kurulum

1. **Proje Deposu Klonlama**: Bu projeyi bilgisayarınıza klonlayın.
    ```bash
    git clone https://github.com/salimunlu/FlightBookingApplication.git
    ```

2. **Gereksinimleri Yükleme**: Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın.
    ```bash
    pip install -r requirements.txt
    ```

3. **Veritabanı Kurulumu**: Veritabanı tablolarını oluşturmak için `main.py` dosyasını çalıştırın.
    ```bash
    python main.py
    ```

4. **Uygulama Arayüzü**: Hem GUI hem de CLI arayüzünden uygulamayı kullanabilirsiniz.
    - CLI için `main.py` dosyasını çalıştırın.
    - GUI için `gui.py` dosyasını çalıştırın.

## Kullanım

### CLI Arayüzü
Komut satırı arayüzünü kullanarak sisteme giriş yapabilir, uçuş arayabilir ve rezervasyon yapabilirsiniz.

- **Kullanıcı Kaydı**: Kayıt olmak için kullanıcı adı ve şifre girin.
- **Giriş**: Sisteme giriş yaparak uçuş arama ve rezervasyon işlemlerine devam edin.
- **Uçuş Arama**: Kalkış ve varış şehirlerini girerek uçuşları listeleyin.
- **Rezervasyon Yapma**: Uygun bir uçuş ID'si girerek rezervasyon yapın.

### GUI Arayüzü
Basit bir grafik arayüz ile uçuşları arayabilir, rezervasyon yapabilir ve rezervasyonlarınızı görüntüleyebilirsiniz.

- **Giriş Ekranı**: Kullanıcı adı ve şifre ile giriş yapın.
- **Uçuş Arama**: Arayüz üzerinden kalkış ve varış şehirlerini seçerek uçuşları görüntüleyin.
- **Rezervasyonlarım**: Mevcut rezervasyonlarınızı listeleyin.

## Geliştirici Notları

- **Veritabanı Yönetimi**: Veritabanı dosyası `airline_booking.db` olarak tanımlanmıştır ve `db_module.py` dosyasında oluşturulmaktadır.
- **GUI Geliştirmesi**: `tkinter` kütüphanesi ile basit bir kullanıcı arayüzü tasarlanmıştır. Uygulamanın logosu `images/logo.png` dizininde yer almaktadır.
- **Güvenlik**: Kullanıcı şifreleri `SHA256` algoritması ile hash'lenerek veritabanına kaydedilir.
- **Uçuş Verisi**: Proje başlangıcında varsayılan olarak birkaç örnek uçuş bilgisi veritabanına eklenir.

## Gereksinimler

- Python 3.x
- `sqlite3` (Python ile birlikte gelir)
- `tkinter` (Python ile birlikte gelir)
- `Pillow` (Görüntü işleme için kullanılır)

Gereksinimleri yüklemek için `requirements.txt` dosyasını kullanabilirsiniz.

```bash
pip install -r requirements.txt


