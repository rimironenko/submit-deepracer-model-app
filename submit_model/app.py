from deepracer.boto3_enhancer import deepracer_client


def lambda_handler(event, context):
    model_arn = event['ModelArn']
    leaderboard_arn = event['LeaderboardArn']
    dr_client = deepracer_client()
    latest_submission = dr_client.get_latest_user_submission(LeaderboardArn=leaderboard_arn)['LeaderboardSubmission']
    last_submission_status = latest_submission['LeaderboardSubmissionStatusType']
    if last_submission_status == 'SUCCESS':
        print("No running leaderboard submissions were found. Creating a new one.")
        dr_client.create_leaderboard_submission(ModelArn=model_arn, LeaderboardArn=leaderboard_arn)
    elif last_submission_status == 'FAILED' or last_submission_status == 'ERROR':
        print("Latest submission was failed. Still creating a new one.")
        dr_client.create_leaderboard_submission(ModelArn=model_arn, LeaderboardArn=leaderboard_arn)
    else:
        print('There is a currently running leaderboard submission. Skipping.')
