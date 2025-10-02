# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description
import basic
def test_add():
    assert basic.add(4, 3, 2, 1) == 10.0, "Should be 10.0"
    assert basic.add(30, 20) == 50.0, "Should be 50.0"
    return None

def test_mul():
    assert basic.mul(4, 3, 2) == 24.0, "Should be 24.0"
    return None

def test_div():
    assert basic.div(4, 3) == 1.333, "Should be 1.333"
    return None

def main():
    print("Starting Tests...")
    test_add()
    test_mul()
    test_div()
    print("All TESTS Successful")
    return None

# Namespace Trick
if __name__ == "__main__":
    main()