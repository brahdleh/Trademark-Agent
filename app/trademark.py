from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from google import genai

def scrape_tms(query):

  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  dr = webdriver.Chrome(options=options)

  dr.get("https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/"+query) # EU TM website

  # Find trademarks
  try:
    elem = WebDriverWait(dr, 5).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="cookiePolicyBannerDiv"]/div/div/div[2]/div[1]/span'))
    )

    button = dr.find_element(By.XPATH,'//*[@id="cookiePolicyBannerDiv"]/div/div/div[2]/div[1]/span')
    button.click()
    elem = WebDriverWait(dr, 5).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="basic-tab-trademarks"]/div/div/div[3]/div[1]'))
    )

    tm_names = []
    tm_classifications = []
    for i in range(1,101):

      tm_name_raw = dr.find_element(By.XPATH, '//*[@id="basic-tab-trademarks"]/div/div/div[3]/div[1]/div['+str(i)+']/header/div/div[1]/h3/a').text
      tm_names.append(re.findall(r'^[\d\w]{9} - (.*) \+ info$', tm_name_raw)[0])

      tm_classifications_raw = dr.find_element(By.XPATH, '//*[@id="basic-tab-trademarks"]/div/div/div[3]/div[1]/div['+str(i)+']/div/div/div[2]/dl/dd[5]').text
      tm_classifications.append(list(map(str, tm_classifications_raw.split(', '))))

      tm_data = pd.DataFrame({
          'Name': tm_names,
          'Classification': tm_classifications
      })
  except:
    tm_data = pd.DataFrame({
          'Name': [],
          'Classification': []
    })

  dr.quit()
  return tm_data

def scrape_classes():
  # Get data on trademark classes from a webpage
  response = requests.get(
      "https://www.londonip.co.uk/trademarks/tm-classes/",
      headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
  )

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')  # Parse
    content = soup.find('div', class_='entry-content')     # Find content
    texts = content.find_all('p')[5:51]                    # Extract paragraph text
    del texts[34]
    cleaned = [str(s).replace('<p>', '') for s in texts]        # Clean <p> markers
    return cleaned

  else:
      print(f"Failed to retrieve the page. Status code: {response.status_code}")

def classifier(summary):
  # Get the class data and join it to a readable string
  classes = scrape_classes()
  classes_string = "\n\n".join(classes)

  # Set up Gemini
  client = genai.Client(api_key="AIzaSyCkuKfcazMTHVUvwxnDKHmc_eiaIj9Q_p8")

  # call response
  response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="""You are an IP expert that classifies a company into classes based on it's goods and services. Below is a company summary,
            and below that is a description of every possible class. Please read the company description and decide which classes are relevant. Return a simple list of the
            form: "9, 10, 11" . Always return at least one number. \n Company description""" + summary + classes_string
  ).text
  return response.replace('\n','').split(", ")

def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]   # d matrix rows
    d.insert(0, list(range(0, n + 1)))   # d matrix columns
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j] + 1,
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]

def check_infringement(tm_name, input_name):
        # Compute Levenshtein distance between two strings
        distance = levenshteinDistance(tm_name.lower(), input_name.lower())
        # Calculate the percentage of characters that need to be changed
        threshold = len(input_name) * 0.2
        return distance < threshold

def inspector(name, classifications):
  # Get the web data from EU IP website and the class data
  tm_data = scrape_tms(str(name))
  classes = scrape_classes()

  # Extract descriptions of the classifications we have assigned to the client
  client_classes = []
  for n in classifications:
    client_classes.append(classes[int(n)-1])
  client_classes_string = "\n".join(client_classes)

  client = genai.Client(api_key="AIzaSyCkuKfcazMTHVUvwxnDKHmc_eiaIj9Q_p8")

  # Keep companies with industry overlap if there is any data
  if(len(tm_data)>0):
    filtered_df = tm_data[tm_data['Classification'].apply(lambda x: any(num in classifications for num in x))]
    filtered_df = filtered_df[filtered_df['Name'].apply(lambda x: check_infringement(x, name))]

    # If there is relevant infringement reflect this
    if(len(filtered_df)>0):
      response = client.models.generate_content(
              model="gemini-2.0-flash",
              contents="You are an EU IP lawyer writing a summary on potential trademark infrigement. The proposed company name is "+str(name)+". The relevant classes for this client have been decided as: "+client_classes_string+". The following names have flagged as being similar and operate in at least one of the same classes: "+str(", ".join(filtered_df['Name'].tolist()))+". Please write a report these potential infringements and some possible recourse. Do not use any previous understanding of company names, simply refer to the information given. Template: Title (Trademark infringement audit) - Submission details (name, current date) - Classification details (brief summary of classes and descriptions) - Conflict details (exact matches then similar names) - Recommended actions (modify application, consult legal advice, negotiate with holder)"
    )
    return response.text
    # Otherwise return no infringement
  else:
    response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents="You are an EU IP lawyer writing a summary on potential trademark infrigement. The proposed company name is "+str(name)+". The relevant classes for this client have been decided as: "+client_classes_string+". We have decided that the We have not found any potential trademark infringement. Your report should cover brief descriptions of the classes, and the lack of infringement. Do not use any understanding of company names, simply refer to the information given. Template: Title (Trademark infringement audit) - Submission details (name, classes, current date) - Classification details (brief summary of classes and descriptions) - Conflict details (state that there are no issues found) - actions to secure trademark (make formal EU application...)"
      )
    return response.text
  
def check_infringements_function(name, summary):
   classes = classifier(summary)
   return {"status": "success", "report": inspector(name, classes)}