import praw
import config
import time
import os


def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="EL_Bekh's First BOT")
    return r


def run_bot(r, comments):
    print("is it working?")
    for comment in r.subreddit('StardustCrusaders').comments(limit=30):
        if "DIO" in comment.body and comment.id not in comments:
            comment.reply("ROADROLLAAAAAAA")
            comments.append(comment.id)
            with open("comments", "a") as f:
                f.write(comment.id + "\n")
    print("It is working...")
    time.sleep(5)


def get_comments():
    if not os.path.isfile("comments"):
        comments = []
    else:
        with open("comments.txt", "w+") as f:
            comments = f.read()
            comments = comments.split("\n")
            comments = comments.filter(None, comments)
            print("error")
    return comments


r = bot_login()
comments = get_comments()
while True:
    run_bot(r, comments)
