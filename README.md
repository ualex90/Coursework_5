<h1 align="center">JobParserDB, Coursework_5</h1>
<h3>Приложение предназначено для поиска вакансий среди работодателей HeadHunter с применением базы данных PostgreSQL</h3>

><h3 align="center">ВНИМАНИЕ!!!</h3>
>
>**Для корректной работы в PyCharm, необходимо включить эмуляцию терминала!!! Для этого необходимо открыть файл 
main.py, вызвать контекстное меню нажатием правой кнопки мыши и перейти в пункт "Modify Run Configuration...". Нажать на 
"Modify Options" и установить галочку на "Emulate terminal in out console"**
>
*Для удобства работы с командами из main.py, можно создать в корне проекта файл .env и поместить в него данные для входа 
на сервер базы данных формате:*
```SQL
USER=user_name
PASSWORD=user_psw
```
***

<h3 align="center">1 Основной функционал</h3>
* Авторизация на сервере базы данных и сохранение данных для авторизации в файл
* Создание базы данных
* Создание таблиц (employers и vacancies) по параметрам из конфигурационного файла
* Очистка и удаление таблиц
* Редактирование списка работодателей
* Получение вакансий выбранных работодателей
* Заполнение базы данных данными о работодателях и их вакансий
* Формирование ответов на запросы к базе данных в виде таблиц
***

<h3 align="center">2 Запуск приложения</h3>

Для запуска необходимо настроить виртуальное окружение poetry в корневой директории проекта:
```bash
poetry install
poetry shell
```

Запуск приложения:
```bash
python3 main.py
```
***

<h3 align="center">3 Работа с приложением</h3>
<h4 align="center">3.1 Главное меню</h4>

После успешного запуска приложения, появится главное меню:
```
1. Подключение к базе данных
2. Редактировать списка работодателей
3. Управление базой данных
4. Запросы к базе данных

(e): Выход из программы
>> 

```
1. Ввод адреса сервера, порта, имя пользователя, пароля и имя базы данных которая будет создана
2. Добавление, удаление работодателей из списка предназначенного для получения данных по API
3. Создание базы данных, создание/удаление/очистка таблиц, заполнение базы данных
4. Выполнение пользовательских запросов к базе данных
***

<h4 align="center">3.2 Подключение к базе данных</h4>
При первом запуске, необходимо ввести данные для подключения к серверу. 
Если сервер находится на локальной машине, можно просто нажать ENTER:
```
Для работы с программой необходимо знать данные для подключения к серверу базы данных PosgreSQL!!!
--------------------------------------------------------------------------------------------------
Введите адрес сервера или нажмите "ENTER" если "localhost
Адрес: 
```
Порт по умолчанию 5432:
```
Если сервер находится на локальной машине, можно просто нажать ENTER
```
Далее необходимо ввести имя пользователя и пароль:
```
Имя пользователя:
```
```
Пароль:
```
Для создания базы данных с которой будет работать приложение, необходимо придумать ее имя или просто нажать ENTER
для создание базы с именем "headhunter":
```
Введите имя для базы данных для HeadHunter (по умолчанию "headhunter")
Имя базы данных:  
```
В случае успешного подключения и создания базы, будет выведено следующее сообщение:
```
Попытка соединения...
Создана база данных "headhunter"
--------------------------------
Соединение с базой данных headhunter установлено
------------------------------------------------
Нажмите "ENTER"
```
При последующих запусках приложения, будет выведено сообщение с предложением подключиться по ранее введенным данным
```
Подключиться к введенному ранее серверу "localhost:5432, user_name"? (y/n)
```
***

<h4 align="center">3.3 Редактировать списка работодателей</h4>
Список работодателей представляет из себя таблицу из 3 колонок
1. "№" - номер на странице таблицы, необходим для выбора работодателя с целью удаления из списка
2. "ID" - Идентификационный номер работодателя на HeadHunter
3. "КОМПАНИЯ" - Имя работодателя

```
|№|   ID    |                                  КОМПАНИЯ                                         |
|===============================================================================================|
|0| 4596113  | Фабрика Решений                                                                  |
|1| 1204987  | Carbon Soft                                                                      |
|2| 6019841  | А-Телематика                                                                     |
|3| 2791     | Шлюмберже                                                                        |
|4| 9311920  | DNS Технологии                                                                   |
|5| 4527132  | Владлинк                                                                         |
|6| 2748     | Ростелеком                                                                       |
|7| 4181     | Банк ВТБ (ПАО)                                                                   |
|8| 23186    | Группа Компаний РУСАГРО                                                          |
|9| 1666189  | МедиаСофт                                                                        |

Страница 1 из 2
(q): в меню, (z): назад, (ENTER): вперед
Для добавления работодателя введите (a)
Для удаления работодателя из списка введите его номер.
>> 
```

Для управления используются навигационные символы:
* (a) - Добавить работодателя. Для этого необходимо ввести ID работодателя или ID нескольких работодателей через запятую:
```
Введите ID работодателей через запятую
>>
```
* (ENTER) - Пролистывание страниц вперед, нужно нажать ENTER
* (z) - Пролистывание страниц назад
* (1) - Для удаления работодателя необходимо ввести его номер на странице и подтвердить (y)
* (q) - Выход в главное меню
***

<h4 align="center">3.4 Управление базой данных</h4>
