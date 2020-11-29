# Extractive YouTube Summaries

This is a quick script I put together to extract and summarise the subtitle transcripts from [YouTube](https://www.youtube.com/) videos. 
I use [extractive summarization](https://en.wikipedia.org/wiki/Automatic_summarization#Extraction-based_summarization) from [Gensim Summarizer](https://radimrehurek.com/gensim_3.8.3/summarization/summariser.html) to extract the most relevant sentences, [deepsegment](https://pypi.org/project/deepsegment/) to segment sentences with poor punctuation, and [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/) to get the transcripts.

# Installation

First, clone the repository. 

In your terminal, run:  
```
pip install -r requirements.txt
```

# Usage

```python
>>> python get_youtube_summary [video link] 200
```

# Resources/References
1. [Federico Barrios, Federico L´opez, Luis Argerich, Rosita Wachenchauzer (2016). Variations of the Similarity Function of TextRank for Automated Summarization,](https://arxiv.org/abs/1602.03606)
