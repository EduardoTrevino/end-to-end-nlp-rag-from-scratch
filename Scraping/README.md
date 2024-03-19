# **All of our Scrapers for CMU Data**
## **Overview**
This project comprises a Python script (**'webScholar_scraper.ipynb'** or .py) designed to scrape open-access papers from CMU faculty members affiliated with the Language Technologies Institute (LTI) for the year 2023. The scraper fetches metadata including the title, abstract, authors, publication venue, year, and a brief summary (TLDR) of each paper.

Following the scraping process, a subsequent script (**'validating_unique_authors.py'** located within the cleaning_webscholar_data folder) cleans, formats, and filters the data based on author IDs to ensure data integrity and relevance.

This project comprises other Python scripts designed to scrape various data related to Carnegie Mellon University (CMU), specifically course listings, and news articles. Each script is tailored for specific data extraction tasks, providing a comprehensive toolkit for CMU-related data gathering and processing.
**'scraping_courses.ipynb'** extracts CMU course listings.
**'buggynewsscript.py'** gathers content from CMU news articles.

## Getting Started
### Prerequisites
* Python 3.6 or higher
* **'requests'** library for making API requests
* **'pickle'** for data serialization and storage
* **'beautifulsoup4'** library for parsing HTML content
### Installation
Clone the repository or download the source code.
Install the required Python libraries using pip:
```
pip install requests beautifulsoup4
```
### Usage
#### Scraping Research Papers
Navigate to the directory containing **'webScholar_scraper.ipynb**' (or .py for terminal users).
Run the script using Jupyter Notebook or as a Python script:
For Jupyter Notebook:
```
jupyter notebook webScholar_scraper.ipynb
```
For terminal:
```
python webScholar_scraper.py
```
This script will collect data from Semantic Scholar API and serialize it into a .pkl file for subsequent processing.

Cleaning and Validating
Navigate to the **'cleaning_webscholar_data'** directory.
Run the **'validating_unique_authors.py'** script to process the serialized data:
```
python validating_unique_authors.py
```
This step cleans the data, formats it appropriately, and filters out records to ensure each author ID is unique and correctly associated with the corresponding paper.
#### Scraping Course Listings

Extracts and saves CMU course listings for a specific term from the official course schedule layout.
Navigate to the directory containing **'scraping_courses.ipynb**'.
Run the script using Jupyter Notebook:
Jupyter Notebook:
```
jupyter notebook scraping_courses.ipynb
```
Course listings are saved to **'raw.txt'**, providing a raw HTML snapshot of the course schedule.

#### Scraping Buggy News Content

Scrapes and saves text content from specified CMU news articles.
Navigate to the directory containing **'buggynewsscript.py**'.
Run the script using the terminal:
Terminal:
```
python buggynewsscript.py
```
News article content is saved to  **'content_output.txt'**, stripping HTML tags and formatting for readability.


### Data Format
#### Research Papers 
The research paper data is serialized and stored in a .pkl file, containing a dictionary with faculty names as keys and their respective papers' metadata as values. This metadata includes:

* Paper ID
* Title
* Abstract
* Publication Venue
* Year
* TLDR summary
* Embedding vector (if available)
* Authors (including Author IDs)

#### Course listings
The course listings are saved in a **'raw.txt'** file containing the HTML of the course listings page.

#### News Content
The buggy news content is saved in a **'content_output.txt'** containing the cleaned text of news articles.

### Limitations and Considerations
The scraper adheres to Semantic Scholar's API rate limits by pausing for 1 second between requests.
It's essential to replace the api_key variable with your own Semantic Scholar API key for authentication.
Data accuracy and completeness depend on the availability and openness of paper information on Semantic Scholar.
