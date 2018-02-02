import pytest,allure
class Test_allure:
    @allure.step(title='第一个测试')
    def test_001(self):
        allure.attach("这是一个描述")
        assert 1