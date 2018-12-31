'''
    1 模拟登陆
    2 动态页面模拟点击
    3 加载 JavaScript 语句
    4 图片文字处理
    5 从网站图片中抓取文字
    6 破解验证码

'''

# 模拟登陆
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = driver.PhantomJS()
driver.get('https://www.666.com/')

# 输入账户密码
driver.find_element_by_name('from_eamil').send_keys('666@666.com')
driver.find_element_by_name('from_passwd').send_keys('666666')

# 模拟点击登陆
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

time.sleep(1.5)

# 生成登陆后快照
driver.save_screenshot("666.png")
with open("666.html", 'w') as f:
    f.write(driver.page_source)

driver.quit()


# 动态页面模拟点击
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class DSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
    
    # 测试用例方法
    def testD(self):
        self.driver.get('http://666.com/')
        while True:
            # 指定 xml 解析
            soup = BeautifulSoup(driver.page_source, 'xml')
            # 返回当前页面的所有标题、列表
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            # zip()函数来可以把列表合并，并创建⼀个元组对的列表
            for titles, nums in zip(nums, titles):
                print(u'数量：'+ num.get_text().strip(), u'标题：' + title.get_text().strip())

            if driver.page_source.find('shark-pager-disable-next') != -1:
                break
            # 模拟点击下一页
            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 退出时清理方法
    def tearDown(self):
        print('加载完成...')
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

            
# 加载 JavaScript 语句
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.666.com/')

# 给搜索输入框标红的 javascript 脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红 js 
driver.execute_script(js)

# 查看页面快照
driver.save_screenshot('red666.png')
driver.quit()



# 图片文字处理
from PIL import Image
import subprocess

def cleanFile(fielPath, newFilePath):
    image = Image.open(fielPath)
    # 对图片进行阈值过滤并保存
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    # 调用 tesseract 命令对图片进行OCR 识别
    subprocess.call(["tesseract", newFilePath, "output"])

    # 打开文件读取结果
    file = open('output.txt', 'r')
    print(file.read())
    file.close()
cleanFile('test.jpg', 'textclean.png')



# 从网站图片中抓取文字
import time
import random
from urllib.request import urlretrieve import subprocess
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(random.randint(1,10))

# 当向右箭头可以点击时,开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(random.randint(1,5))

    # 获取已加载的新页面(一次可以加载多个页面,但是重复页面不能加载到集合中)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

driver.quit()

# Tesseract 处理我们收集的图中URL 链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], 
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    f = open("page.txt", "r")
    p.wait() 
    print(f.read())



# 破解验证码
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import subprocess
image requests
from PIL import Image, ImageOps

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)
    html = urlopen('http://www.666.com/')
    bsObj = BeautifulSoup(html)

    # 收集需要处理的表单数据(包括验证码和输入字段)
    imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
    formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"]
    captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"]
    captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"]
    captchaUrl = "http://www.666.com" + imageLocation
    urlretrieve(captchaUrl, "captcha.jpg")
    cleanImage("captcha.jpg")
    p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"],
                        stdout = subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("captcha.txt", "r")

    # 清理识别结果中的空格和换行符
    captchaResponse = f.read().replace(" ", "").replace("\n", "")
    print("Captcha solution attempt: " + captchaResponse)
    if len(captchaResponse) == 6:
        params = {
            "captcha_token":captchaToken, 
            "captcha__sid":captchaSid,
            "form_id":"comment_node_page_form", 
            "form_build_id": formBuildId, 
            "captcha_response":captchaResponse, 
            "name":"Ryan Mitchell", 
            "subject": "I come to seek the Grail", 
            "comment_body[und][0][value]": "...and I am definitely not a bot"}
        r = requests.post("http://www.pythonscraping.com/comment/reply/10", data=params)
        responseObj = BeautifulSoup(r.text)

        if responseObj.find("div", {"class":"messages"}) is not None:
            print(responseObj.find("div", {"class":"messages"}).get_text())

        else:
            print("There was a problem reading the CAPTCHA correctly!")