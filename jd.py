
import requests
from bs4 import BeautifulSoup

URL = "https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job?in_iframe=1"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_job_details():
    try:
        print("Fetching webpage...")
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
        print("Webpage fetched successfully!")
        soup = BeautifulSoup(response.text, 'html.parser')
        # Your code goes here
        job_title_element= soup.select_one('div#iCIMS_Header h1')
        job_title= job_title_element.get_text(strip=True) if job_title_element else 'job title not found'
        
        all_content_parts=[]
        content_containers=soup.find_all('div', class_='iCIMS_Expandable_Text')
        
        for container in content_containers:
            text_part=container.get_text(separator='\n', strip=True)
            all_content_parts.append(text_part)
        full_content='\n\n'.join(all_content_parts) if all_content_parts else 'job description not found'

        print(f"Job Title: {job_title}\n")
        print("Job Description:\n")
        print(full_content)
        
        print("\n\n--- SCRAPING COMPLETE ---")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
    

if __name__ == "__main__":
    scrape_job_details()
