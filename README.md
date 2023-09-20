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

Список работодателей представляет из себя таблицу из 3 колонок:
* "№" - номер на странице таблицы, необходим для выбора работодателя с целью удаления из списка
* "ID" - Идентификационный номер работодателя на HeadHunter
* "КОМПАНИЯ" - Имя работодателя

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

Если были внесены изменения, то будет предложено создать базу данных
***

<h4 align="center">3.4 Управление базой данных</h4>
Данный раздел предназначен для редактирования состава базы данных. Каждая выполненная/невыполненная операция будет 
подтверждена сообщением
```
1. Создать таблицу "vacancies"
2. Создать таблицу "employers"
3. Очистить таблицу "vacancies"
4. Очистить таблицу "employers"
5. Удалить таблицу "vacancies"
6. Удалить таблицу "employers"
7. Заполнить базу данных

(q): Назад в главное меню
>> 
```
***

<h4 align="center">3.5 Запросы к базе данных</h4>

Данный раздел позволяет обращаться к созданной и заполненной базе данных. Если база данных или какие либо таблицы не 
существуют, то будет предложено их создать.

1. Получает список всех компаний и количество вакансий у каждой компании

```
|   №   |                     Работодатель                    | Вакансии |
|========================================================================|
|   1   | Тензор                                              |   193    |
|   2   | Группа Компаний РУСАГРО                             |   673    |
|   3   | Банк ВТБ (ПАО)                                      |   2000   |
|   4   | DNS Технологии                                      |    54    |
|   5   | Miles&Miles                                         |    16    |
|   6   | Фабрика Решений                                     |    5     |
|   7   | Владлинк                                            |    37    |
|   8   | МедиаСофт                                           |    26    |
|   9   | Carbon Soft                                         |    5     |
|  10   | Шлюмберже                                           |   208    |

Страница 1 из 2
(q): в меню, (z): назад, (ENTER): вперед
```

2. Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию

```
|   №   |              Вакансия              |          Работодатель         |   Зарплата  |      Ссылка на HeadHunter      |
|===========================================================================================================================|
|   1   | Agile коуч                         | Банк ВТБ (ПАО)                |             | https://hh.ru/vacancy/86093517 |
|   2   | Agile коуч                         | Банк ВТБ (ПАО)                |             | https://hh.ru/vacancy/71697112 |
|   3   | BI-аналитик (Junior)               | DNS Технологии                | 60000 RUR   | https://hh.ru/vacancy/86509396 |
|   4   | BI разработчик                     | Группа Компаний РУСАГРО       |             | https://hh.ru/vacancy/86853256 |
|   5   | Build-инженер/программист          | Тензор                        | 210000 RUR  | https://hh.ru/vacancy/85845944 |
|   6   | Build-инженер/программист          | Тензор                        | 210000 RUR  | https://hh.ru/vacancy/85846160 |
|   7   | Business-Analyst CJM               | Банк ВТБ (ПАО)                |             | https://hh.ru/vacancy/86920990 |
|   8   | Chief Product Owner (расчетный ... | Банк ВТБ (ПАО)                |             | https://hh.ru/vacancy/86290749 |
|   9   | Contracts Analyst                  | Шлюмберже                     |             | https://hh.ru/vacancy/85921911 |
|  10   | CRM Lead (Стрим "Транзакционный... | Банк ВТБ (ПАО)                |             | https://hh.ru/vacancy/84261303 |

Страница 1 из 322
(q): в меню, (z): назад, (ENTER): вперед
```

3. Получает среднюю зарплату по вакансиям

```
|   №   | Средняя зарплата |
|==========================|
|   1   | 102405 RUR       |
```

4. Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям

```
|   №   |              Вакансия              |          Работодатель         |   Зарплата  |      Ссылка на HeadHunter      |
|===========================================================================================================================|
|   1   | Руководитель направления разраб... | Тензор                        | 550000 RUR  | https://hh.ru/vacancy/86736121 |
|   2   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86280717 |
|   3   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86280545 |
|   4   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86280667 |
|   5   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86280749 |
|   6   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86280638 |
|   7   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/82786641 |
|   8   | Руководитель направления разработки| Тензор                        | 520000 RUR  | https://hh.ru/vacancy/86409061 |
|   9   | Senior Android Developer           | Тензор                        | 440000 RUR  | https://hh.ru/vacancy/84159013 |
|  10   | Ведущий программист Python         | Тензор                        | 430000 RUR  | https://hh.ru/vacancy/86352061 |
```

5. Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python

```
|   №   |              Вакансия              |          Работодатель         |   Зарплата  |      Ссылка на HeadHunter      |
|===========================================================================================================================|
|   1   | Middle Fullstack Python разработчик| DNS Технологии                |             | https://hh.ru/vacancy/84406564 |
|   2   | Middle / Senior Python/Go developer| МедиаСофт                     | 200000 RUR  | https://hh.ru/vacancy/30548119 |
|   3   | Python developer                   | МедиаСофт                     | 250000 RUR  | https://hh.ru/vacancy/46229759 |
|   4   | Python-developer                   | Тензор                        | 200000 RUR  | https://hh.ru/vacancy/85846174 |
|   5   | Python-developer                   | Тензор                        | 220000 RUR  | https://hh.ru/vacancy/82613417 |
|   6   | Python-developer                   | Тензор                        | 215000 RUR  | https://hh.ru/vacancy/86641266 |
|   7   | Python разработчик                 | Тензор                        | 223000 RUR  | https://hh.ru/vacancy/85464970 |
|   8   | Senior Python developer            | МедиаСофт                     | 250000 RUR  | https://hh.ru/vacancy/86531354 |
|   9   | Senior разработчик-python (Djan... | Фабрика Решений               | 320000 RUR  | https://hh.ru/vacancy/86819736 |
|  10   | Ведущий C++, Python-программист    | Тензор                        | 340000 RUR  | https://hh.ru/vacancy/86396495 |

Страница 1 из 4
(q): в меню, (z): назад, (ENTER): вперед
```
