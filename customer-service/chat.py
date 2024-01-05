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
field = "hotel booking system"

output_format = f"""
Provide them in JSON format with the following keys: 
name: <customer name>
email: <customer email>
agent: <agent name>
wait time: <wait time to start conversation with agent>
total tile: <total coverstaion time>
summary: <summary of coversation>
chat: <list of coversation between agent and customer>
status: <one of 'created', 'resolved', 'investigating'>
ticket: <optional field. create a jira ticket number only if status is 'investigating'>
created_at: <chat creation time>
"""

prompt = f"""
I am running {field} business and I would like to get a fake customer service chat conversation \
to do quality assurance. Here are few requirements that I have for you.
1. Cover many possible cases as much as possible.
2. 10% of customers are really upset due to the issue they have.
3. 30% of issues is not resolved during coversasion. In this case, a issue ticket will be created to follow up.
{output_format}
"""
print("====prompt====")
print(prompt)
for i in range(size):
    response = get_completion(prompt)
    print(f"====response-{i}====")
    print(response.choices[0].message.content)
    print("====token====")
    print(response.usage)