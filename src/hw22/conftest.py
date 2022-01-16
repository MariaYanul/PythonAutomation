import pytest
from human import Human

@pytest.fixture
def human() -> Human:
    human = Human('Jonh', 25, 'male', 75)
    yield human
