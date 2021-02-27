import os
site="dvmn.org"
frname="Violeta"
myname="Igor"
mymail=os.getenv("LOGIN")
tomail="ike14492@gmail.com"
mypass=os.getenv("PASSWORD")
lt = """From: mymail
To: tomail
Subject: PythonMailer
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
lt=lt.replace("%website%", site)
lt=lt.replace("%friend_name%", frname)
lt=lt.replace("%my_name%",myname)
lt=lt.replace('mymail', mymail)
lt=lt.replace('tomail', tomail)
lt=lt.encode("UTF-8")

import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login(mymail, mypass)
server.sendmail(mymail, tomail, lt)
server.quit()
