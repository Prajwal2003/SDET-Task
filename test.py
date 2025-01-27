from selenium import webdriver
from browsermobproxy import Server
import time

bmp_path = "/Users/starkz/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"

server = Server(bmp_path)
server.start()
proxy = server.create_proxy()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_options)

proxy.new_har("exactspace", options={"captureHeaders": True, "captureContent": True})

driver.get("https://exactspace.co/")
time.sleep(5)

har_data = proxy.har

with open("exactspace.har", "w") as f:
    f.write(str(har_data))

driver.quit()
server.stop()
