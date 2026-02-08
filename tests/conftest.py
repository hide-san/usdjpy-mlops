import pytest

@pytest.fixture
def sample_fixture():
    # Setup code for the fixture
    yield 'sample data'
    # Teardown code (if needed)
