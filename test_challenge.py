import pytest
import re
from challenge import find_max_sum


class TestRegexMaxSum:
    
    def test_original_example(self):
        """Test the provided example"""
        input_strings = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
        expected = 13
        result = find_max_sum(input_strings)
        assert result == expected
    
    def test_empty_array(self):
        """Test with empty input array"""
        result = find_max_sum([])
        assert result == 0
    
    def test_no_digits(self):
        """Test strings with no digits"""
        input_strings = ["abc", "def", "xyz"]
        result = find_max_sum(input_strings)
        assert result == 0
    
    def test_only_digits(self):
        """Test strings with only digits"""
        input_strings = ["123", "456", "789"]
        result = find_max_sum(input_strings)
        assert result == 24  # 7+8+9 = 24
    
    @pytest.mark.parametrize("inputs,expected", [
        (["a1b2c3", "x9y8z7"], 24),      # 1+2+3=6, 9+8+7=24
        (["000", "111"], 3),             # 0+0+0=0, 1+1+1=3 
        (["5a5a5a", "1b1b1b1b"], 15),    # 5+5+5=15, 1+1+1+1=4 
        (["", "9"], 9),                  # empty=0, single digit=9
        (["single7", "double88"], 16),   # 7 vs 8+8=16 
        (["z", "9z9z9"], 27),           # 0 vs 9+9+9=27 
    ])
    def test_mixed_content(self, inputs, expected):
        """Test various mixed scenarios"""
        result = find_max_sum(inputs)
        assert result == expected
    
    def test_consecutive_digits_treated_individually(self):
        """Test that consecutive digits are treated individually."""
        # "36" should be treated as 3+6=9, not 36
        input_strings = ["h1n36mfl"]
        result = find_max_sum(input_strings)
        assert result == 10  # 1+3+6 = 10
        
        # Additional test for consecutive digits
        input_strings = ["abc123def"]
        result = find_max_sum(input_strings)
        assert result == 6  # 1+2+3 = 6, not 123
    
    def test_regex_pattern_validation(self):
        """Test that the regex pattern correctly finds individual digits."""
        test_string = "a1b23c456d"
        digits = re.findall(r'\d', test_string)
        expected_digits = ['1', '2', '3', '4', '5', '6']
        assert digits == expected_digits
        
        # Test the sum calculation
        result = find_max_sum([test_string])
        expected_sum = 1 + 2 + 3 + 4 + 5 + 6  # = 21
        assert result == expected_sum
    
    def test_edge_cases(self):
        """Test specific edge cases."""
        # Empty string in array
        result = find_max_sum(["abc", "", "123"])
        assert result == 6  # 1+2+3 = 6
        
        # Single character strings
        result = find_max_sum(["a", "5", "b", "9"])
        assert result == 9  # max of 0, 5, 0, 9
        
        # All zeros
        result = find_max_sum(["000", "00"])
        assert result == 0
        
        # Large digits
        result = find_max_sum(["9a9b9c"])
        assert result == 27  # 9+9+9 = 27
    


def test_regex_functionality():
    """Test the regex functionality"""
    assert re.findall(r'\d', "abc123def") == ['1', '2', '3']
    assert re.findall(r'\d', "no_digits") == []
    assert re.findall(r'\d', "1a2b3c") == ['1', '2', '3']


def test_performance_with_max_constraints():
    """Test with maximum constraints (10 strings, 12 chars each)."""
    max_strings = ["a1b2c3d4e5f6" for _ in range(10)]  # 10 strings, 12 chars each
    result = find_max_sum(max_strings)
    assert result == 21