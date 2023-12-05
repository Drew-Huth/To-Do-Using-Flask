import snowflake.connector

conn = snowflake.connector.connect(
    user = 'JOE',
    password = 'Closer92',
    account = 'https://eq96204.ca-central-1.aws.snowflakecomputing.com/'
)

cs = conn.cursor()

# try:
#     cs.execute('')