import re

# 1. Salin teks dari file .lrc Anda ke dalam variabel ini
lrc_text = """
[00:44.85]I know a place
[00:54.53]It's somewhere I go when I need to remember your face
[01:04.16]We get married in our heads
[01:14.77]Something to do while we try to recall how we met
[01:21.21]
[01:24.21]Do you think I have forgotten?
[01:29.22]Do you think I have forgotten?
[01:34.12]Do you think I have forgotten about you?
[01:41.67]
[01:44.27]You and I
[01:49.12]Were alive
[01:54.44]With nothing to do I could lay and just look in your eyes
[02:04.81]Wait and pretend
[02:14.84]Hold on and hope that we'll find our way back in the end
[02:21.36]
[02:24.28]Do you think I have forgotten?
[02:29.16]Do you think I have forgotten?
[02:34.10]Do you think I have forgotten about you?
[02:44.25]Do you think I have forgotten?
[02:49.23]Do you think I have forgotten?
[02:54.12]Do you think I have forgotten about you?
[03:01.86]
[03:04.60]There was something about you that now I can't remember
[03:09.51]It's the same damn thing that made my heart surrender
[03:14.51]And I'll miss you on a train
[03:16.98]I'll miss you in the morning
[03:19.50]I never know what to think about
[03:23.83]
[03:23.63]I think about you
[03:29.23]About you
[03:34.24]Do you think I have forgotten about you?
[03:44.17]About you
[03:49.30]About you
[03:54.22]Do you think I have forgotten about you?
[04:02.78]
"""

lyrics = []

# 2. Proses parsing baris demi baris menggunakan Regex
# Pattern ini mencari format [menit:detik] diikuti oleh teks lirik
pattern = r"\[(\d+):(\d+\.\d+)\](.*)"

for line in lrc_text.strip().split("\n"):
    match = re.match(pattern, line)
    if match:
        minutes = int(match.group(1))
        seconds = float(match.group(2))
        text = match.group(3).strip()
        
        # Rumus mengubah menit ke total detik
        total_seconds = round((minutes * 60) + seconds, 3)
        
        # Masukkan ke dalam list dengan format tuple (float, "string")
        lyrics.append((total_seconds, text))

# 3. Cetak hasilnya agar formatnya persis seperti Foto 1
print("lyrics = [")
for time_stamp, lyric_text in lyrics:
    print(f'    ({time_stamp}, "{lyric_text}"),')
print("]")