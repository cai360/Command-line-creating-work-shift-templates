import project
import schedual
import pytest

def main():
    test_show_function()
    test_check_option()
    test_print_schedual()

def test_show_function():
    assert project.show_function() == 1

def test_check_option():
    assert project.check_option(1) == 1
    with pytest.raises(ValueError):
        project.check_option("cat")

def test_print_schedual():
    s = schedual.Schedual()
    assert project.print_schedual(s) == 3





if __name__ == "__main__":
    main()
