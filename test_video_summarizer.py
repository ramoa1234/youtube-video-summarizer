from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

api_key = 'Enter API key here'

def get_video_id(url):
    video_id = []
    iterating = False
    for character in url:
        if(character == '='):
            if not iterating:
                iterating = True
            else:
                iterating = False
        if(iterating):
            video_id.append(character)
    print(''.join(video_id))
    return ''.join(video_id)
  

def get_response(question, transcript):
    if(question):
        response = client.chat.completions.crete(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": question},
                    {"role": "user", "Content": transcript}
                ]
            )
    else:
        
        response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "you are a helpful assiant can you please summarize what this text is about"},
                    {"role": "user", "content":transcript}
                ]
            )

    return response



def main():
    if(api_key): 
        question = input('do want to ask question about prompt if no leave blank')
        url = input('enter youtube video url here')
        video_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        response = get_response(question, transcript)
        print(response)
    else:
        print('Need to Enter an API key')

main()
