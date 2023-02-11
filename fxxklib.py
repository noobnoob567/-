#第一版程序，疯狗型抢座法，抢到什么就什么
import time
import datetime
from webdriver_manager.chrome import ChromeDriverManager
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
from selenium import webdriver

#driver_path = r"D:\python\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=driver_path)
browser = webdriver.Chrome(ChromeDriverManager().install())
#browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/roomSelectSeat.php?area_id=17")
def login():
	browser.get("https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php")
	time.sleep(2)
	print(f"正在登录系统")
	input = browser.find_element_by_id("un")#输入账号
	input.send_keys('201852099')
	#input.send_keys('201864010')
	#time.sleep(0.2)
	input = browser.find_element_by_id("pd")#输入密码
	input.send_keys('Wl000218')
	#input.send_keys('774965430164a')
	time.sleep(0.5)
	browser.find_element_by_xpath("/html/body/form/div[2]/div/div[2]/div[2]/div[1]/span/input").click()
	print(f"登录完成")
	time.sleep(2)
	
	
def picking(method):
	browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/areaSelectSeat.php")
	time.sleep(1)
	browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/roomSelectSeat.php?area_id=17")
	#方式0以临时座位作为测试
	time.sleep(1)
	if method == 0:
		while True:
			try:
				if browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[2]"):
					#text = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]")
					#browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]").click()
					print(f"找到按钮")
					#三楼大厅
					text1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td").text
					#301
					text2 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[3]/td").text
					#312
					text3 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[4]/td").text
					#401
					text4 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td").text
					#404
					text5 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td").text
					#409
					text6 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[7]/td").text
					#501
					text7 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[8]/td").text
					#504
					text8 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[9]/td").text
					#507
					text9 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[10]/td").text										
					num1 = int(text1[-1])
					num2 = int(text2[-1])
					num3 = int(text3[-1])
					num4 = int(text4[-1])
					num5 = int(text5[-1])
					num6 = int(text6[-1])
					num7 = int(text7[-1])
					num8 = int(text8[-1])
					num9 = int(text9[-1])
					print(num1,num2,num3,num4,num5,num6,num7,num8,num9)
					
					if num1 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[2]").click()
					elif num2 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[3]").click()
					elif num3 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[4]").click()
					elif num4 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[5]").click()
					elif num5 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[6]").click()
					elif num6 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[7]").click()
					elif num7 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[8]").click()
					elif num8 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[9]").click()
					elif num9 != 0:
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[10]").click()
					
					else:
						print(f"没有座位,正在点击刷新")
						time.sleep(0.3)
						browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/button[1]").click()
						print(f"刷新完毕")
						time.sleep(0.2)
						continue		
					
				time.sleep(0.4)
				browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
				time.sleep(0.3)
				browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
				print(f"预约成功请查看，若失败请重启")
				break
					
			except:

				print(f"找不到按钮，正在重试")
				time.sleep(0.5)
				browser.refresh()
				time.sleep(0.5)
				
	else:
		print(f"end")
		time.sleep(5)
	
method = 0	
login()
picking(method)
