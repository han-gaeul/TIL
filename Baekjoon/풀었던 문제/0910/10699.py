# 서울의 오늘 날짜를 출력하는 프로그램 작성

# 입력은 없다

# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력

import datetime

nowTime = datetime.datetime.now()
print(nowTime.strftime('%Y-%m-%d'))