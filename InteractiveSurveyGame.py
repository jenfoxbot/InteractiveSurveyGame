#Makey Makey Survey Game!
#Written by Jennifer Fox <jenfoxbot@gmail.com>
'''----------------------------------------------------------------------------
 * "THE COFFEE-WARE LICENSE" (Revision 42):
 * <jenfoxbot@gmail.com> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a coffee in return.
 * ----------------------------------------------------------------------------
 '''
from __future__ import print_function
import subprocess

#Create/Open file to store survey results
file = open('SurveyResults.txt', 'a')

#Matrix to store questions -- change/add questions to customize your survey
questions = ['What is your favorite mythical creature?', 'What is your favorite breakfast?',
             'What is your favorite subject in school?']

#Dictionary to store question choices -- change/add responses for each question. 
#Change dictionary keys to reflect Makey Makey header pin letter assignments
choices = [{'w' : 'Dragon, duh', 'a' : 'Unicorn forever!', 's' : 'Hippogriff, because why', 'd' : 'Do faeries count?', 'f' : 'Yoda, me choose'},
           {'w': 'Toast!', 'a': 'Eggs & Bacon', 's': 'Pancakes', 'd': 'Oatmeal', 'f': 'Bagel and cream cheese'},
           {'w': 'Science/Math!', 'a': 'Art/Music!', 's' : 'English/Writing', 'd': 'History/Philosophy', 'f': 'All of them!'}]
    
#Ask survey question and print choices, take response, return reponse
def takeVote(questionNum, questions, choices):
    message = format('Question %s: %s \n Choices: %s. \n' %(questionNum, questions, sorted(choices.values())))
    vote = getValidInput(message, choices.keys())

    return choices[vote]


#Require user to validate survey choice (prevents random inputs)
def checkVote(vote):
    print("Your vote is: ", vote, "\n")
    
    #Reprogram two Makey Makey into 'y' and 'n' keys, or switch key codes to correspond to existing Makey Makey assignments (e.g. 'g' or ' ')
    response = getValidInput('Is this correct? Please select the "yes" or "no" touch pads. ', ['y', 'n'])

    if response == 'y':
        print("Success!! \n You have voted for: ", vote, "\n Next question loading...", end = '\n\n')
        return True
    elif response == 'n':
        print("Resetting choice...", end = '\n\n')
        return False


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
                            
