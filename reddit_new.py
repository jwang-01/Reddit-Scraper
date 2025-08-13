import praw
from fuzzywuzzy import fuzz
import csv
import os 
import json
from datetime import datetime
import time
import yaml 


# --- Configuration ---

yaml_file = 'documentation.yaml'

with open(yaml_file, 'r') as file:
        yfile = yaml.safe_load(file)
        print(yfile)


CLIENT_ID = yfile['CLIENT_ID']
CLIENT_SECRET = yfile['CLIENT_SECRET']
USER_AGENT = yfile['USER_AGENT']

OUTPUT_CSV = yfile['OUTPUT_CSV']
OUTPUT_JSON = yfile['OUTPUT_JSON']

SUBREDDITS = yfile['SUBREDDITS']


KEYWORDS = yfile['KEYWORDS'] # @Jill edit this
POST_LIMIT = yfile['POST_LIMIT']      # number of posts to fetch per subreddit @Jill edit this
COMMENT_LIMIT = yfile['COMMENT_LIMIT']     # top comments per post 

print(os.path.abspath(yaml_file))

# --- Initialize Reddit API ---
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# --- Get Subreddits ---

relevant_subs = [(name, None) for name in SUBREDDITS]

print("Scanning the following subreddits only:")
for name, _ in relevant_subs:
    print(f"- r/{name}")

print(f"Found {len(relevant_subs)} relevant subreddits:")
for name, count in relevant_subs:
    print(f"- r/{name} ({count} subscribers)")

# --- Prepare CSV (write header once) ---
fieldnames = ['subreddit', 'title', 'url', 'created_utc', 'score', 'num_comments']
with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
# --- Collect posts, append to CSV, and build JSON data ---

all_posts = []
for name, _ in relevant_subs:
    how_post = 0
    subreddit = reddit.subreddit(name)
    print(f"Date for {name}")
    print(f"Initial: {how_post}")
    while True:
            try:
                x = datetime.fromisoformat(input("Start Date (YYYY-MM-DD):"))
                #last_date = x
                #print(last_date)
            except ValueError:
                continue
            break
    while True:
        try:
            y = datetime.fromisoformat(input("End Date (YYYY-MM-DD):"))
        except ValueError:
            y = datetime.now()
            print(f"End Date: {y}")
        break
    #while how_post < POST_LIMIT: 
    for submission in subreddit.new(limit=POST_LIMIT):
        subreddit = reddit.subreddit(name)
        text = (submission.title + '' + submission.selftext).lower()
        # set time parameter yourself in input
        #if last_date == x:
            #x = x
        #elif last_date != x:
            #x = last_date
        post_date = datetime.fromtimestamp(submission.created_utc)
        if not any(kw in text for kw in KEYWORDS):
            continue
        elif not (x < post_date < y):
            continue
        how_post += 1

            

        # Fetch top comments
        submission.comments.replace_more(limit=0)
        top_comments = []
        for comment in submission.comments[:COMMENT_LIMIT]:
            top_comments.append({'author': str(comment.author), 'body': comment.body})

        post_data = {
            'subreddit': name,
            'title': submission.title,
            'body' : submission.selftext,
            'url': submission.url,
            'created_utc': submission.created_utc,
            'score': submission.score,
            'num_comments': submission.num_comments,
            'top_comments': top_comments
        }
        all_posts.append(post_data)
        # Append metadata row to CSV immediately
        row = {k: post_data[k] for k in fieldnames}
        with open(OUTPUT_CSV, 'a', newline='', encoding='utf-8') as f_append:
            writer = csv.DictWriter(f_append, fieldnames=fieldnames)
            writer.writerow(row)
        print(f"[+] Appended: r/{name} – \"{submission.title[:50]}…\" {post_date} {str(how_post)}")
        #x = post_date
        #time.sleep(0.5)  # respectful rate‑limit
    #maybe loop?
        #if how_post < POST_LIMIT:
            #continue
        #elif how_post == POST_LIMIT:
            #break
print(f"Final: {how_post}")

# --- Write JSON output ---
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f_json:
    json.dump(all_posts, f_json, indent=2)

print(f"\nDone! CSV growing live in {OUTPUT_CSV}, final JSON in {OUTPUT_JSON}.")
print("Data has been written to 'documentation.yaml'")

#yaml file
data = {
    'CLIENT_ID' : 'Jomt_btpXsBqac61X3cO_Q',
    'CLIENT_SECRET' : 'BxnFNZ8VGgwjo2GYuE17EzmAHh8w2w',
    'USER_AGENT' : 'k12-cybersec-scraper/0.1 by TopEducator9706',
    'OUTPUT_CSV' : 'k12_firewall_posts.csv',
    'OUTPUT_JSON' : 'k12_firewall_posts.json',
    'SUBREDDITS' : ['k12sysadmin','k12cybersecurity'],
    'KEYWORDS' : ['cyber', 'firewall', 'network', 'security', 'k12', 'school', 'edtech', 
             'domain', 'block', 'ai', 'artifical', 'intelligence', 'vulnerabilities', 
             'issue', 'problem', 'difficulties'],
    'POST_LIMIT' : 10,
    'COMMENT_LIMIT' : 2,
    'Start Date' : x,
    'End Date' : y,
    'yaml_file' : 'documentation.yaml'
}

def log():
    print(f"Date: {datetime.now()}")
    with open(OUTPUT_JSON, 'r') as file:
        reddit_list = json.load(file)
    json_details = {"Columns" : len(post_data) ,
                    "Rows" : len(reddit_list)}
    for d in json_details:
        print(f"{d}: {json_details[d]}\n")

    print("Content Included:")
    for z in post_data:
        print(f"{z}\n")
    with open(yaml_file, 'r') as file:
        yfile = yaml.safe_load(file)
        for i in yfile:
            print(f"{i} = {yfile[i]}\n")

    print(f"JSON File Path: {os.path.abspath(OUTPUT_JSON)}\n")
    
    print(f'YAML File: {os.path.abspath(yaml_file)}')

log()