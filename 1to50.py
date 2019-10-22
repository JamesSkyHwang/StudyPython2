from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

#전역변수
#현재 찾아야 할 숫자
num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        if btn.text == str(num):
            btn.click()
            num += 1
            return

'''
//*[@id="grid"]/div[1]/span
//*[@id="grid"]/div[2]/span
//*[@id="grid"]/div[6]/span
'''


#print(btns)
#print(btns[0].text)

while num <= 50:
    clickBtn()
