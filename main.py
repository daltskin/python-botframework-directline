"""Python sample to call Bot Framework using DirectLine v3 API"""

# Start here for documentation: https://docs.microsoft.com/en-us/bot-framework/rest-api/bot-framework-rest-direct-line-3-0-concepts"""
# For Generating a token vs start conversation: https://docs.microsoft.com/en-us/bot-framework/rest-api/bot-framework-rest-direct-line-3-0-authentication
# Here we use start conversation as we'll be calling the bot immediately

import requests

class DirectLineAPI(object):
    """Shared methods for the parsed result objects."""

    def __init__(self, direct_line_secret):
        self._direct_line_secret = direct_line_secret
        self._base_url = 'https://directline.botframework.com/v3/directline'
        self._set_headers()
        self._start_conversation()

    def _set_headers(self):
        headers = {'Content-Type': 'application/json'}
        value = ' '.join(['Bearer', self._direct_line_secret])
        headers.update({'Authorization': value})
        self._headers = headers

    def _start_conversation(self):
        # For Generating a token use
        # url = '/'.join([self._base_url, 'tokens/generate'])
        # botresponse = requests.post(url, headers=self._headers)
        # jsonresponse = botresponse.json()
        # self._token = jsonresponse['token']

        # Start conversation and get us a conversationId to use
        url = '/'.join([self._base_url, 'conversations'])
        botresponse = requests.post(url, headers=self._headers)

        # Extract the conversationID for sending messages to bot
        jsonresponse = botresponse.json()
        self._conversationid = jsonresponse['conversationId']

    def send_message(self, text):
        """Send raw text to bot framework using directline api"""
        url = '/'.join([self._base_url, 'conversations', self._conversationid, 'activities'])
        jsonpayload = {
            'conversationId': self._conversationid,
            'type': 'message',
            'from': {'id': 'user1'},
            'text': text
        }
        botresponse = requests.post(url, headers=self._headers, json=jsonpayload)
        if botresponse.status_code == 200:
            return "message sent"
        return "error contacting bot"

    def get_message(self):
        """Get a response message back from the botframework using directline api"""
        url = '/'.join([self._base_url, 'conversations', self._conversationid, 'activities'])
        botresponse = requests.get(url, headers=self._headers,
                                   json={'conversationId': self._conversationid})
        if botresponse.status_code == 200:
            jsonresponse = botresponse.json()
            return jsonresponse['activities'][1]['text']
        return "error contacting bot for response"



