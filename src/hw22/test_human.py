import pytest

def test_check_return_value_for_name_property(human):
    assert human.name == 'Jonh'

def test_check_return_value_for_age_property(human):
    assert human.age == 25

def test_check_raise_exception_for_change_gender(human):
    method = getattr(
        human, f"_{human.__class__.__name__}__validate_gender"
    )

    with pytest.raises(Exception) as error:
        method("test")

def test_check_return_value_for_getting_fat(human):
    human.get_fat()
    assert human.weight == 80

def test_check_return_value_for_growing_up(human):
    human.grow_up()
    assert human.age == 26

def test_check_return_value_for_changing_name(human):
    human.change_name('David')
    assert human.name == 'David'

def test_check_return_value_for_changing_name_again(human):
    human.change_name('David')
    assert human.name == 'David'
