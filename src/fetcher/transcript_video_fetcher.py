from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter

def write_to_json_file(video_id, transcript):
    formatter = JSONFormatter()

    # .format_transcript(transcript) turns the transcript into a JSON string.
    json_formatted = formatter.format_transcript(transcript)

    # Now we can write it out to a file.
    with open('transcript_video_' + video_id + '.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)
    # Now should have a new JSON file that you can easily read back into Python.

def fetch_transcript_by_id(video_id):
    # retrieve the available transcripts
    # the Transcript object provides metadata properties(video_id, language, language_code, is_generated, is_translatable, translation_languages)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    write_to_json_file(video_id, transcript)

def print_transcript(transcript):
    text_list = []
    for i in transcript:
        text_list.append(i['text'])

    text = ' '.join(text_list)
    print(text)
    print
    print(transcript.fetch())


def appeand_all_transcript_text(srt):
    text_list = []
    for i in srt:
        text_list.append(i['text'])

    text = ' '.join(text_list)
    return text