# HyperNovaDownloader.-Python-script-
This is YT downloder made by Python and Faster,Better
# HyperNovaDownloader

## 🌐 프로젝트 개요 / Project Overview / Proje Özeti

**한국어:**  
HyperNovaDownloader는 yt-dlp와 ffmpeg를 활용하여 유튜브 영상을 MP3 또는 MP4로 다운로드할 수 있는 간단한 CLI 툴입니다.

**English:**  
HyperNovaDownloader is a simple CLI tool that uses yt-dlp and ffmpeg to download YouTube videos as MP3 or MP4 files.

**Türkçe:**  
HyperNovaDownloader, yt-dlp ve ffmpeg kullanarak YouTube videolarını MP3 veya MP4 olarak indirmenizi sağlayan basit bir CLI aracıdır.

---

## 📂 주요 파일 / Main Files / Ana Dosyalar

- `HNYTdownloader.py` : 메인 실행 파일 / Main executable file / Ana çalıştırılabilir dosya  
- `downloads/` : 변환된 파일 저장 폴더 / Folder for converted files / Dönüştürülmüş dosyaların kaydedileceği klasör  
- `temp_downloads/` : 임시 파일 저장 폴더 / Temporary files folder / Geçici dosyaların kaydedileceği klasör  

---

## ⚙️ 실행 흐름 / Execution Flow / Çalışma Akışı

1. 언어 선택 / Language selection / Dil seçimi  
2. 유튜브 링크 입력 / Enter YouTube link / YouTube bağlantısı girin  
3. 저장 형식 선택 (MP3[1] / MP4[2]) / Choose format (MP3[1] / MP4[2]) / Format seçin (MP3[1] / MP4[2])  
4. yt-dlp로 다운로드 / Download with yt-dlp / yt-dlp ile indirme  
5. ffmpeg 변환 / Convert with ffmpeg / ffmpeg ile dönüştürme  
6. 다운로드 폴더에 저장 / Save to downloads folder / downloads klasörüne kaydetme  
7. 임시 파일 삭제 / Delete temporary files / Geçici dosyaları silme  

---

## 📝 코드 설명 / Code Explanation / Kod Açıklaması

### run_yt_dlp(fmt)
- **한국어:** 지정한 포맷(fmt)으로 yt-dlp를 실행하는 함수. 성공 시 True, 실패 시 False 반환  
- **English:** Runs yt-dlp with the specified format (fmt). Returns True if successful, False otherwise.  
- **Türkçe:** Belirtilen formatta (fmt) yt-dlp çalıştırır. Başarılı olursa True, aksi takdirde False döner.

### clean_filename(name)
- **한국어:** 파일 이름에서 특수문자를 제거하고 공백을 `_`로 변환  
- **English:** Cleans the filename by removing special characters and replacing spaces with `_`.  
- **Türkçe:** Dosya adındaki özel karakterleri kaldırır ve boşlukları `_` ile değiştirir.

### 변환 처리 / Conversion / Dönüştürme
- **MP3 선택:** 오디오만 추출 + 썸네일을 앨범 커버로 삽입  
- **MP4 선택:** 비디오와 오디오를 합쳐 원본 화질로 저장  
- **English MP3:** Extract audio only + insert thumbnail as album cover  
- **English MP4:** Combine video and audio, save in original quality  
- **Türkçe MP3:** Sadece sesi çıkarır + küçük resim albüm kapağı olarak eklenir  
- **Türkçe MP4:** Video ve sesi birleştirir, orijinal kalitede kaydeder

---

## 💻 사용 예시 / Usage Example / Kullanım Örneği

```bash
$ python3 HNYTdownloader.py
CMD:KO/KR=[z],EN=[x],TR=[c],Credits(w)Exit(e): z
다운로드하실 유튜브 영상 링크를 적어주세요
> https://youtube.com/xxxx
저장 형식을 선택하세요: MP3[1] / MP4[2] : 2
✅ MP4 저장 완료: example_video.mp4
