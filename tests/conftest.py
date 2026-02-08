# Configuration for pytest
# This is a test configuration file for pytest

import pytest

@pytest.fixture
def sample_fixture():
    # This is an example fixture that can be used in tests
    return "sample data"
