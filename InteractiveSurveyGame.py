#Makey Makey Survey Game!
#Written by Jennifer Fox <jenfoxbot@gmail.com>
'''----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <jenfoxbot@gmail.com> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.
 * ----------------------------------------------------------------------------
 '''
from __future__ import print_function
import subprocess

#Create/Open file to store survey results
file = open('SurveyResults.txt', 'a')

#Matrix to store questions -- change/add questions to customize your survey
questions = ['How did you find this survey?', 'What is your favorite part of the museum?',
             'What is your favorite subject in school?']

#Dictionary to store question choices -- change/add responses for each question. Change dictionary keys to reflect Makey Makey 
choices = [{'w' : 'I knew it was here!', 'a' : 'Stumbled upon it!', 's' : 'Not really sure how I got here...', 'd' : 'Was told to check it out by another person.', 'f' : 'Intuition.'},
           {'w': 'This survey!', 'a': 'Butterfly house!', 's': 'Planetarium!', 'd': 'Interactive exhibits!', 'f': 'All of it!'},
           {'w': 'Science/Math!', 'a': 'Art/Music!', 's' : 'English/Writing', 'd': 'History/Philosophy', 'f': 'All of them!'}]
    
#Ask survey question and print choices, take response, return reponse
def takeVote(questionNum, questions, choices):
    message = format('Question %s: %s \n Choices: %s. \n' %(questionNum, questions, choices.values()))
    vote = getValidInput(message, choices.keys())

    return choices[vote]


#Require user to validate survey choice (prevents random inputs)
def checkVote(vote):
    print("Your vote is: ", vote, "\n")
    
    response = getValidInput('Is this correct? Please select the "yes" or "no" touch pads. ', [' ', 'n'])

    if response == ' ':
        print("Success!! \n You have voted for: ", vote, "\n Next question loading...", end = '\n\n')
        return True
    elif response == 'n':
        print("Resetting choice...", end = '\n\n')
        return False

    return check

#Function ensures that user inputs a valid response
def getValidInput(message, valid_inputs):
    while True:
        response = input(message)
        if len(response) == 0:
            print("Whoops! Something broke.. Try again!", end = '\n\n')
        elif response[0] in valid_inputs:
            return response[0]
        else:
            print("Sorry -- Your selection is not possible. Please try again.", end = '\n\n')

#Run the survey -- cycle through each question and corresponding choices, log user response if user validates choice. 
def takeSurvey():
    print("Welcome to the Survey Game! Please choose your survey responses using the objects in front of you.", end = '\n\n')

        #For each question, take a vote
    for i, question in enumerate(questions):
        vote = takeVote(i+1, questions[i], choices[i])
        #For each vote, check user validation -- if False (aka "no"), re-ask same question
        while not checkVote(vote):
            vote = takeVote(i+1, questions[i], choices[i])
        file.write(questions[i] + '\t' + vote + '\n')



def main():
    print("Makey Makey Survey Game. \n Designed by Jennifer Fox <jenfoxbot@gmail.com>", end = '\n\n')

    try:
        while True:
            takeSurvey()
    except KeyboardInterrupt:
        file.close()

if __name__ == '__main__':
    main()

file.close()
                            