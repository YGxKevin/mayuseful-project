password = ('a123456') 										#宣告正確密碼
x = 3				  	 									#可輸入次數

while x >= 1 and x <= 3:									# 進入WHILE LOOP
	PSW = input('Please enter password:')					#注意: 如用數值 以後要修改將一個一個數值處理
	if PSW == password:										#注意: 要跟正確密碼不同的宣告 否則將蓋過正確密碼 形成BUG
		break
	else:
		x -= 1
		print('Access Denied')
		if x == 0:
			break
		print('you still got', x, 'times chances')

if PSW == password:
	print('Access Granted')
else:
	print('You have no Authorization to Access this file.')