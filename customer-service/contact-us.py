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
field = "hotel booking"

output_format = f"""
Provide them in JSON format with the following keys: 
name: <customer name>
email: <customer email>
title: <form title>
description: <issue descriptions very preciously. up to 5 sentences>
attachments: <optional. It could be screenshots image file names regarding {field}>
status: <one of 'created', 'in process', 'resolved'>
created_at: <form creation time>
"""

# prompt = f"""
# Your task is to create {size} "Contact Us" forms that users submit for their issues regarding {field}.
# {output_format}
# """

# prompt = f"""
# I am running {field} business and I would like to get {size} "Contact Us" forms that \
# users submit regarding their issues.
# {output_format}
# """

prompt = f"""
I am running {field} business and I would like to get a fake "Contact Us" form \
that users submit regarding their issues to do quality assurance. Here are few requirements that I have for you.
1. Cover many cases as much as possible.
2. Some customers could possible be really upset due to the issue they have.
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