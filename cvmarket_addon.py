import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)

df = pd.read_csv('cvmarket.csv')
# print(df)
average_min_salary = df['Min Salary'].mean().round(2)
average_max_salary = df['Max Salary'].mean().round(2)
total_job_listings = df['Title'].count()
job_listings_per_company = df['Company'].value_counts()
average_salary_by_title = df.groupby('Title')[['Min Salary', 'Max Salary']].mean().round(2)
job_listings_per_location = df['Location'].value_counts()
summary = {
    'Average MIN Salary': average_min_salary,
    'Average MAX Salary': average_max_salary,
    'Total Job Listings': total_job_listings,
    'Job Listings per Company': job_listings_per_company,
    'Average Salary by Title': average_salary_by_title,
    'Job Listings per Location': job_listings_per_location
}
# print(summary)


def truncate_title(title, max_length=10):
    if len(title) > max_length:
        return title[:max_length] + '...'
    return title

df['Short Title'] = df['Title'].apply(truncate_title)
df['Average Salary'] = df[['Min Salary', 'Max Salary']].mean(axis=1)
sorted_data = df.sort_values(by='Average Salary', ascending=False).head(10)
plt.figure(figsize=(14, 8))
plt.bar(sorted_data['Short Title'], sorted_data['Average Salary'], color='skyblue')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.title('Top 10 Job Titles by Average Salary')
plt.xticks(rotation=45)
plt.show()