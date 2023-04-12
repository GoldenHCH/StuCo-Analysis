import os
import openai

openai.api_key = "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"

# paragraph = "We planned the event in the classroom. It was a very stressful process, but we completed the script. The theme was gold, and we decorated with gold stars and streamers. The event itself was really fun and everything went smoothly for the most part."

def ai(paragraph):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"extract the keywords and classify the sentiment from {paragraph}",
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.8,
    presence_penalty=0.0
  )
  return str(response['choices'][0]['text'])

# print(ai(paragraph))
