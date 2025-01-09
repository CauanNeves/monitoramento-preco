from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

#Funcções do Webdriver
def start_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\\secretario',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    return driver

def wait_for_element(driver, by, value, timeout=60):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def formatted_price(price):
    price_before = price.replace('R$', '').strip()
    price_before = price_before.replace(',', '.')
    
    price_clean = float(price_before)
    
    if price_clean.is_integer():
        return int(price_clean)
    else:
        return price_clean
#Função principal
def main():
    driver = start_driver()
    driver.get('https://www.terabyteshop.com.br/produto/31959/gabinete-gamer-redragon-wideload-extreme-mid-tower-rgb-vidro-curvado-temperado-atx-black-sem-fonte-sem-fan-ca-605b')
    sleep(0.5)
    price_in_cash = driver.execute_script(f'''
return document.evaluate(
    '//p[@id= "valVista"]', 
    document, 
    null, 
    XPathResult.FIRST_ORDERED_NODE_TYPE, 
    null
    ).singleNodeValue;
                                    ''')
    driver.execute_script('arguments[0].scrollIntoView({behavior: "instant", block: "center"});', price_in_cash)
    price_in_cash = driver.execute_script('return arguments[0].innerText;', price_in_cash)
    price_full = driver.find_element(By.XPATH, '(//span[@id="valParc"])[2]').text
    
    print(f'Preço à vista: {formatted_price(price_in_cash)};\nPreço cheio: {formatted_price(price_full)}')
    
if __name__ == '__main__':
    main()