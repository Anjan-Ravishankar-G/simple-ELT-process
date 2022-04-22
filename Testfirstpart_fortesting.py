import pytest
import firstpart

class Testclass:
    def test_methodcount0(self):
        
        result=firstpart.extract(0,'C://Users//ADMIN//anjan-python//fileproject//documents//testcase1.txt')
        result1=firstpart.transformation(result)
        result2=firstpart.writer(0,'C://Users//ADMIN//anjan-python//fileproject//writtendoc//xyz.txt',result1)
        assert result=='Hello world, hello' and result2=='HELLO WORLD, HELLO'

    def test_methodcount1(self):
        result=firstpart.extract(1,'C://Users//ADMIN//anjan-python//fileproject//documents//testcase1.txt')
        result1=firstpart.transformation1(result)
        result2=firstpart.writer(1,'C://Users//ADMIN//anjan-python//fileproject//writtendoc//xyz.txt',result1)
        assert result=='Hello world, hello' and result2==['hello->2', 'world->1']    