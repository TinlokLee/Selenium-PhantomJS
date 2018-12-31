from selenium import webdriver
from selenium.webdriver.common.keys import Keys

diver = webdriver.PhantomJS()
diver.get('https://github.com/')
data = diver.find_element_by_id("wrapper").text

print(data)
print(driver.title)

# 生成快照并保存
driver.save_screenshot('github.png')
driver.find_element_by_id('kw').send_keys(u'python')

# 模拟点击
driver.find_element_by_id('su').click()

# 获取新的页面快照
driver.save_screenshot("python.png")

# 打印网页渲染后的源代码
print(diver.page_source)

# 获取当前页面 cookie
print(driver.get_cookiess())

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("666")

# 模拟 Enter 回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
driver.find_element_by_id("kw").clear()

# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()

'''页面操作'''
# 获取 id 标签值
element = driver.find_element_by_id("passwd_id")
# 获取 name 标签值
element = driver.find_element_by_name("user-name")
# 获取标签名值
element = driver.find_elements_by_tag_name("input")
# 也可以通过 XPath 来匹配
element = driver.find_element_by_xpath("//inputt[@id='passwd-id']")

from selenium.webdriver.common.by import By
element = driver.find_element(by=By.ID, value="coolestWidgetEvah")
frame = driver.find_element(By.TAG_NAME, "iframe")
cheese = driver.find_element(By.LINK_TEXT, "cheese")
cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")
inputs = driver.find_elements(By.XPATH, "//input")

'''鼠标动作链'''
from selenium.webdriver import ActionChains

# 鼠标移动到 ac 位置
ac = diver.find_element_by_xpath('element')
ActionChains(driver).move_to_element(ac).perform()

# 在 ac 位置单击
ac = driver.find_element_by_xpath("elementA")
ActionChains(driver).move_to_element(ac).click(ac).perform()

# 在 ac 位置双击
ac = driver.find_element_by_xpath("elementB")
ActionChains(driver).move_to_element(ac).double_click(ac).perform()

# 在 ac 位置右击
ac = driver.find_element_by_xpath("elementC")
ActionChains(driver).move_to_element(ac).context_click(ac).perform()

# 在 ac 位置左键单击 hold 住
ac = driver.find_element_by_xpath('elementF')
ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

# 将 ac1 拖拽到 ac2 位置
ac1 = driver.find_element_by_xpath('elementD')
ac2 = driver.find_element_by_xpath('elementE')
ActionChains(driver).drag_and_drop(ac1, ac2).perform()


'''填充表单'''
from selenium.webdriver.support.ui import Select

# 找到 name 的选项卡
select = Select(driver.find_element_by_name('status'))

# 三种选择下拉框方式，索引、值、标签文本
select.select_by_index(1)
select.select_by_value("0")
select.select_by_visible_text(u"未审核")

# 全部取消
select.deselect_all()

'''弹窗处理'''
alert = driver.switch_to_alert()

'''页面切换'''
driver.switch_to_window('this is window name')

# 获取每个窗口操作对象
for handle in driver.window_handles:
    driver.switch_to_window(handle)

'''页面前进后退'''
driver.forward()
driver.back()

'''获取页面cookies'''
for cookie in driver.get_cookies():
    print("%s -- %s" % (cookie['name'], cookie['value']))

# 删除cookies
driver.delete_cookie('CookieName')
driver.delete_all_cookies()

'''页面等待***'''
'''
    为了避免元素定位困难，selenium 提供两种等待方式
    隐式等待：等待特定时间
    显示等待：指定某一条件直到条件成立继续执行

'''
# 隐式等待
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get('https://www.666.com/')
doElement = driver.find_element_by_id('doElement')

# 显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.get('https://www.666.com/')
try:
    element = WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.ID, 'doElement')))

finally:
    driver.quit()
    



