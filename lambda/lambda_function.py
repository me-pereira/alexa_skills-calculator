# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Bem vindo a calculadora. Por favor, informe a operação e, em seguida, dois números."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SomaHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SomaIntent")(handler_input)

    def handle(self, handler_input):
        primeironumerosoma = handler_input.request_envelope.request.intent.slots["primeironumerosoma"].value
        segundonumerosoma = handler_input.request_envelope.request.intent.slots["segundonumerosoma"].value
        
        float_primeironumerosoma = float(primeironumerosoma)
        float_segundonumerosoma = float(segundonumerosoma)
        
        resultadosomaraw = float_primeironumerosoma + float_segundonumerosoma
        
        if resultadosomaraw % 1 == 0:
            resultadosoma = int(resultadosomaraw)
        else:
            resultadosoma = "{:.2f}".format(resultadosomaraw)
        
        resultadosoma_str = str(resultadosoma)
        
        speak_output = "A soma dos valores é igual a " + resultadosoma_str + " !"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class SubtracaoHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SubtracaoIntent")(handler_input)

    def handle(self, handler_input):
        primeironumerosubtracao = handler_input.request_envelope.request.intent.slots["primeironumerosubtracao"].value
        segundonumerosubtracao = handler_input.request_envelope.request.intent.slots["segundonumerosubtracao"].value
        
        float_primeironumerosubtracao = float(primeironumerosubtracao)
        float_segundonumerosubtracao = float(segundonumerosubtracao)
        
        resultadosubtracaoraw = float_segundonumerosubtracao - float_primeironumerosubtracao
        
        if resultadosubtracaoraw % 1 == 0:
            resultadosubtracao = int(resultadosubtracaoraw)
        else:
            resultadosubtracao = "{:.2f}".format(resultadosubtracaoraw)
        
        resultadosubtracao_str = str(resultadosubtracao)
        
        speak_output = "A subtração dos valores é igual a " + resultadosubtracao_str + " !"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class MultiplicacaoHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MultiplicacaoIntent")(handler_input)

    def handle(self, handler_input):
        primeironumeromultiplicacao = handler_input.request_envelope.request.intent.slots["primeironumeromultiplicacao"].value
        segundonumeromultiplicacao = handler_input.request_envelope.request.intent.slots["segundonumeromultiplicacao"].value
        
        float_primeironumeromultiplicacao = float(primeironumeromultiplicacao)
        float_segundonumeromultiplicacao = float(segundonumeromultiplicacao)
        
        resultadomultiplicacaoraw = float_primeironumeromultiplicacao * float_segundonumeromultiplicacao
        
        if resultadomultiplicacaoraw % 1 == 0:
            resultadomultiplicacao = int(resultadomultiplicacaoraw)
        else:
            resultadomultiplicacao = "{:.2f}".format(resultadomultiplicacaoraw)
        
        resultadomultiplicacao_str = str(resultadomultiplicacao)
        
        speak_output = "A multiplicação dos valores é igual a " + resultadomultiplicacao_str + " !"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )

class DivisaoHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DivisaoIntent")(handler_input)

    def handle(self, handler_input):
        primeironumerodivisao = handler_input.request_envelope.request.intent.slots["primeironumerodivisao"].value
        segundonumerodivisao = handler_input.request_envelope.request.intent.slots["segundonumerodivisao"].value
        
        float_primeironumerodivisao = float(primeironumerodivisao)
        float_segundonumerodivisao = float(segundonumerodivisao)
        
        resultadodivisaoraw = float_primeironumerodivisao / float_segundonumerodivisao
        
        if resultadodivisaoraw % 1 == 0:
            resultadodivisao = int(resultadodivisaoraw)
        else:
            resultadodivisao = "{:.2f}".format(resultadodivisaoraw)
        
        resultadodivisao_str = str(resultadodivisao)
        
        speak_output = "A divisão de " + primeironumerodivisao + " por " + segundonumerodivisao + " é igual a " + resultadodivisao_str + " !"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Nesta skill, você pode somar, subtrair, multiplicar ou dividir valores. Basta falar o nome da operação, seguido de dois números."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Até a próxima!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, eu não entendi. Você pode somar, subtrair, multiplicar ou dividir dois números. Caso queira saber mais, diga ajuda. Oque você gostaria de fazer?"
        reprompt = "Não entendi! Como posso te ajudar?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, não pude processar seu pedido. Por favor tente novamente."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(SomaHandler())
sb.add_request_handler(SubtracaoHandler())
sb.add_request_handler(MultiplicacaoHandler())
sb.add_request_handler(DivisaoHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()