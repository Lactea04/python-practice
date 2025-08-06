import pytest

from Employee import Employee


@pytest.mark.usefixtures
def default_employee():
    emp_infor = Employee('Taegyun', 'Kim', 5000)
    return emp_infor


def test_give_default_raise():
    print(default_employee().show_infor())
    assert 'Taegyun', 'Kim' in default_employee().show_infor().values()


def test_give_raise():
    print(default_employee().give_raise())
    assert 10450 in default_employee().give_raise().values()