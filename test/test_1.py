import allure
import pytest
""" Основная информация взята из https://stepik.org/lesson/765268/step/1?unit=767488.
    Для просмотра результатов тестов необходимо в консоли в папке проекта запустить команду allure "serve test_result/)" """

@allure.description("Test #1.1")
def test_1_1():
    pat_1()
    pat_2()


@allure.description("Test #1.2")
def test_1_2():
    pat_1()
    pat_2()
    pat_3()


def pat_1():
    with allure.step("Step 1"):
        pass

def pat_2():
    with allure.step("Step 2"):
        pass


def pat_3():
    with allure.step("Step 3"):
        assert 1+1==3