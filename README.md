# Reddit-Scraper
This is a Reddit scraper that goes through the following subreddits: r/k12sysadmin and r/k12cybersecurity. Reddit is a server where people around the world share their experiences in a certain topic, making it a possibly relevant sosurce to figuring out what teachers/tech admin themselves see and experience in school. To investigate the security issues regarding tech in k-12 education, the scraper provides the tools to go through hundreds of reddit posts regarding security issues and pull out the ones relevant to the research focus. You can also access and change the variables in the documentation.yaml file. That is where the names of the subreddits that will be scanned and the keywords will live. The date range from which you want the posts to be from will be collected in the terminal as the code runs. All posts--including the date of post, top 2 comments, body and title of the post--will be documented into a JSON and CSV file. 

# How to Use

1. Enter virtual environment
2. Install requirements and packages
   You can run the following code to install all the packages used in the code:
   ```python
   pip install -r requirements txt .
   ```
4. Change post limit and keywords in the YAML file.
   The variables for post limit is POST_LIMIT and keywords is KEYWORDS.
5. Run the code

# Usage

After running the code, all submission titles, comments, and the details of each post will be found in the JSON file. The full file path of the JSON file will be found at the bottom of the terminal. Data on the size of the JSON elemets will also be found in the output in the terminal. 

#Example Configurations

Only maximum of 20 posts and 2 comments:
```python
CLIENT_ID: Jomt_btpXsBqac61X3cO_Q
CLIENT_SECRET: BxnFNZ8VGgwjo2GYuE17EzmAHh8w2w
COMMENT_LIMIT: 2
POST_LIMIT: 30
```

Maximum date:
```python
End Date: 2025-08-02 13:36:27.823893
```
Scraping k12 cybersecurity related subreddits/submissions:
```python
KEYWORDS:
- cyber
- firewall
- network
- security
- k12
- school
- edtech
- domain
- block
- ai
- artifical
- intelligence
- vulnerabilities
- issue
- problem
- difficulties
OUTPUT_CSV: k12_firewall_posts.csv
OUTPUT_JSON: k12_firewall_posts.json
SUBREDDITS:
- k12sysadmin
- k12cybersecurity
Start Date: 2025-01-01 00:00:00
USER_AGENT: k12-cybersec-scraper/0.1 by TopEducator9706
```
