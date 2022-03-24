# Evaluating future salary

This program fetches programming vacancies for the most popular programming languages through HeadHunter and SuperJob API and calculates average salary by programming language. Results are presented in form of a table.

### How to install

Python3 should already be installed. Use pip (or pip3, in case of conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To get data through SuperJob API you will need a secret key. [Register an app](https://api.superjob.ru/register) in order to get one. After that, create an `.env` file in the project directory and put your secret key in the `SUPERJOB_SECRET_KEY` variable:
```
SUPERJOB_SECRET_KEY = 'YOUR_SECRET_KEY'
```

### Usage

To run the program use the following command from the project directory:
```
python main.py
```
Example of the result:
```
+HeadHunter Moscow------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 3501             | 797                 | 190811           |
| Java                  | 3016             | 430                 | 245380           |
| Python                | 2574             | 439                 | 214571           |
| Ruby                  | 184              | 52                  | 231682           |
| PHP                   | 1352             | 599                 | 169397           |
| C++                   | 1450             | 378                 | 194894           |
| C#                    | 1562             | 413                 | 193680           |
| C                     | 2528             | 667                 | 181808           |
| Go                    | 745              | 168                 | 260968           |
| Swift                 | 499              | 128                 | 258220           |
+-----------------------+------------------+---------------------+------------------+
+SuperJob Moscow--------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 87               | 63                  | 139919           |
| Java                  | 35               | 26                  | 175492           |
| Python                | 46               | 31                  | 165593           |
| Ruby                  | 2                | 2                   | 130000           |
| PHP                   | 63               | 47                  | 154636           |
| C++                   | 38               | 34                  | 171617           |
| C#                    | 30               | 22                  | 173818           |
| C                     | 24               | 18                  | 166055           |
| Go                    | 5                | 5                   | 200400           |
| Swift                 | 5                | 4                   | 202500           |
+-----------------------+------------------+---------------------+------------------+
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).
