from deepracer.boto3_enhancer import deepracer_client


def lambda_handler(event, context):
    model_arn = event['ModelArn']
    leaderboard_arn = event['LeaderboardArn']
    dr_client = deepracer_client()
    latest_submission = dr_client.get_latest_user_submission(LeaderboardArn=leaderboard_arn)['LeaderboardSubmission']
    if latest_submission['LeaderboardSubmissionStatusType'] == 'SUCCESS':
        print("No running leaderboard submissions were found. Creating a new one.")
        return dr_client.create_leaderboard_submission(ModelArn=model_arn, LeaderboardArn=leaderboard_arn)
    print('There is a currently running leaderboard submission. Please see its status as the lambda output.')
    return latest_submission['LeaderboardSubmission']

