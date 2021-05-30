from numpy import datetime_as_string
from pymysql import connect
from sanic.response import json
from db import connection
from templates import templates
import pandas as pd
from json import loads

async def employees(request, *args, **kwargs):
    count = kwargs.get('count')
    count = count if count else 10
    employees_df = pd.read_sql('SELECT * FROM employees LIMIT %(LIMIT)s', connection, params={'LIMIT': count})
    employees_json = loads(employees_df.to_json(orient='records', date_format='iso'))
    payload = {
        'success': True,
        'data': employees_json
    }
    return templates.render('employees/index.html', request, data=payload)

async def employees_salary(request, *args, **kwargs):
    count = kwargs.get('count')
    count = count if count else 10
    employees_df = pd.read_sql('SELECT * FROM employees LEFT JOIN salaries ON employees.emp_no = salaries.emp_no LIMIT %(LIMIT)s', connection, params={'LIMIT': count})
    employees_json = loads(employees_df.to_json(orient='table', date_format='iso'))
    payload = {
        'success': True,
        'data': employees_json
    }
    return templates.render('employees/salaries.html', request, data=payload)

async def employees_current_salary(request, *args, **kwargs):
    count = kwargs.get('count')
    count = count if count else 10
    employees_df = pd.read_sql('SELECT * FROM employees LEFT JOIN salaries ON employees.emp_no = salaries.emp_no WHERE YEAR(to_date)=9999 LIMIT %(LIMIT)s', connection, params={'LIMIT': count})
    employees_json = loads(employees_df.to_json(orient='table', date_format='iso'))
    payload = {
        'success': True,
        'data': employees_json
    }
    return templates.render('employees/salaries-current.html', request, data=payload)
