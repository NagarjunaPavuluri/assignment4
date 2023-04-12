import json
import boto3


with open('config.json') as f:
    config = json.load(f)

topicName = config['topicName']
Ucmo= config['Ucmo']
personal = config['personal']
print(topicName)
sns = boto3.client('sns')
response = sns.create_topic(Name=topicName)
topicArn = response['TopicArn']
ucmoSubscription = sns.subscribe(
    TopicArn=topicArn,
    Protocol='email',
    Endpoint=Ucmo
)
personalSubscription = sns.subscribe(
    TopicArn=topicArn,
    Protocol='email',
    Endpoint=personal
)
print("UCMO Subscription ARN: " + ucmoSubscription['SubscriptionArn'])
print("Personal Subscription ARN: " + personalSubscription['SubscriptionArn'])
#nagarjuna