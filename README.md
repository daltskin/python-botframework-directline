# python-botframework-directline
Example Python for calling Bot Framework via the DirectLine API (v3)

For further details refer to the API documentation here: 
[http://dev.botframework.com](https://docs.microsoft.com/en-us/bot-framework/rest-api/bot-framework-rest-direct-line-3-0-concepts
)
1. Register your bot on the dev.botframework.com portal
2. Enable the DirectLine Channel and copy the secret key
3. Add you key below and run

Usage example

bot = DirectLineAPI('{your-direct-line-secret-here}')
bot.send_message("Hi")
botresponse = bot.get_message()
print botresponse