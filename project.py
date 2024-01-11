import time
from Body.listen import hearing
import pyautogui as ui
from Body.speak import *
import random

dlg = [
    "Sure, sir.",
    "Creating.",
    "Just a while, sir.",
    "Working on project creation.",
    "Initializing project.",
    "Almost there, sir.",
    "Generating project files.",
    "This won't take long.",
    "Preparing project structure.",
    "Creating a masterpiece, sir.",
    "Hold on, sir.",
    "Let me handle it.",
    "In progress, sir.",
    "Your project is on the way.",
    "Sit tight, sir.",
    "Executing project creation.",
    "Building your project.",
    "Creating magic, sir.",
    "Your project is coming to life.",
    "Just a moment, sir.",
    "Processing your request.",
    "Project initiation in progress.",
    "Creating the future, sir.",
    "Cooking up something special, sir.",
    "Sit back and relax, sir.",
    "Project creation in full swing.",
    "Don't blink, sir. It's happening.",
    "Engaging project creation protocol.",
    "This will be amazing, sir.",
    "Working diligently on your project.",
    "Crafting your project with care.",
    "Initiating project creation sequence.",
    "Hold your excitement, sir.",
    "Your project is in good hands.",
    "Building dreams, sir.",
    "Constructing your project masterpiece.",
    "Preparing to impress, sir.",
    "Creating wonders for you.",
    "Project creation in the works.",
    "Your project is getting ready.",
    "We're making progress, sir.",
    "Generating brilliance, sir.",
    "Your project is on the way.",
    "Creating innovation, sir.",
    "Strap in, sir. It's project time!",
    "Just a little longer, sir.",
    "Your project is our priority.",
]

dlg2 = [
    "Sir, could you please share the project's name?",
    "Any preferences for the project name, sir?",
    "I'm ready to hear the name of your project, sir.",
    "A great project needs a great name, what's your choice, sir?",
    "The project is coming along nicely. What should we call it, sir?",
    "Naming the project is always exciting, sir. Your suggestion?",
    "Ready when you are, sir! What's the project's name?",
    "Let's give your project a standout name, sir. What do you think?",
    "Exciting times, sir! What shall we name the project?",
    "Sir, the project creation awaits its unique name. Any ideas?",
    "In the world of coding, a good project name is key. Your thoughts, sir?",
    "Your project, your name, sir! What's the chosen name?",
    "Ready for the next step, sir! What's the project's name?",
    "A project without a name is like a code without comments. What's your pick, sir?",
    "Sir, the project creation journey continues. What's the name?",
    "Projects come and go, but a good name sticks. What's your choice, sir?",
    "Every project has a story, and it starts with a name. Your decision, sir?",
    "Naming the project is the first step to bringing it to life. Your call, sir!",
    "The project canvas is ready. What masterpiece name shall we paint on it, sir?",
    "Creating a project is like naming a child. What's our project's name, sir?",
    "Sir, the project is eager to introduce itself. What name do you have in mind?",
    "A project with a name is a project with an identity. Your choice, sir?",
    "Let's add a touch of your creativity to the project name, sir. Any suggestions?",
    "Sir, the project creation journey is incomplete without its name. What's your idea?",
    "Ready to set the project on its way with a unique name. What's your pick, sir?",
    "Sir, the project is like a book waiting for its title. What should we call it?",
    "The project creation process is on hold until we have a name, sir. Your input?",
    "A project without a name is just a collection of code. What shall we name it, sir?",
    "Sir, the project is like a ship without a name. What should we name it before it sets sail?",
    "Naming the project is our next mission. Your thoughts, sir?",
    "The project creation journey continues with a name. What's your suggestion, sir?",
    "Every project has a personality, and it starts with a name. Your choice, sir?",
    "The project is in the cocoon stage. What beautiful name will it emerge with, sir?",
    "A project with a name is a project with a soul. What name shall we give it, sir?",
    "Naming the project is the finishing touch before it begins. What's your choice, sir?",
    "Sir, the project is ready to take its first step. What name shall we give it for this journey?",
    "A project without a name is like a melody without lyrics. What name shall we give it, sir?",
    "The project creation symphony continues. What name shall we add to its notes, sir?",
    "Sir, naming the project is our current quest. What title shall we bestow upon it?",
    "The project is eager to introduce itself to the world. What name shall we give it, sir?",
    "A project without a name is like a puzzle without a picture. What name fits the picture, sir?",
    "The canvas is set, sir. What name shall we paint on it for this project?",
    "Naming the project is like giving it a passport. What name shall we put on its identity, sir?",
    "Sir, the project is ready for its christening. What name shall we baptize it with?",
    "Every project needs a name to shine. What name shall we give this shining star, sir?",
    "Sir, the project creation journey continues. What name shall we etch into its code?",
    "The project is knocking on the door of the digital world. What name shall we open the door with, sir?",
]
dlg3 = [
    "Is it a large project, sir?",
    "Are we working on a big project, sir?",
    "Considering the scope, is this project on the larger side, sir?",
    "Is the project size substantial, sir?",
    "Is the project expected to be significant in scale, sir?",
    "Are we dealing with a sizable project, sir?",
    "Is the project in the category of being large-scale, sir?",
    "In terms of size, would you describe this project as large, sir?",
    "Is the project on the larger end of the scale, sir?",
    "Given the nature of the project, is it considered to be large, sir?",
    "Do we have a substantial project on our hands, sir?",
    "Is this project falling into the category of being a large-scale endeavor, sir?",
    "Considering the complexity, would you say this is a large project, sir?",
    "Is the project size expected to be on the larger side, sir?",
    "Given the requirements, is this project categorized as large, sir?",
    "In terms of project size, are we looking at a larger project, sir?",
    "Is the project scope considerable, sir?",
    "Are we dealing with a project of substantial size, sir?",
    "Is the project's magnitude leaning towards being large, sir?",
    "Is the project expected to be of a larger scale, sir?",
    "Considering the workload, would you categorize this project as large, sir?",
    "Is the project's scale on the larger end, sir?",
    "Given the objectives, is this project on the larger side, sir?",
    "In terms of project size, is it fair to say this is a larger project, sir?",
    "Is the project's scale considerable, sir?",
    "Considering the project's goals, is it a larger project, sir?",
    "Is the project size substantial, sir?",
    "Are we looking at a project that falls into the larger category, sir?",
    "Is this project expected to be of considerable size, sir?",
    "Considering the requirements, is this project considered to be large, sir?",
    "Is the project scope on the larger side, sir?",
    "Given the complexity, is this project categorized as large, sir?",
    "Is the project anticipated to be of a larger scale, sir?",
    "Considering the workload, would you describe this project as large, sir?",
    "Is the project magnitude leaning towards being large, sir?",
    "Is the project expected to be on the larger end of the scale, sir?",
    "Given the objectives, would you say this is a larger project, sir?",
    "Is the project's scale on the larger end, sir?",
    "Considering the goals, is this project on the larger side, sir?",
]
dlg4 = [
    "Let's talk about subdirectory count, sir.",
    "Could you please tell me about the subfolder count, sir?",
    "When it comes to the project structure, how many subdirectories are we looking at, sir?",
    "Shifting our focus, sir, how many subfolders are there in the project?",
    "Exploring the project's organization, sir, can you share the count of subdirectories?",
    "Diving into the project's file system, sir, do you have the count of subfolders?",
    "Considering the project's directory structure, sir, how many subdirectories are there?",
    "Taking a closer look at the organization, sir, can you provide the count of subfolders?",
    "In the context of project directories, sir, how many subdirectories do we have?",
    "Let's delve into the directory details, sir. How many subfolders are part of the project?",
    "Talking about the project's file arrangement, sir, what's the count of subdirectories?",
    "Focusing on the project's layout, sir, could you share the subfolder count with me?",
    "Shifting our attention to the project structure, sir, do you know how many subdirectories there are?",
    "Examining the project's organization, sir, can you tell me the count of subfolders?",
    "Turning our focus to the directories, sir, how many subdirectories are present in the project?",
    "Discussing the project's file arrangement, sir, what's the count of subdirectories?",
    "Exploring the directory structure, sir, can you provide the count of subfolders?",
    "Let's talk about the organization of the project, sir. How many subdirectories are there?",
    "Considering the project's file system, sir, do you have the count of subfolders?",
    "Diving into the project's directory structure, sir, how many subdirectories are there?",
    "Taking a closer look at the organization, sir, can you provide the count of subfolders?",
    "In the context of project directories, sir, how many subdirectories do we have?",
    "Let's delve into the directory details, sir. How many subfolders are part of the project?",
    "Talking about the project's file arrangement, sir, what's the count of subdirectories?",
    "Focusing on the project's layout, sir, could you share the subfolder count with me?",
    "Shifting our attention to the project structure, sir, do you know how many subdirectories there are?",
    "Examining the project's organization, sir, can you tell me the count of subfolders?",
    "Turning our focus to the directories, sir, how many subdirectories are present in the project?",
    "Discussing the project's file arrangement, sir, what's the count of subdirectories?",
]
dlg5 = [
    "What is the name of the subdirectory, sir?",
    "Sir, could you please tell me the name of the subdirectory?",
    "When it comes to subdirectories, sir, can you share the name of the one you're referring to?",
    "Exploring the project's directory structure, sir, what's the name of the subdirectory?",
    "Diving into the organization, sir, could you provide the name of the subdirectory?",
    "Considering the subdirectories, sir, which one are we talking about? Can you share the name?",
    "In the context of project directories, sir, could you tell me the name of the subdirectory?",
    "Shifting our focus to subdirectories, sir, what's the name of the one you have in mind?",
    "Talking about the subdirectory, sir, can you provide its name?",
    "Exploring the project's file arrangement, sir, which subdirectory are we discussing? Name, please.",
    "Focusing on the subdirectories, sir, do you have a specific one in mind? What's its name?",
    "Shifting our attention to the directory structure, sir, can you tell me the name of the subdirectory?",
    "Examining the project's organization, sir, what's the name of the subdirectory in question?",
    "Turning our focus to subdirectories, sir, which one do you want to discuss? Can you share the name?",
    "Discussing the project's file arrangement, sir, which subdirectory are you referring to? Name, please.",
    "Exploring the directory structure, sir, do you have a specific subdirectory in mind? What's its name?",
    "Let's talk about the organization of subdirectories, sir. Which one are we focusing on? Name, please.",
    "Considering the project's file system, sir, could you tell me the name of the subdirectory?",
    "Diving into the subdirectories, sir, which one is on your mind? Can you share its name?",
    "Taking a closer look at the organization, sir, what's the name of the subdirectory you're interested in?",
    "In the context of project directories, sir, can you tell me the name of the subdirectory?",
    "Let's delve into the details of subdirectories, sir. What's the name of the one you're referring to?",
    "Talking about the subdirectory, sir, can you provide its name?",
    "Focusing on the subdirectories, sir, do you have a specific one in mind? What's its name?",
    "Shifting our attention to the directory structure, sir, can you tell me the name of the subdirectory?",
    "Examining the project's organization, sir, what's the name of the subdirectory in question?",
    "Turning our focus to subdirectories, sir, which one do you want to discuss? Can you share the name?",
    "Discussing the project's file arrangement, sir, which subdirectory are you referring to? Name, please.",
    "Exploring the directory structure, sir, do you have a specific subdirectory in mind? What's its name?",
    "Let's talk about the organization of subdirectories, sir. Which one are we focusing on? Name, please.",
]
dlg6 = [
    "So you want to create more directories, sir?",
    "Can I create one more directory, sir?",
    "Considering the project's structure, sir, are we looking to add another directory?",
    "Thinking about the organization, sir, do you want to create an additional directory?",
    "In the context of project directories, sir, are we planning to introduce another one?",
    "Exploring the project's file system, sir, are you considering the creation of another directory?",
    "Considering the directory structure, sir, is the idea to add one more directory?",
    "Focusing on the project's layout, sir, are we discussing the addition of another directory?",
    "In terms of project directories, sir, do you want to create an additional one?",
    "Let's talk about the organization of directories, sir. Are we planning to create one more?",
    "Examining the project's organization, sir, is the plan to introduce another directory?",
    "Turning our focus to directories, sir, are we considering the creation of another one?",
    "Discussing the project's file arrangement, sir, do you want to add another directory?",
    "Exploring the directory structure, sir, are you thinking about creating one more directory?",
    "Let's discuss the addition of directories, sir. Are we planning to create another one?",
    "Thinking about the project's layout, sir, can we create one more directory?",
    "Considering the organization of directories, sir, are we looking to add another one?",
    "In the context of project directories, sir, do you want to introduce an additional one?",
    "Focusing on the project's file system, sir, is the idea to create another directory?",
    "Examining the directory structure, sir, are we planning to add one more directory?",
    "Turning our focus to directories, sir, do you want to create an additional one?",
    "Discussing the project's organization, sir, is the plan to introduce another directory?",
    "Exploring the addition of directories, sir, are we considering the creation of another one?",
    "Let's talk about the project's layout, sir. Are we thinking about creating one more directory?",
    "Thinking about the organization, sir, do you want to add another directory?",
    "Considering the project's file arrangement, sir, are we planning to create another directory?",
    "Examining the directory structure, sir, is the idea to add one more directory?",
    "Turning our focus to directories, sir, do you want to create an additional one?",
    "Discussing the project's file system, sir, are you considering the creation of another directory?",
    "Exploring the organization of directories, sir, are we looking to add another one?",
]

dl7 = [
    "alright boss no problem",
    "sure boss",
    "understood sir, as you wish",
    "affirmative sir",
    "roger that boss",
    "got it sir",
    "no problem boss",
    "acknowledged sir",
    "as you command boss",
    "okay sir, understood",
    "very well boss",
    "right away sir",
    "no issues boss",
    "affirmative, proceeding as directed",
    "message received sir",
    "absolutely boss",
    "all clear sir",
    "copy that boss",
    "noted sir",
    "consider it done boss",
    "will do sir",
    "certainly boss",
    "yes sir, no problem",
    "affirmative, boss",
    "ok sir, as you wish",
    "okey sir, just asking",
    "roger that sir",
    "received boss",
    "clear sir",
    "no worries boss",
    "sure thing sir",
    "on it boss",
    "acknowledged, proceeding as instructed",
    "aye aye sir",
    "message received loud and clear boss",
    "very well sir",
    "no problemo boss",
    "acknowledged, sir",
    "understood, boss",
    "okie dokie sir",
    "right away boss",
    "acknowledged and understood sir",
    "all good boss",
    "as you wish sir",
    "acknowledged and proceeding sir",
    "ok sir, got it",
    "absolutely sir",
    "clear as crystal boss"
]
def create_directory():
    time.sleep(1)
    ui.hotkey("ctrl", "shift", "n")
    choice_dlg5 = random.choice(dlg5)
    print(choice_dlg5)
    speak(choice_dlg5)
    name = hearing()
    ui.write(name)
    ui.hotkey("enter")
    choice_dlg6 = random.choice(dlg6)
    speak(choice_dlg6)
    condition = hearing().lower()
    if "yes" in condition or "yes it is" in condition or "it is" in condition or "ya" in condition or "make insider" in condition or "make sub directory" in condition or "do it" in condition:
        choice_dlg4 = random.choice(dlg4)
        speak(choice_dlg4)
        create_directory()
    else:
        dl7c = random.choice(dl7)
        speak(dl7c)

def project_creator():
    choice_dlg = random.choice(dlg)
    print(choice_dlg)
    speak(choice_dlg)
    ui.hotkey("win","d")
    time.sleep(1)
    ui.hotkey("ctrl","shift","n")
    choice_dlg2 = random.choice(dlg2)
    print(choice_dlg2)
    speak(choice_dlg2)
    name = hearing()
    ui.write(name)
    choice_dlg3 = random.choice(dlg3)
    speak(choice_dlg3)
    condition = hearing().lower()
    if "yes" in condition or "yes it is" in condition or "it is" in condition or "ya" in condition or "make insider" in condition or "make sub directory" in condition or "do it" in condition:
        choice_dlg4 = random.choice(dlg4)
        speak(choice_dlg4)
        ui.hotkey("enter")
        ui.hotkey("enter")
        create_directory()
        # while True:
    elif "no" in condition or "no need" in condition or "nhi" in condition:
        choice_dlga = random.choice(dl7)
        speak(choice_dlga)
    else:
        pass











