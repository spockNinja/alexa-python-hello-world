from utils import (
    build_response,
    build_speechlet_response,
    log
)


def get_welcome_response(session):
    """
    Welcome the user to my python skill
    """

    card_title = "Welcome"
    speech_output = "Welcome to my python skill. You can search for pypi packages. "

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask me to search pypi for a package. "

    session_attributes = session.get('attributes', {})

    speechlet_response = build_speechlet_response(
        card_title,
        speech_output,
        reprompt_text
    )
    return build_response(session_attributes, speechlet_response)


def handle_session_end_request():
    """
    Say goodbye to the user.
    """
    card_title = "Session Ended"
    speech_output = "Thank you for using my python skill. Have a nice day! "

    speechlet_response = build_speechlet_response(
        card_title,
        speech_output,
        should_end_session=True
    )
    return build_response({}, speechlet_response)


def on_session_started(session_started_request, session):
    """
    Called when a new session is started.
    """
    log('session started', session_started_request, session)


def on_launch(launch_request, session):
    """
    Called when the user launches the skill without a command.
    """
    log('on_launch', launch_request, session)

    return get_welcome_response(session)


def on_intent(intent_request, session):
    """
    Called when the user specifies an intent for this skill.
    """

    log('on_intent', intent_request, session)

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response(session)
    elif intent_name in ["AMAZON.CancelIntent", "AMAZON.StopIntent", "AMAZON.PauseIntent"]:
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.

    *Not called when the skill returns should_end_session=true*
    """
    log('session ended', session_ended_request, session)
    # add any cleanup logic here


def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest, etc.)

    The JSON body of the request is provided in the event parameter.
    """

    # TODO uncomment once you have an app id
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    request = event['request']
    session = event['session']
    request_type = request['type']

    if session['new']:
        on_session_started(request, session)

    if request_type == "LaunchRequest":
        return on_launch(request, session)
    elif request_type == "IntentRequest":
        return on_intent(request, session)
    elif request_type == "SessionEndedRequest":
        return on_session_ended(request, session)
