import os
import subprocess
import re
import shutil
from pathlib import Path

# 언어 설정
system = input("CMD:KO/KR=[z],EN=[x],TR=[c],Credits(w)Exit(e):").strip().lower()
if system == "z":  # Korean
    link = input("다운로드하실 유튜브 영상 링크를 적어주세요 \n").strip()
elif system == "x":  # English
    link = input("Enter a YouTube Video URL \n").strip()
elif system == "c":  # Turkish
    link = input("YouTube video link'i girin \n").strip()
elif system == "w":  # Credits
    print("Code By github'HyperNovaSTUDIO' Modified By 'ChatGPT'")
    exit()
elif system == "e":
    exit()
else:
    print("잘못된 언어 코드입니다. 종료합니다.")
    exit()

# 다운로드 형식 선택 (숫자 방식)
if system == "z":
    choice = input("저장 형식을 선택하세요: MP3[1] / MP4[2] : ").strip()
elif system == "x":
    choice = input("Choose format: MP3[1] / MP4[2] : ").strip()
elif system == "c":
    choice = input("Format seçin: MP3[1] / MP4[2] : ").strip()
else:
    choice = "1"

if choice == "1":
    file_type = "mp3"
elif choice == "2":
    file_type = "mp4"
else:
    print("❌ 잘못된 선택입니다. 기본값 MP3로 저장합니다.")
    file_type = "mp3"

# URL에서 playlist 파라미터 제거
if "&" in link:
    link = link.split("&")[0]

# 경로 설정
temp_dir = Path("temp_downloads")
output_dir = Path("downloads")
temp_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

# yt-dlp 포맷 후보
if file_type == "mp3":
    formats = [
        "bestaudio[ext=m4a]/bestaudio/best",
        "bestaudio[ext=webm]/bestaudio/best",
        "bestaudio"
    ]
else:  # mp4
    formats = [
        "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    ]

# yt-dlp 실행 함수
def run_yt_dlp(fmt):
    command = [
        "yt-dlp",
        "--no-playlist",
        "-f", fmt,
        "--write-thumbnail",
        "--add-header", "User-Agent: Mozilla/5.0",
        "-o", str(temp_dir / "%(title)s.%(ext)s"),
        link
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ yt-dlp 실패 (format={fmt})")
        print("STDERR:", e.stderr[:200], "...")
        return False

# 포맷별 시도
success = False
for fmt in formats:
    if run_yt_dlp(fmt):
        success = True
        break

if not success:
    print("❌ yt-dlp로 다운로드 실패. 모든 포맷 시도했음.")
    exit()

# 파일 이름 정리 함수
def clean_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r'\s+', "_", name)
    return name.strip("_")

# 썸네일 이미지 확장자 후보
thumbnail_exts = [".jpg", ".jpeg", ".png", ".webp"]

# 변환 처리
for file in temp_dir.iterdir():
    base_stem = file.stem

    # === MP3 변환 ===
    if file_type == "mp3" and file.suffix.lower() in [".webm", ".m4a", ".mp4", ".opus", ".flac"]:
        mp3_name = clean_filename(base_stem) + ".mp3"
        mp3_path = output_dir / mp3_name

        # 썸네일 찾기
        thumbnail_path = None
        for ext in thumbnail_exts:
            candidate = temp_dir / (base_stem + ext)
            if candidate.exists():
                thumbnail_path = candidate
                break

        if thumbnail_path:
            ffmpeg_cmd = [
                "ffmpeg", "-y",
                "-i", str(file),
                "-i", str(thumbnail_path),
                "-map", "0:a",
                "-map", "1",
                "-c:a", "libmp3lame",
                "-b:a", "192k",
                "-id3v2_version", "3",
                "-metadata:s:v", "title=Album cover",
                "-metadata:s:v", "comment=Cover (front)",
                str(mp3_path)
            ]
        else:
            ffmpeg_cmd = [
                "ffmpeg", "-y",
                "-i", str(file),
                "-vn",
                "-ab", "192k",
                "-ar", "44100",
                str(mp3_path)
            ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"✅ MP3 저장 완료: {mp3_name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ ffmpeg 변환 중 오류 발생: {file.name}")
            print(e)

    # === MP4 변환 ===
    elif file_type == "mp4" and file.suffix.lower() in [".mp4", ".webm", ".mkv"]:
        mp4_name = clean_filename(base_stem) + ".mp4"
        mp4_path = output_dir / mp4_name
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", str(file),
            "-c", "copy",
            str(mp4_path)
        ]
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"✅ MP4 저장 완료: {mp4_name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ MP4 변환 오류: {file.name}")
            print(e)

# 임시폴더 삭제
shutil.rmtree(temp_dir)
