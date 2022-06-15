import pytest
import json

from submit_model import app


@pytest.fixture()
def dr_submit_event():
    test_event = open('./events/event.json')
    return json.load(test_event)


def test_lambda_handler(dr_submit_event, mocker):
    app.lambda_handler(dr_submit_event, "")
