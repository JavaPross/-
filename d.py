import unittest
import time
def measure_time(func):
    start_time =time.time()  
    result =func()  
    end_time =time.time()  
    exec_time =end_time -start_time  
    return result, exec_time
def slow_function():
    time.sleep(1)  
    return "готоыо"
class TestmeasureTime(unittest.TestCase):     
    def test_execution_time(self):
        result, exec_time = measure_time(slow_function)
        self.assertEqual(result, "готово")  
        self.assertGreaterEqual(exec_time, 1)  
    def test_fast_function(self):
        def fast_function():
            return 42
        result, exec_time = measure_time(fast_function)
        self.assertEqual(result, 42)  
        self.assertLess(exec_time, 0.01)  
if __name__ == "__main__":
    unittest.main()
# (я сделал с обьяснением в офийиальном сайте пайтона)
