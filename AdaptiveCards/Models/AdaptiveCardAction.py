from http import HTTPStatus
from botbuilder.core.teams import TeamsActivityHandler
from botbuilder.core import CardFactory
from botbuilder.schema.teams import TabResponse, TabResponsePayload, TabSuggestedActions
from botbuilder.schema import CardAction
import http
import json
import os

# Card response for task module invoke request
def invokeTaskResponse():
  return type('',(),
    {
      'status': HTTPStatus.OK,
      'body': {
          'task': {
              'type': "continue",
              'value': {
                  'card': {
                      'contentType': "application/vnd.microsoft.card.adaptive",
                      'content': adaptiveCardTaskModule
                  },
                  'heigth': 250,
                  'width': 400,
                  'title': 'Sample Adaptive Card'
              }
          }
      }
    })()

# Card response for tab fetch request
async def createFetchResponse(userImage, displayName):
  print("Create Invoke response")
  # imageString = '';

  # if userImage != None:
  #     # Converting image of Blob type to base64 string for rendering as image.
  #     await userImage.arrayBuffer().then(result => {
  #         console.log(userImage.type);
  #         imageString = Buffer.from(result).toString('base64');
  #         if (imageString != '') {
  #             // Writing file to Images folder to use as url in adaptive card
  #             fs.writeFileSync("Images/profile-image.jpeg", imageString, { encoding: 'base64' }, function (err) {
  #                 console.log("File Created");
  #             });
  #         }
  #     }).catch(error => { console.log(error) });
  # }

  return type('',(),
    {
      'status': HTTPStatus.OK,
      'body': {
          'tab': {
              'type': "continue",
              'value': {
                  'cards': [
                      {
                          # 'card': getAdaptiveCardUserDetails(imageString, displayName),
                          'card': getAdaptiveCardUserDetails('', displayName),
                      },
                      {
                          'card': getAdaptiveCardSubmitAction(),
                      }
                  ]
              },
          },
      }
  })()

# Card response for tab submit request
def createSubmitResponse():
  print("Submit response")
  return type('',(),
    {
      'status': HTTPStatus.OK,
      'body': {
          'tab': {
              'type': "continue",
              'value': {
                  'cards': [
                      {
                          'card': signOutCard,
                      }
                  ]
              },
          },
      }
  })()

# Card response for tab submit request
def taskSubmitResponse():
  print("Task Submit response")
  return type('',(),
  {
    'status': HTTPStatus.OK,
    'body': {
        'task': {
            'value': {
                'tab': {
                    'type': "continue",
                    'value': {
                        'cards': [
                            {
                                'card': taskSubmitCard
                            }
                        ]
                    }
                }
            },
            'type': "continue"
        },
        'responseType': "task"
    }
})()

# Adaptive Card with user image, name and Task Module invoke action
def getAdaptiveCardUserDetails(image, name):
  return type('', (), {
      '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
      'body': [
          {
              'type': "ColumnSet",
              'columns': [
                  {
                      'type': "Column",
                      'items': [
                          {
                              'type': "Image",
                              'url': os.environ.get("BaseUrl") + "/Images/profile-image.jpeg" 
                                    if (image != None) and (image != '') 
                                    else "https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg",
                              'size': "Medium"
                          }
                      ],
                      'width': "auto"
                  },
                  {
                      'type': "Column",
                      'items': [
                          {
                              'type': "TextBlock",
                              'weight': "Bolder",
                              'text': 'Hello: ' + name,
                              'wrap': True
                          },
                      ],
                      'width': "stretch"
                  }
              ]
          },
          {
              'type': 'ActionSet',
              'actions': [
                  {
                      'type': "Action.Submit",
                      'title': "Show Task Module",
                      'data': {
                          'msteams': {
                              'type': "task/fetch"
                          }
                      }
                  }
              ]
          }
      ],
      'type': 'AdaptiveCard',
      'version': '1.4'
  })()

# Adaptive Card showing sample text and Submit Action
def getAdaptiveCardSubmitAction():
  return type('', (), {
      '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
      'body': [
          {
              'type': 'Image',
              'height': '300px',
              'width': '400px',
              'url': 'https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg',
          },
          {
              'type': 'TextBlock',
              'size': 'Medium',
              'weight': 'Bolder',
              'text': 'tab/fetch is the first invoke request that your bot receives when a user opens an Adaptive Card tab. When your bot receives the request, it either sends a tab continue response or a tab auth response',
              'wrap': True,
          },
          {
              'type': 'TextBlock',
              'size': 'Medium',
              'weight': 'Bolder',
              'text': 'tab/submit request is triggered to your bot with the corresponding data through the Action.Submit function of Adaptive Card',
              'wrap': True,
          },
          {
              'type': 'ActionSet',
              'actions': [
                  {
                      'type': 'Action.Submit',
                      'title': 'Sign Out',
                  }
              ],
          }
      ],
      'type': 'AdaptiveCard',
      'version': '1.4'
  })()

# Adaptive Card to show in task module
adaptiveCardTaskModule = type('', (), {
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
  'version': '1.4'})()

# Adaptive Card to show sign out action
signOutCard = type('', (), {
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
})()

# Adaptive Card to show task/submit action
taskSubmitCard = type('', (), {
    '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
    'body': [
        {
            'type': 'TextBlock',
            'size': 'Medium',
            'weight': 'Bolder',
            'text': 'The action called task/submit. Please refresh to laod contents again.',
            'wrap': True,
        }
    ],
    'type': 'AdaptiveCard',
    'version': '1.4'
})()
