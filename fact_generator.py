# -*- coding: utf-8 -*-



from numpy.random import randint
import pandas as pd

from twython import Twython
from auth import (
        consumer_key,
        consumer_secret,
        access_token, 
        access_token_secret
        )

twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

master_list = pd.read_csv("fact_factory.csv")

people = master_list["people"].dropna()
territories = master_list["countries"].dropna()

def pick_year():
    year = str(randint(0,2019))
    return year


person = people[randint(0, len(people))]
territory = territories[randint(0, len(territories))]

parts = [person, " invaded ", territory, " in ", pick_year(), " CE"]

def make_tweet():
    sentence = "".join(part for part in parts)
    return sentence

tweet = make_tweet()

twitter.update_status(status=tweet)