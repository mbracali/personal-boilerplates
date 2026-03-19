# Import the random library
import random

# Import the tomllib library
import tomllib

# Import fast API router 
from fastapi import APIRouter

# Create a router object
router = APIRouter()

# Store all the game oneliners in a list
GAME_ONE_LINERS = [
    "War. War never changes... - Narrator",
    "It's a-me, Mario! - Mario Mario",
    "Get over here! - Scorpion",
    "The cake is a lie. - GLaDOS",
    "I used to be an adventurer like you, then I took an arrow to the knee. - Guard",
    "Hey you, you're finally awake. - Ralof of Riverwood",
    "Stay awhile and listen. - Deckard Cain",
    "It's time to kick ass and chew bubblegum... and I'm all outta gum. - Duke Nukem",
    "All your base are belong to us. - CATS",
    "A man chooses, a slave obeys. - Andrew Ryan",
    "Kept you waiting, huh? - Solid Snake",
    "You are a horrible person. - Chloe Price",
    "Nothing is true, everything is permitted. - Ezio Auditore",
    "Grass grows, birds fly, sun shines, and brother, I hurt people. - The scout",
    "You were almost a Jill sandwich! - Barry Burton",
    "Do you get to the Cloud District very often? Oh, what am I saying, of course you don't. - Nazeem",
    "Life is cruel. Of this I have no doubt. - Queen Myrrah",
    "Death can have me when it earns me. - Kratos",
    "Do not be sorry, be better! - Kratos",
    "Boy! - Kratos",
    "<-- You died --> - Soulsborn",
    "Would you kindly? - Atlas",
    "Thank you Mario! But our princess is in another castle! - Toad",
    "Take this, is dangerous to go alone!",
    "Do a barrel roll! - Peppy Hare",
    "Finish him! - Ed Boon (??)",
    "Toasty! - Ed Boon (??)",
    "The right man in the wrong place can make all the difference in the world. - G-Man",
    "No gods or kings. Only man. - Andrew Ryan",
    "I have a plan. - Dutch van der Linde",
    "Press F to pay respects.",
    "Hey! Listen! - Navi",
    "What is a man? A miserable little pile of secrets! - Dracula",
    "Hadouken! - Ryu",
    "Praise the Sun! - Solaire of Astora",
    "Got to go fast! - Sonic the Hedgehog",
    "I need a wepon! - Master Chief",
    "I am the great mighty poo, and I'm going to throw my s*** at you. - Great Mighty Poo",
    "Snake? Snake? SNAAAAAAAAAAAAAAKEEEEE! - Colonel Campbell",
    "MO - MO - MO - MO - MONSTER KILL! - Announcer",
    "Unf - Doomguy",
    "Wind's howling. - Geralt of Rivia",
    "I should go. - Commander Shepard",
    "50,000 people used to live here. Now it's a ghost town. - Captain MacMillan",
    "Ah shit, here we go again. - CJ",
    "All we had to do was follow the damn train, CJ! - Big Smoke",
    "Stop right there, criminal scum! - Imperial Guard",
    "Objection! - Phoenix Wright",
    "It's super effective!",
    "I never asked for this. - Adam Jensen",
    "Wololo - Priest",
    "Nanomachines, son! - Senator Armstrong",
    "Why are we still here? Just to suffer? - Kazuhira Miller",
    "Rise and shine, Mr. Freeman. - G-Man",
    "LEEEROOOOY JENKIIIIINS!",
    "You have died of dysentery.",
    "Falcon Punch! - Captain Falcon",
    "Rip and tear, until it is done.",
    "Hesitation is defeat. - Isshin Ashina",
    "I am malenia blade of miquella and i have never known defeat - Malenia",
    "The fallen leaves tell a story...",
    "Wasted.",
    "Fatality! - Ed Boon (??)",
    ]

@router.get("/game_one_liners", status_code=200)
def game_one_liners():
    """ Return a one liner from a random video-game. """

    # Return on random oneliners
    one_liner = random.choice(GAME_ONE_LINERS)

    return {"message": one_liner}
