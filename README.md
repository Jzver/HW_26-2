# DRF_homework_26.2. Celery

### Задание 1

Настройте проект для работы с Celery. Также настройте приложение на работу с celery-beat для выполнения периодических
задач.

### Задание 2

Ранее вы реализовали функционал подписки на обновление курсов. Теперь добавьте асинхронную рассылку писем пользователям
об обновлении материалов курса.

### Задание 3  

С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю 
last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.