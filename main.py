from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import streamlit as st


if __name__ == '__main__':
    command = input('Введите команду: ')
    if command == 'salary':
        try:
            print(date.today())
            calculate_salary()
        except Exception as e:
            print('У нам проблемы')
        finally:
            print('Программа завершена')
    else:
        try:
            print(date.today())
            get_employees()
        except Exception as e:
            print('У нам проблемы')
        finally:
            print('Программа завершена')

