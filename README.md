# Reddit-Scraper
This is a Reddit scraper that goes through the following subreddits: r/k12sysadmin and r/k12cybersecurity. Reddit is a server where people around the world share their experiences in a certain topic, making it a possibly relevant sosurce to figuring out what teachers/tech admin themselves see and experience in school. To investigate the security issues regarding tech in k-12 education, the scraper provides the tools to go through hundreds of reddit posts regarding security issues and pull out the ones relevant to the research focus. You can also access and change the variables in the YAML file. That is where the names of the subreddits that will be scanned and the keywords will live. The date range from which you want the posts to be from will be collected in the terminal as the code runs. All posts--including the date of post, top 2 comments, body and title of the post--will be documented into a JSON and CSV file. 

#How to Use

1. Enter virtual environment
2. Install requirements and packages
   You can run the following code to install all the packages used in the code: pip install -r requirements txt .
3. Change post limit and keywords in the YAML file.
   The variables for post limit is POST_LIMIT and keywords is KEYWORDS.
4. Run the code
