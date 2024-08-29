from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

test_video_id = "rXld2YqnEgY"



def get_summary(ai_question):
    client = OpenAI(
    api_key= "enter API key here",
    organization="org-U1OqjvSUtE2t3gwXcoH0DuMI"

    )


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "you are a helpful assiant can you please summarize what this text is about"},
            {"role": "user", "content": ai_question}
        ]
    )

    message = response.choices[0].message.content
    print(message)


def main():
    video_id = input("'input the video id here: ") 
    transcript = YouTubeTranscriptApi.get_transcript(video_id) 

    ai_question = ""
    for key in transcript:
        x = key.get('text')
        ai_question += x
    get_summary(ai_question)

main()
