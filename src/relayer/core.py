import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handler(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
