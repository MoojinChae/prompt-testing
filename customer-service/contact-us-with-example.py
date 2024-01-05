from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        temperature=1,
    )
    return chat_completion

size = 3
field = "men apparel shopping mall"

output_format = f"""
Provide them in JSON format with the following keys: 
TicketID: 
Name: 
Email: 
Age: 
Gender:
Product Purchase:
Date of Purchase:
Ticket Type:
Ticket Subject:
Ticket Description:
Ticket Status: one of 'pending customer response', 'open', 'closed'
Resolution:
Ticket Priority: one of 'critial', 'low'
Ticket Channel: one of 'social media', 'chat', 'email', 'phone'
First Response Time: timestamp that agent first responsed.
Time to Resolution: timestamp that the ticket is closed.
Customer Satisfaction Rating: only set if ticket status is 'closed'. range from 1 to 5.
"""

prompt = f"""
I am running {field} business and I would like to get 3 fake customer support tickets to do AI quality assurance.
{output_format}
And, here are some example tickets that you can follow.
"TicketID": "1234",
"Name": "Marisa Obrien",
"Email": "carrollallison@example.com",
"Age": 32,
"Gender": "Male",
"Product Purchase": "Gap T-Shirt",
"Date of Purchase": "2021-03-22",
"Ticket Type": "Billing inquiry",
"Ticket Subject": "Account access",
"Ticket Description": "Hello, I can't sign-in to the website.",
"Ticket Status": "Closed",
"Resolution": "Password Reset",
"Ticket Priority": "low",
"Ticket Channel": "Social media",
"First Response Time": "2023-06-01 11:14:38",
"Time to Resolution": "2023-06-01 18:05:38",
"Customer Satisfaction Rating": 3
"""

print("====prompt====")
print(prompt)
for i in range(size):
    response = get_completion(prompt)
    print(f"====response-{i}====")
    print(response.choices[0].message.content)
    print("====token====")
    print(response.usage)