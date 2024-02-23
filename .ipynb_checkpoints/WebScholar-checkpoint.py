import requests
import time
import pickle

# Your Semantic Scholar API key
api_key = 'oBKuf3esid1L9pahwNBkY4o8GNEdx0jw4NxIncfW'

# Headers for authentication
headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json',
}

# Function to search for open-access papers by author and year
def search_open_access_papers(author_name, year):
    time.sleep(1)  # Respect the rate limit of 1 request per second
    # Fields to be returned for each paper
    fields = 'title,abstract,authors,publicationVenue,year,tldr,openAccessPdf,embedding.specter_v2'
    # Search query URL, including the fields parameter
    search_url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={author_name}&year={year}&openAccessPdf&fieldsOfStudy=Computer Science&fields={fields}"
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        papers = response.json().get('data', [])
#         print(f"Status Code: {response.status_code}, Response: {response.text}")
        return papers
    else:
        print(f"Error searching for papers by {author_name}: {response.status_code}")
        return []

# List of faculty names
faculty_names = [
    "Yonatan Bisk", "Ralf Brown", "Jamie Callan", "Justine Cassell", "Mona Diab",
    "Fernando Diaz", "Scott Fahlman", "Robert Frederking", "Daniel Fried", "Anatole Gershman",
    "Alexander Hauptmann", "Daphne Ippolito", "Lori Levin", "Lei Li", "Teruko Mitamura",
    "Louis-Philippe Morency", "David Mortensen", "Graham Neubig", "Eric Nyberg", "Kemal Oflazer",
    "Bhiksha Ramakrishnan", "Carolyn Rosé", "Alexander Rudnicky", "Maarten Sap", "Michael Shamos",
    "Rita Singh", "Emma Strubell", "Alexander Waibel", "Shinji Watanabe", "Sean Welleck",
    "Eric P. Xing", "Chenyan Xiong", "Yiming Yang"
]

# Initialize a dictionary to hold the results
papers_dict = {}

# Initialize dictionaries to track missing information
missing_venue_info = {}
missing_tldr_info = {}
missing_embedding_info = {}

for faculty_name in faculty_names:
    papers = search_open_access_papers(faculty_name, 2023)
    if papers:
        papers_dict[faculty_name] = {}
        for paper in papers:
            paper_url = paper.get("openAccessPdf", {}).get("url")
            if paper_url:  # Ensure there's a URL to use as a key
                publication_venue_name = paper["publicationVenue"].get("name") if paper.get("publicationVenue") else "No publication venue information available"
                tldr_text = paper["tldr"].get("text") if paper.get("tldr") else "No TLDR summary available"
                embedding_vector = paper["embedding"].get("vector") if paper.get("embedding") else []

                # Track missing information
                if not paper.get("publicationVenue"):
                    missing_venue_info.setdefault(faculty_name, []).append(paper_url)
                if not paper.get("tldr"):
                    missing_tldr_info.setdefault(faculty_name, []).append(paper_url)
                if not paper.get("embedding"):
                    missing_embedding_info.setdefault(faculty_name, []).append(paper_url)
                    
                papers_dict[faculty_name][paper_url] = {
                    "paperId": paper.get("paperId"),
                    "title": paper.get("title"),
                    "abstract": paper.get("abstract"),
                    "publicationVenue": publication_venue_name,
                    "year": paper.get("year"),
                    "tldr": tldr_text,
                    "embedding": embedding_vector,
                    "authors": [{"authorId": author.get("authorId"), "name": author.get("name")} for author in paper.get("authors", [])]
                }
    else:
        # Add the author's name with an empty dictionary if no papers were found
        papers_dict[faculty_name] = {}

# print(papers_dict)
# Define the filename where you want to store the dictionary
filename = 'data/webscholar_lti_dict.pkl'

# # Open the file in binary write mode and use pickle.dump() to write the dictionary
with open(filename, 'wb') as file:
    pickle.dump(papers_dict, file)

# Initialize metadata variables
total_authors = len(papers_dict)
total_papers_by_author = {author: len(papers_dict[author]) for author in papers_dict}

# Display metadata
print(f"Total authors: {total_authors}")
print(f"Papers by each author: {total_papers_by_author}")
print("Missing venue information: ", missing_venue_info)
print("Missing TLDR information: ", missing_tldr_info)
print("Missing embedding information: ", missing_embedding_info)

# Print out the detailed information for each found paper
for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"Abstract: {paper.get('abstract', 'No abstract available')}")
    print(f"Year: {paper['year']}")
    print(f"Open Access: {paper.get('isOpenAccess', False)}")

    # Extracting and printing author names
    authors = paper.get('authors', [])
    author_names = ', '.join([author['name'] for author in authors])
    print(f"Authors: {author_names}")

    # Printing the publication venue if available
    venue = paper.get('publicationVenue', {}).get('name', 'No venue info')
    print(f"Publication Venue: {venue}")

    # Printing TLDR (Auto-generated summary) if available
    tldr = paper.get('tldr', {}).get('text', 'No TLDR available')
    print(f"TLDR: {tldr}")

    print("---------\n")  
    
if not papers:
    print("No papers found for the given criteria.")

