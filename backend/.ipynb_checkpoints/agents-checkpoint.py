
from openai import OpenAI

client = OpenAI()

def explain_bill(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Explain electricity bills in simple language."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content

def generate_savings(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Give electricity saving recommendations."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content

def dispute_generator(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Generate a utility bill dispute email."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
