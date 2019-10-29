import typing

def topic() -> typing.List[typing.Dict[str, typing.Any]]:
    return [{
        'Type': 'Notification',
        'MessageId': '<message-id>',
        'TopicArn': 'arn:aws:sns:us-east-1:<aws-account-id>:billingTest',
        'Subject': 'AWS Budgets: billingThree has exceeded your alert threshold',
        'Message': 'AWS Budget Notification October 28, 2019\nAWS Account <aws-account-id>\n\nDear AWS Customer,\n\nYou requested that we alert you when the ACTUAL Cost associated with your billingThree budget is greater than $24.00 for the current month. The ACTUAL Cost associated with this budget is $36.69. You can find additional details below and by accessing the AWS Budgets dashboard [1].\n\nBudget Name: billingThree\nBudget Type: Cost\nBudgeted Amount: $30.00\nAlert Type: ACTUAL\nAlert Threshold: > $24.00\nACTUAL Amount: $36.69\n\n[1] https://console.aws.amazon.com/billing/home#/budgets\n',
        'Timestamp': '2019-10-28T15:56:27.357Z',
        'SignatureVersion': '1',
        'Signature': '<redacted>',
         'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-<hash>.pem',
         'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:<aws-account-id>:billingTest:<message-id>',
         'MessageAttributes': {}
    }]

