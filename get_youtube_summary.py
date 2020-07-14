"""
To do:
1. Make the segmenting dynamic. Only use deepsegment if necessary.
2. Change the input so that you can enter word_count or ratio.
3. In the abscenece of the above, make it such that it'll dynamically choose
which method to use to summarise the topic. 
4. Save pdfs to my Dropbox for the E-reader. Maybe create a summary and then the full thing.
5. Add abstractive summaries for each sentence if possible. 
"""

import spacy
nlp = spacy.load('en_core_web_sm')
nlp_pipe = nlp.create_pipe('sentencizer')
nlp.add_pipe(nlp_pipe, before='parser')
import deepsegment
segmenter = deepsegment.DeepSegment('en')
from gensim.summarization.summarizer import summarize
from youtube_transcript_api import YouTubeTranscriptApi
import re
import sys

def parse_youtube_url(url):
    return url.replace(r'https://www.youtube.com/watch?v=','')

def main(url, word_count):
    video_id = parse_youtube_url(url)
    text = YouTubeTranscriptApi.get_transcript(video_id)
    text_extracted = [phrase['text'] for phrase in text]
    sentences = segmenter.segment_long(' '.join(text_extracted),n_window=10)
    #sentences = list(nlp(' '.join(text_extracted)).sents)
    #sentences = [sentence.text for sentence in sentences]
    summary = summarize('. '.join(sentences), word_count=word_count)
    skip_deps = ['advmod', 'amod', 'predet', 'intj']
    cleaned_summary = ' '.join([token.norm_ for token in nlp(summary) if token.dep_ not in skip_deps])
    print(cleaned_summary)

if __name__ == '__main__':
    # Too many arguments
    if len(sys.argv) > 3:
        print('Please, input just the YouTube URL and the number of words for your summary.')
        sys.exit(1)  # abort because of error
    # Too few arguments
    elif len(sys.argv) < 3:
        try:
            user_input = input('Please, type a positive number to determine how many words to have in the summary.')
            n = int(user_input)
            url = sys.argv[1]
            url = str(url)
            main(url, abs(n))
        except ValueError:
            print(f'{user_input} is not a valid variable. Please, insert a positive integer for the number words you want.')
            sys.exit(1)
    # Correct number of arguments
    else:
        try:
            url = sys.argv[1]
            url = str(url)
            word_count = sys.argv[2]
            word_count = int(word_count)
            main(url, abs(word_count))
        except ValueError:
            print(f'{url} or {word_count} is not a valid variable. Please, insert a YouTube URL and a positive integer for the number words you want.')
            sys.exit(1)
        except IndexError:
            print('Please, next time, insert a YouTube URL and a positive integer for the number of words you want.')
        