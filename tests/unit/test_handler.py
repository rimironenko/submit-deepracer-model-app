import pytest

from submit_model import app


@pytest.fixture()
def dr_submit_event():
    return {
        "ModelArn": "",
        "LeaderboardArn": ""
    }


def test_lambda_handler(dr_submit_event, mocker):
    app.lambda_handler(dr_submit_event, "")
