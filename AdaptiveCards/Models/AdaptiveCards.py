from http import HTTPStatus

from botbuilder.core import (
    CardFactory
)

# Card response for authentication
def createAuthResponse (signInLink):
    adaptive_card = {
        "status": HTTPStatus.OK,
        "body": {
            "tab": {
                "type": "auth",
                "suggestedActions": {
                    "actions": [
                        {
                            "type": "openUrl",
                            "value": signInLink,
                            "title": "Sign in to this app"
                        }
                    ]
                }
            },
        }
    }

    return CardFactory.adaptive_card(adaptive_card)

def  createFetchResponse(userImage, displayName):
    adaptive_card = {
        "status": HTTPStatus.OK,
        "body": {
            "tab": {
                "type": "continue",
                "value": {
                    "cards": [
                        {
                            "card": getAdaptiveCardUserDetails(userImage, displayName),
                        },
                        {
                            "card": getAdaptiveCardSubmitAction(),
                        }
                    ]
                },
            },
        }
    }

    return CardFactory.adaptive_card(adaptive_card)

# Adaptive Card with user image, name and Task Module invoke action
def getAdaptiveCardUserDetails(image, name):
    if (image and image != ''):
        image = f"data:image/png;base64, {image}"
    else:
        image = "https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg"

    adaptive_card = {
        "$schema": 'http://adaptivecards.io/schemas/adaptive-card.json',
        "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "url": image,
                                "size": "Medium"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": 'Hello: ' + name,
                                "wrap": True
                            },
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": 'ActionSet',
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Show Task Module",
                        "data": {
                            "msteams": {
                                "type": "task/fetch"
                            }
                        }
                    }
                ]
            }
        ],
        "type": 'AdaptiveCard',
        "version": '1.4'
    }
  
    return adaptive_card

# Adaptive Card showing sample text and Submit Action
def getAdaptiveCardSubmitAction():
    return {
        "$schema": 'http://adaptivecards.io/schemas/adaptive-card.json',
        "body": [
            {
                "type": 'Image',
                "height": '157px',
                "width": '300px',
                "url": 'https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg',
            },
            {
                "type": 'TextBlock',
                "size": 'Medium',
                "weight": 'Bolder',
                "text": 'tab/fetch is the first invoke request that your bot receives when a user opens an Adaptive Card tab. When your bot receives the request, it either sends a tab continue response or a tab auth response',
                "wrap": True,
            },
            {
                "type": 'TextBlock',
                "size": 'Medium',
                "weight": 'Bolder',
                "text": 'tab/submit request is triggered to your bot with the corresponding data through the Action.Submit function of Adaptive Card',
                "wrap": True,
            },
            {
                "type": 'ActionSet',
                "actions": [
                    {
                        "type": 'Action.Submit',
                        "title": 'Sign Out',
                    }
                ],
            }
        ],
        "type": 'AdaptiveCard',
        "version": '1.4'
    };

def invokeTaskResponse():
    adaptiveCard = {
        "status": HTTPStatus.OK,
        "body": {
            "task": {
                "type": 'continue',
                "value": {
                    "card": {
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "content": adaptiveCardTaskModule()
                    },
                    "heigth": 250,
                    "width": 400,
                    "title": 'Sample Adaptive Card'
                }
            }
        }
    }

    return CardFactory.adaptive_card(adaptiveCard)

# Adaptive Card to show in task module
def adaptiveCardTaskModule():
    return {
        '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
        'body': [
            {
                'type': 'TextBlock',
                'size': 'Medium',
                'weight': 'Bolder',
                'text': 'Sample task module flow for tab'
            },
            {
                'type': 'Image',
                'height': '50px',
                'width': '50px',
                'url': 'https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg',
            },
            {
                'type': 'ActionSet',
                'actions': [
                    {
                        'type': "Action.Submit",
                        'title': "Close",
                        'data': {
                            'msteams': {
                                'type': "task/submit"
                            }
                        }
                    }
                ]
            }
        ],
        'type': 'AdaptiveCard',
        'version': '1.4'}

# Card response for tab submit request
def taskSubmitResponse():
  adaptive_card = {
    'status': HTTPStatus.OK,
    'body': {
        'task': {
            'value': {
                'tab': {
                    'type': "continue",
                    'value': {
                        'cards': [
                            {
                                'card': taskSubmitCard()
                            }
                        ]
                    }
                }
            },
            'type': "continue"
        },
        'responseType': "task"
    }
  }

  return CardFactory.adaptive_card(adaptive_card)

# Adaptive Card to show task/submit action
def taskSubmitCard():
    return {
        '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
        'body': [
            {
                'type': 'TextBlock',
                'size': 'Medium',
                'weight': 'Bolder',
                'text': 'The action called task/submit. Please refresh to load contents again.',
                'wrap': True,
            }
        ],
        'type': 'AdaptiveCard',
        'version': '1.4'
    }

# Card response for tab submit request
def createSubmitResponse():
  adaptive_card = {
      'status': HTTPStatus.OK,
      'body': {
          'tab': {
              'type': "continue",
              'value': {
                  'cards': [
                      {
                          'card': signOutCard(),
                      }
                  ]
              },
          },
      }
  }

  return CardFactory.adaptive_card(adaptive_card)

# Adaptive Card to show sign out action
def signOutCard():
    return {
    '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
    'body': [
        {
            'type': 'TextBlock',
            'size': 'Medium',
            'weight': 'Bolder',
            'text': 'Sign out successful. Please refresh to Sign in again.',
            'wrap': True,
        }
    ],
    'type': 'AdaptiveCard',
    'version': '1.4'
}