from InstagramAPI import InstagramAPI
import pprint
import os

user = os.environ.get('DB_USER')
password = os.environ.get('INST_KINGALIEN_PASS')
api = InstagramAPI(user, password)
api.USER_AGENT = 'Instagram 10.34.0 Android (18/4.3; 320dpi; 720x1280; Xiamo; HM ISW; armani; qcom; en_US)'


def get_my_profile_details():
    api.login()
    api.getSelfUsernameInfo()
    result = api.LastJson
    formated_print = pprint.pformat(result)
    print(formated_print)

get_my_profile_details()