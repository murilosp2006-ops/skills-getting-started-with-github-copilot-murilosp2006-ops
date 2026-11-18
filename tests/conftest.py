from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def restore_activities():
    snapshot = deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(snapshot)