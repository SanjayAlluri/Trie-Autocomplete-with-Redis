
# Trie Autocomplete with Redis

A simple autocomplete application built using Python, a Trie data structure, Redis caching, and Streamlit.

## Project Structure

- `trie.py` - Implements the Trie data structure for prefix-based word searching.
- `cache.py` - Handles Redis caching to store and retrieve autocomplete suggestions.
- `app.py` - Provides the Streamlit user interface.
- `main.py` - Runs a command-line test of the Trie and Redis integration.
- `words.txt` - Contains the words used for autocomplete.

## How It Works

1. The user enters a prefix in the Streamlit interface.
2. The application checks Redis for cached suggestions.
3. If the suggestions are cached, Redis returns them directly.
4. If there is a cache miss, the Trie searches for matching words.
5. The results are stored in Redis for future queries, with a 60-second expiration time.

## Tech Stack

- Python
- Trie Data Structure
- Redis
- Streamlit
- Docker

## Run Locally

Install the dependencies:

```bash
pip install streamlit redis
```

Start Redis using Docker:

```bash
docker run --name autocomplete-redis -p 6379:6379 -d redis
```

Run the application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to use the application.
