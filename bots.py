import dataset
import random

bot_names = ["Einstein", "Napoleon the Tall", "realDonaldTrump", "Ye", "Alan Turing (Mr.Robot)"]


def einsteinResponse(alt1):
    alt2 = random.choice(dataset.positive_verbs_ING)
    responseList = [f'[Einstein]: I love to {alt1}. Its one of my favorite things, besides studying the universe.',
                    f'[Einstein]: That sounds splendid! Can we do that after I done {alt2}?',
                    f'[Einstein]: {alt1} is ok, but can we not go {alt2} or do you like something to do with science?',
                    f'[Einstein]: I thing I will go and play chess with Niels Bohr.']
    return random.choice(responseList)


def napoleonResponse(alt1):
    alt2 = random.choice(dataset.positive_verbs_ING)
    responseList = [f'[Napoleon the tall]: I like to {alt1} too, but have you ever tried {alt2}?',
                    f'[Napoleon the tall]: Mon dieu! I hate to {alt1}!',
                    f'[Napoleon the tall]: {alt1}?? Cant we invade the russians first?',
                    f'[Napoleon the tall]: Viva la France!!',
                    f'[Napoleon the tall]: 1....2.... lets {alt1}!!']
    return random.choice(responseList)


def trumpResponse(alt1):
    alt2 = random.choice(dataset.positive_verbs_ING)
    responseList = [f'[realDonaldTrump]: I will make america great again! But first, lets {alt1}.',
                    f'[realDonaldTrump]: Its no fun to {alt1}. I will just win anyway, by a landslide.',
                    f'[realDonaldTrump]: You are fired!',
                    f'[realDonaldTrump]: You are hired!',
                    f'[realDonaldTrump]: Can you not go and ask sleepyJoe to {alt1}? I want to go {alt2} instead.']
    return random.choice(responseList)


def kanyeResponse(alt1):
    alt2 = random.choice(dataset.positive_verbs_ING)
    responseList = [f'[Ye]: I fell like Im too busy writing history to read it. Thats why I dont have time to {alt1}.',
                    f'[Ye]: I love to {alt1}! Its my favorite.',
                    f'[Ye]: LOL!',
                    f'[Ye]: I have to decided to run for president in 2024! Do you want to by my vise president?',
                    f'[Ye]: God told me: To {alt1} is so bad for you. {alt2} is so much better.']
    return random.choice(responseList)


def turingResponse(alt1):
    alt2 = random.choice(dataset.positive_verbs_ING)
    responseList = [f'[Alan Turing (Mr.Robot)]: Can machines {alt1}?',
                    f'[Alan Turing (Mr.Robot)]: A computer would deserve to be called intelligent if it could deceive a human into beliving that it can {alt1}. Right?',
                    f'[Alan Turing (Mr.Robot)]: We may hope that a computer can compete with you when you {alt1}',
                    f'[Alan Turing (Mr.Robot)]: I want to build a machine more powerful than my brain! Then I wont need to {alt1}']
    return random.choice(responseList)


available_bots = [einsteinResponse, napoleonResponse, trumpResponse, kanyeResponse, turingResponse]
banned_char = [",", ".", "!", "?"]
 

def bot(message: str):
    
    # Filters message to make it readable
    for c in banned_char:
        message.replace(c, "")
    msg_array = message.lower().split()
    wordFound = ""

    #If the message is a greeting than a random bot greets the client
    if msg_array[1] in dataset.greetings:
        return f'[{random.choice(bot_names)}]: {random.choice(dataset.greetings)}!' 

    #Checks if there is any known word in the database that can be used to respond with.
    for msg in msg_array:
        if msg in dataset.positive_verbs:
            wordFound = msg
            break

    #If not, then chooses a random word.
    if wordFound == "":
        wordFound = random.choice(dataset.positive_verbs)

    return random.choice(available_bots)(wordFound)
    
