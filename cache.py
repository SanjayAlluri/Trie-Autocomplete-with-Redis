
import json
import redis

from trie import Trie

client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def get_cached_suggestions(prefix):
    key = f"autocomplete:{prefix.lower()}"
    result = client.get(key)

    if result is None:
        return None

    return json.loads(result)


def cache_suggestions(prefix, suggestions):
    key = f"autocomplete:{prefix.lower()}"

    client.set(
        key,
        json.dumps(suggestions),
        ex=60
    )


def get_suggestions(prefix, trie):
    # 1. Check Redis first
    cached = get_cached_suggestions(prefix)

    if cached is not None:
        print("Cache hit!")
        return cached

    # 2. Cache miss: search the Trie
    print("Cache miss! Searching Trie...")
    suggestions = trie.search_prefix(prefix)

    # 3. Save the result in Redis
    cache_suggestions(prefix, suggestions)

    return suggestions
