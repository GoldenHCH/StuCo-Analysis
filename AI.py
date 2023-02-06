import os
import openai

openai.api_key = "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"

paragraph = "Tailgate went great. Hotdogs, otter pops, and condiments were served during lunch. We actually had pretty much the perfect amount of food and setup was quite minimal with a couple grills. Participation was better than I expected with lines overflowing into the school. The games we set up weren’t used too much; this happened because we couldn’t really initiate the games since we were serving the food. "

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
  return response

print(ai(paragraph))
