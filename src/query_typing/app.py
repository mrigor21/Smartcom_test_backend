# mypy src/ --strict

from query_typing.model import (
    DepartmentModel,
    DepartmentQuery,
    EmployeeModel,
    EmployeeQuery,
)
from query_typing.model_base import ModelBase, QueryBase


departments = DepartmentQuery([DepartmentModel(id=1, name="dep1", parent_id=None)])
employees = EmployeeQuery([EmployeeModel(id=1, name="emp1", department_id=1), EmployeeModel(id=2, name="emp3", department_id=2)])

employee = employees.get(2)
employee_name: str = employee.name

department = departments.get(1)
department_name: str = department.name

try:
    departments.get(1)
    employees.get(99)
except DepartmentQuery.NotFoundError:
    print("no department found")
except EmployeeQuery.NotFoundError:
    print("no employee found")
