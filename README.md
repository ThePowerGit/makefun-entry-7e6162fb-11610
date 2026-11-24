# One Sentence for a Traveler from 1800

A single sentence explaining the internet to someone arriving from the year
1800 — a post office the size of the world, where a letter reaches any house
before its ink dries and anyone may shelve a book for every reader to copy.

## The text

> The internet is a post office the size of the world: a letter to any house arrives before its ink dries, and anyone may set a book on its shelf for every reader to take a copy.

- Character count: **176**
- Cap: **200 characters** (UTF-8, non-whitespace)

`entry.txt` holds exactly these characters — one line, no trailing newline.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
defaulting to `/output`.

## License

MIT — see `LICENSE`.
