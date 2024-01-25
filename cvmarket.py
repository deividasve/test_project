from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

data = []

url_list = ['https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&search%5Bcategories%5D%5B0%5D=8&search%5Bkeyword%5D=&ga_track=90',
            'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&search%5Bcategories%5D%5B0%5D=8&search%5Bkeyword%5D=&ga_track=90&start=30',
            'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&search%5Bcategories%5D%5B0%5D=8&search%5Bkeyword%5D=&ga_track=90&start=60',
            'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&search%5Bcategories%5D%5B0%5D=8&search%5Bkeyword%5D=&ga_track=90&start=90',
            'https://www.cvmarket.lt/darbo-skelbimai?op=search&search%5Bjob_salary%5D=3&search%5Bcategories%5D%5B0%5D=8&search%5Bkeyword%5D=&ga_track=90&start=120']

for url in url_list:

    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())

    jobs = soup.find_all('article', {'data-component-id': True}) #tikrina, ar yra reikšmė data-component-id
    # print(jobs)

    for job in jobs:
        title = job.find('h2', class_='xl:text-xl font-bold mt-2 hover:underline').text.strip()
        company = job.find('span', class_='job-company mr-5').text.strip()
        # salary_range = job.find('div', class_='inline-block mt-2.5 lg:mt-0 salary-block mr-5').text.strip()
        salary_min_element = job.find('div', {'data-salary-from': True})
        salary_min = salary_min_element['data-salary-from'] if salary_min_element else 'N/A'
        salary_max_element = job.find('div', {'data-salary-to': True})
        salary_max = salary_max_element['data-salary-to'] if salary_max_element else 'N/A'
        salary_type_element = job.find('span', class_='text-slate-200 visited-group:text-gray-300 text-sm font-bold mt-0.5 salary-type')
        salary_type = salary_type_element.text.strip() if salary_type_element else 'N/A'
        location = job.find('span', class_='bg-blue-50 text-slate-500 py-1.5 px-3 font-bold text-sm rounded-full flex w-fit h-fit justify-center items-center space-x-1.5 cursor-defaults leading-4 location').text.strip()
        job_posted = job.find('div', class_='whitespace-nowrap').text.strip()
        data.append({'Title': title,
                     'Company': company,
                     'Min Salary': salary_min,
                     'Max Salary': salary_max,
                     'Salary Type': salary_type,
                     'Location': location,
                     'Job Posted': job_posted
                     })

df = pd.DataFrame(data)
print(df)
df.to_csv('cvmarket.csv', index=False)