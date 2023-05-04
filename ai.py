
import openai

openai.api_key ="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"

response = openai.Image.create(

    prompt="face. it has browny greeny eyes, slightly off centre. very realistic",

    n=1,

    size="1024x1024"

)
print(response['data'][0]['url'])