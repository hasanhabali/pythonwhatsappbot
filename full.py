from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome tarayıcısını aç
browser = webdriver.Chrome()

# WhatsApp Web sayfasını aç
browser.get("https://web.whatsapp.com/")

# Alıcının telefon numarası ya da ismi
recipient = "Jane Doe"

# Gönderilecek mesaj
message = "Merhaba! Bu bir test mesajıdır."

# Alıcının sohbet penceresini bul
user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(recipient))
user.click()

# Mesaj kutusunu bul ve mesajı gönder
message_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys(message)
message_box.send_keys(Keys.RETURN)
