import os

import requests
from dotenv import load_dotenv
from terminaltables import AsciiTable


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif not salary_to:
        return salary_from * 1.2
    elif not salary_from:
        return salary_to * 0.8


def predict_rub_salary_hh(vacancy):
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        return predict_salary(
            vacancy['salary']['from'],
            vacancy['salary']['to'],
        )


def predict_rub_salary_sj(vacancy):
    if vacancy['payment_from'] and vacancy['payment_to'] \
            and vacancy['currency'] == 'rub':
        return predict_salary(vacancy['payment_from'], vacancy['payment_to'])


def get_hh_statistics(keyword):
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'specialization': 1.221,
        'area': 1,
        'period': 30,
        'per_page': 100,
        'vacancy_search_field': 'name',
        'text': keyword,
    }
    pages_number = 1
    page = 0
    salaries_sum = 0
    vacancies_processed = 0
    vacancies_found = 0
    while page < pages_number:
        payload['page'] = page
        response = requests.get(url, params=payload)
        response.raise_for_status()
        hh_response = response.json()
        vacancies_found = hh_response['found']
        pages_number = hh_response['pages']
        for vacancy in hh_response['items']:
            predicted_salary = predict_rub_salary_hh(vacancy)
            if predicted_salary:
                salaries_sum += predicted_salary
                vacancies_processed += 1
        page += 1
    if vacancies_processed:
        average_salary = int(salaries_sum / vacancies_processed)
    else:
        average_salary = 0
    vacancies_by_keyword = {
        'vacancies_found': vacancies_found,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary,
    }
    return vacancies_by_keyword


def get_sj_statistics(keyword, superjob_secret_key):
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'
    sj_headers = {'X-Api-App-Id': superjob_secret_key}
    sj_payload = {
        'catalogues': 48,
        'town': 4,
        'count': 100,
        'keyword': keyword,
    }
    vacancies_found = 0
    salaries_sum = 0
    vacancies_processed = 0
    page = 0
    more_results = True
    while more_results:
        sj_payload['page'] = page
        response = requests.get(sj_url, headers=sj_headers, params=sj_payload)
        response.raise_for_status()
        sj_response = response.json()
        vacancies_found = sj_response['total']
        for vacancy in sj_response['objects']:
            predicted_salary = predict_rub_salary_sj(vacancy)
            if predicted_salary:
                salaries_sum += predicted_salary
                vacancies_processed += 1
        more_results = sj_response['more']
        page += 1
    if vacancies_processed:
        average_salary = int(salaries_sum / vacancies_processed)
    else:
        average_salary = 0
    vacancies_by_keyword = {
        'vacancies_found': vacancies_found,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary,
    }
    return vacancies_by_keyword


def print_table(vacancies_statistics, title):
    table_data = [[
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата',
    ]]
    for language, statistics in vacancies_statistics.items():
        language_statistics = [
            language,
            statistics['vacancies_found'],
            statistics['vacancies_processed'],
            statistics['average_salary'],
        ]
        table_data.append(language_statistics)
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')
    programming_languages = [
        'JavaScript',
        'Java',
        'Python',
        'Ruby',
        'PHP',
        'C++',
        'C#',
        'C',
        'Go',
        'Swift',
    ]
    hh_statistics_by_language = {}
    sj_statistics_by_language = {}
    for language in programming_languages:
        hh_statistics_by_language[language] = get_hh_statistics(language)
        sj_statistics_by_language[language] = get_sj_statistics(language, superjob_secret_key)
    print_table(hh_statistics_by_language, 'HeadHunter Moscow')
    print_table(sj_statistics_by_language, 'SuperJob Moscow')


if __name__ == '__main__':
    main()
