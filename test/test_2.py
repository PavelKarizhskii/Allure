import pytest
import allure

class Tests():

    @allure.description("Test #2.1")
    def test_pau_1(self):
        assert 1+1==2

    @allure.description("Test #2.2")
    def test_2_2(self):
        assert 1+1==3
