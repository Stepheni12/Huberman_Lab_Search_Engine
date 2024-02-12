# Huberman Lab Podcast RAG-Based Search Engine

For an in-depth look at how I put this project together you can check out the accompanying blog [post](https://isteph.netlify.app/building-a-hugging-face-space) I wrote.

Retrieval-Augmented Generation (RAG) is a simple yet powerful approach that is going to completely revolutionize search. This project provides a peak into the capabilities of RAG, which even in this simple example showcases how it can significantly outperfom keyword-based search techniques.

#### General Approach
The idea behind this project was to create an advanced search engine to discover Huberman Lab Podcast episodes for topics you are interested in. However, as opposed to simple keyword-based search, this RAG-Based approach allows for a much stronger search engine which incorporates the actual context and meaning of what you are trying to find as opposed to just matching keywords. The general approach was as follows:

1. Scrape mp3 files from the RSS feed on the Huberman Lab website
2. Generate transcriptions of all the mp3 files
3. Break down individual episode transcriptions into smaller sections
4. Generate word embeddings for each of these smaller sections
5. Store all the embeddings in a vector database
6. Create a gradio frontend to allow users to utilize the search functionality

#### References
Jason Liu, also for the inspiration on doing a RAG project

Huberman Lab Podcast, for all the valuable free information