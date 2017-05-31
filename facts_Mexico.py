from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
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

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hola! Say give me a fact to know more about Mexico"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Say give me a fact to know more about Mexico"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you, please come back soon "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
                                                
#this Functions handles the questionaire
def facts(intent, session):
    facts_ = ["The official name of Mexico is United Mexican States",
              "A Mexican tamale called the zacahuil is three feet long and weighs about 150 pounds",
              "The largest wildcat in North America is the jaguar, which can be found in Mexico's southern jungles.",
              "The first printing press in North America was used in Mexico City in 1539.",
              "The National University of Mexico was founded in 1551 by Charles V of Spain and is the oldest university in North America.",
              "Relative to their bodies, Chihuahuas have the biggest brain in the dog world.",
              "The Chihuahua is the worlds smallest dog and is named for a Mexican state.",
              "Millions of monarch butterflies migrate to Mexico every year from the U.S. and Canada, though logging operations are rapidly destroying their habitat.",
              "The border between Mexico and the United States is the second largest border in the world (only the U.S.-Canadian border is longer).",
              "Mexico’s size is 756,066 square miles, which is almost three times larger than Texas.",
              "Mexican children do not receive presents on Christmas Day. They receive gifts on January 6, the day on which Mexicans celebrate the arrival of the Three Wise Men.",
              "Mexico City is built over the ruins of a great Aztec city, Tenochtitlán. Because it is built on a lake, Mexico is sinking at a rate of 6 to 8 inches a year as pumps draw water out for the city’s growing population.",
              "Mexico’s flag is made up three vertical stripes. The left green stripe stands for hope, the middle white stripe represents purity, and the right red stripe represents the blood of those who died fighting for Mexico's independence. The picture of an eagle eating a snake is based on an Aztec legend.",
              "The red poinsettia (which the Aztecs called cuetlaxochitl) originated in Mexico and is named after Joel Roberts Poinsett, the first United States ambassador to Mexico (in the 1820s).",
              "Only ten countries in the world have a larger population than Mexico’s 109,955,400 people.",
              "Mexico City has the highest elevation and is oldest city in North America. It is also one of the largest cities in the world.",
              "Mexico is the 14th largest country in the world by total area.",
              "Modern Mexicans are a unique blend of many ancient civilizations, including the Olmec, Zapotec, Toltec, Maya, Aztec, Inca, African, French, and Spanish.",
              "The first great civilization in Mexico were the Olmecs (1400-300 B.C.) who established many cities along the eastern coast of Mexico, sculpted the famous Colossal Heads, and worshipped a mysterious, unnamed god that was part human and part jaguar.",
              "The Zapotec civilization (600 B.C.-A.D. 800) established great cities along southern Mexico and developed the first writing system in the Americas.",
              "Catholicism is the dominate religion in Mexico",
              "Mexico is second only to Brazil in the number of Catholic citizens.",
              "One unusual Mayan weapon was a “hornet bomb,” which was an actual hornet’s nest thrown at enemies during battle.",
              "Snakes appear repeatedly in Mexican mythology, from the serpent god Kukulcan which can be found the side of the Chichen Itza pyramid to the feathered serpent god, Quetzalcoatl.",
              "The Aztecs adopted human sacrifice from earlier cultures (such as the Olmecs) because they believed the universe would come to an end and the sun would cease to move without human blood. There are many ancient statues of gods sticking out their togues, such as Huitzilopochtli, which may be a sacred gesture that suggests their thirst for blood.",
              "In the fourteenth century, a group of Chichmecas (warrior nomads) called the Aztecs (or Mexicas) settled in Mexico when they saw an eagle (representing the sun) standing on a cactus (a symbol of the heart) clutching a snake (a symbol of the earth or Quetzalcoatl)—an image which is now depicted on the Mexican flag.",
              "Mexico is home to the world's smallest volcano, which stands just 43 feet (13 meters) tall,",
              "Mexico is located in the “Ring of Fire,” one of the earth’s most violent earthquake and volcano zones.",
              "During an Aztec human sacrifice, five priests, sometimes with their faces painted with different colors, held the sacrificial victims’ arms and legs. The heart, referred to as “precious eagle cactus fruit,” was cut from the live victim and burned on a fire in the temple.",
              "Shells and stones on the Aztecs' ritual blades symbolized the faces of the gods for which the sacrificial hearts were intended. They would sacrifice between 10,000 to 50,000 victims per year. Under the rule of Montezuma II, 12,000 victims were sacrificed in one day.",
              "The Aztecs played ritual ball game known as tlachtli in which the losers were often sacrificed to the gods. 
              "Mexico is home to a very rare rabbit called the volcano rabbit which lives near Mexican volcanoes. 
              "The descendants of the Aztecs speak a form of the Aztec language called Nahuatl. Many of its words, particularly for types of food, passed into English...such as tomatoes (tomatl), chocolate (chocolatl), and avocados (ahuacatl).",
              "About 60% of the modern Mexican population is mestizo (Indian-Spanish), 30% is Indian or predominately Indian, 9% is Caucasian, and 1% is other.",
              "Hernan Cortés had a native mistress and able translator Marina (La Malinche). She gave birth to his first son, who is considered the first mestizo (Indian-Spanish).",
              "Creoles are descendants of the Spanish people who first arrived in Mexico. Now they are the name of Mexico's small population: Caucasian Europeans, Americans, and Canadians.",
              "Mexico remained under Spanish control for nearly 300 years until the Mexican people, led by a priest named Father Hidalgo, rose up against the Spanish on September 16, 1810. Hidalgo is widely considered the father of modern Mexico, and Mexican Independence is celebrated on September 15-16.",
              "When Spanish Conquistador Hernan Cortés arrived in 1519, the Aztecs believed he was their returning god, Quetzalcoatl, and offered him the drink of the gods: hot chocolate.",
              "Spanish conquerors brought bullfighting to Mexico, and, second to Spain, Mexico now has the most bullfighting rings in the world. Bullfighting takes place from November to April, and the Plaza Mexico is the largest bullring in the world.",
              "Cacao was a highly valued commodity in pre-Hispanic Mexico",
              "Mexico introduced chocolate, corn, and chilies to the world.",
              "While the charreada (a competitive sport similar to a rodeo) is Mexico's national sport, fútbol (soccer in the U.S.) is currently more popular.",
              "Texas was a Mexican province which declared its independence from Mexico in 1836, resulting in war with the United States (1836-1838).",
              "In 1910, under the guidance of Emiliano Zapata and Pancho Villa, Mexican peasants revolted against the dictatorship of Porfirio Díaz to gain equality and land. The civil war lasted 10 years and took the lives over 1 million people.", 
              "Before 1958, women could not vote in presidential elections. Women, however, did play an important role in the 1910 revolution, serving as spies, arms smugglers, and soldaderas or soldiers.",
              "In 1994, a group of Mexican peasants and farmers called the Zapatistas (named after Emiliano Zapata) started another revolt to highlight the differences between the rich and poor.",
              "The Great Pyramid of Cholula is also known as Tlachihualtepetl, which is Nahuatl for artificial mountain",
              "The largest pyramid in the world is the Great Pyramid of Cholula in Mexico. It is also the largest monument ever constructed in the world.",
              "Even though over 50 native tongues are still spoken in rural locations, Spanish is the national language of Mexico. In fact, Mexico is the most populated Spanish-speaking country in the world.",
              "The North Atlantic Free Trade Association (NAFTA) was created in 1994 to encourage trade among the United States, Canada, and Mexico. But NAFTA has largely failed to lift Mexico out of poverty due to Mexico's repeated economic crises, a weak public education system, government corruption, and Mexico's inability to enforce the rule of law.",
              "Actor Anthony Quinn was the first Mexican to win an Academy Award for his role in the 1952 movies Viva Zapata.",
              "The Chichen Itza Pyramid in Mexico was named one of the new Seven Wonders of the World.",
             "According to the California Avocado Commission, Americans consume up to 81 million pounds of avocados on Cinco de Mayo every year."
             ]
    return facts_[8]

def handle_fact(intent, session):
    session_attributes = {}
    card_title = "Fact Teller"
    speech_output = facts()
    reprompt_text = None
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyFact":
        return handle_fact(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


#####
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

