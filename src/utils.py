import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def build_speechlet_response(title, output, reprompt_text=None, should_end_session=False):
    """
    Build JSON structure for Alexa response.
    """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "Zork: " + title,
            'content': "Zork: " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def log(msg, request, session, level=logging.INFO):
    log_data = {
        "sessionId": session['sessionId'],
        "requestId": request['requestId'],
        "message": msg
    }
    logger.log(level, json.dumps(log_data))
