import os
import json
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

from utils.cache import get_cache_file, put_cache_file

load_dotenv()

slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_team_id = os.environ["SLACK_TEAM_ID"]
client = WebClient(token=slack_token)
logger = logging.getLogger(__name__)

"""
List users:
1. From cache file if exists
2. From Slack users_list endpoint and write cache file for future use
https://api.slack.com/methods/admin.users.list
"""
try:
    file_name = f"user-list-{slack_team_id}.json"
    cached_members = get_cache_file(file_name)
    if cached_members is None:
        response = client.users_list(team_id=slack_team_id)
        members = json.dumps(response["members"], indent=4)
        logger.info(members)
        put_cache_file(file_name, members)
    else:
        cached_members = json.loads(cached_members)
        logger.info("Listing cached users")
        for user in cached_members:
            logger.info(json.dumps(user, indent=2))

except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    logger.error(f"Got an error: {e.response['error']}")