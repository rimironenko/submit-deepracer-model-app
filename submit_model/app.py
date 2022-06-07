from deepracer.boto3_enhancer import deepracer_client


def lambda_handler(event, context):
    model_arn = event['ModelArn']
    leaderboard_arn = event['LeaderboardArn']
    dr_client = deepracer_client()
    # models = dr_client.list_models(ModelType="REINFORCEMENT_LEARNING", MaxResults=100)["Models"]
    return dr_client.create_leaderboard_submission(model_arn, leaderboard_arn)

