# WiFi configuration
WIFI_SSID = 'MYWIFISSID'
WIFI_PASS = 'MYSECUREPASSWORD'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'XXXXXXXXXXXX-ats.iot.us-east-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/aws_root.ca'
AWS_CLIENT_CERT = '/flash/cert/aws_client.cert'
AWS_PRIVATE_KEY = '/flash/cert/aws_private.key'

################## Subscribe / Publish client #################
CLIENT_ID = 'PycomPublishClient'
TOPIC = 'dt/plant1/001/aggregate' # Subscribe Topic
TOPIC = 'dt/plant1/002/aggregate' # Publish Topic
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'dt/plant1/001/aggregate'
LAST_WILL_MSG = 'To All: Last will message'
