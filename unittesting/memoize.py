#!/usr/bin/env python3
import time
import unittest
from unittest.mock import patch


def memo(func):
    cache = {}
    def memoized(*args):
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return memoized


@memo
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n-2)


   
class TestMemo(unittest.TestCase):
    @patch('__main__.memo')
    def testMemoFibo(self, mock_memo):
        memoized = mock_memo(fibo(5))
        
        memoized(5)
        memoized(5)
        
        # This asserts that the second call did not recompute but used the cached result
        mock_memo.assert_called_once()    
        
if __name__ == "__main__":
     unittest.main()
