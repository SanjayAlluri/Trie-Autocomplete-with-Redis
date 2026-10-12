
import streamlit as st

from trie import Trie
from cache import get_suggestions, client


# Build the Trie once per Streamlit process
@st.cache_resource
def load_trie():
    trie = Trie()

    with open("words.txt", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                trie.insert(word)

    return trie


st.set_page_config(
    page_title="Trie Autocomplete",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 Trie Autocomplete")
st.write("Search using Trie and Redis caching.")

try:
    # Connect to Redis and load the Trie
    client.ping()
    trie = load_trie()

    query = st.text_input(
        "Search for something",
        placeholder="Try app, python, or data..."
    )

    if query.strip():
        prefix = query.strip().lower()

        suggestions = get_suggestions(prefix, trie)

        st.subheader("Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.write(f"🔹 {suggestion}")
        else:
            st.info("No matching suggestions found.")

    st.divider()
    st.caption(
        "Redis caches suggestions for 60 seconds. "
        "Repeated searches can reuse cached results."
    )

except Exception as error:
    st.error(f"Could not load the autocomplete system: {error}")
