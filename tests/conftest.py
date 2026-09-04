import pytest

# fixture apara alterar o idimo da fixture padrãod o faker
@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_br']