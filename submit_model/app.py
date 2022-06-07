from deepracer.boto3_enhancer import deepracer_client


def lambda_handler(event, context):
    dr_client = client = deepracer_client()
    models = dr_client.list_models(ModelType="REINFORCEMENT_LEARNING", MaxResults=100)["Models"]
    return models

