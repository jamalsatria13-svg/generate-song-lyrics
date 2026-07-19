# Terminal Lyrics Player

Play an MP3 in the terminal while synchronized lyrics scroll or update in place, timed against playback position. Includes a helper script to convert `.lrc` lyric files into the Python tuple format the players use.

## Contents

| File | Description |
|---|---|
| `converter.py` | Converts standard `.lrc` timestamped lyrics (`[mm:ss.xx]text`) into a Python `lyrics = [(seconds, "text"), ...]` list you can paste into a player script. |
| `liriklagu1.py` | Simple player: prints each new lyric line downward in the terminal as playback reaches its timestamp (no translation). |
| `liriklagu2.py` | Enhanced player: centered, color-coded display showing the previous/current/next line at once, plus an optional translation line under the active lyric. |

## Requirements

- Python 3.8+
- An MP3 file to play (**not included** — see note below)
- A terminal that supports ANSI escape codes for `liriklagu2.py`'s colors and cursor positioning (most Linux/macOS terminals; on Windows the script enables this via `os.system('')`, which works in modern `cmd`/PowerShell/Windows Terminal)

## Installation

```bash
git clone <this-repo-url>
cd <repo-name>
pip install -r requirements.txt
```

## Usage

### 1. Generate a lyrics list from an `.lrc` file

Open `converter.py`, paste your `.lrc` content into the `lrc_text` variable, then run:

```bash
python converter.py
```

This prints a `lyrics = [...]` block to the terminal — copy it into `liriklagu1.py` or `liriklagu2.py`, replacing the existing `lyrics` list. For `liriklagu2.py`, you'll additionally need to add a translation string as a third tuple element per line (or leave it as `""`).

### 2. Play a song with synced lyrics

Place your MP3 in the same folder as the player script and update the `MP3_FILE` filename inside the script to match, then run:

```bash
python liriklagu1.py
# or
python liriklagu2.py
```

Press Enter to start playback; press `Ctrl+C` to stop early.

## Notes / Known Limitations

- **MP3 files are not included in this repo.** `liriklagu1.py` expects `bernadya-kita_buat_menyenangkan.mp3` and `liriklagu2.py` expects `about_you.mp3` in the working directory — add your own audio and/or update `MP3_FILE`. Don't commit copyrighted audio files to a public repo.
- `converter.py`, `liriklagu1.py`, and `liriklagu2.py` are standalone scripts, not wired together automatically — the lyrics list has to be copy-pasted from the converter's output into a player script by hand.
- Lyric timing sync relies on `pygame.mixer.music.get_pos()`, which measures elapsed playback time and isn't frame-accurate; drift can occur on longer tracks.
- Both players call `lyrics.sort(key=lambda x: x[0])` at startup, so entries don't need to be in timestamp order beforehand.

## License

Add a license of your choice here (e.g. MIT) before making the repo public. Note this covers the code only — you're responsible for the rights to any audio/lyrics you use with it.
