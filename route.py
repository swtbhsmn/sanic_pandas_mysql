from sanic import Sanic

from api.home.views import (
    home,
)

from api.employee.views import (
    employees,
    employees_salary,
    employees_current_salary
)

app = Sanic.get_app()

def route():
    app.add_route(home, '/', methods=['GET'], name='home')
    app.add_route(employees, '/employees', methods=['GET'], name='employees_default')
    app.add_route(employees, '/employees/<count:int>', methods=['GET'], name='employees_count')
    app.add_route(employees_salary, '/employees-salaries', methods=['GET'], name='employees_salaries_default')
    app.add_route(employees_salary, '/employees-salaries/<count:int>', methods=['GET'], name='employees_salaries_count')
    app.add_route(employees_current_salary, '/employees-current-salaries', methods=['GET'], name='employees_current_salaries_default')
    app.add_route(employees_current_salary, '/employees-current-salaries/<count:int>', methods=['GET'], name='employees_current_salaries_count')