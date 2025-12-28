# ALM3 Converter

[中文](#中文) | [English](#english)

---

## English

Convert `.alm3` encrypted audio files to MP3 format.

### Usage

```bash
# Convert a single file
python alm3_decoder.py music.alm3

# Batch convert all .alm3 files in a directory
python alm3_decoder.py ./my_music_folder/
```

Output files are saved in the same directory as `original_name.alm3.decoded.mp3`

### How it works

`.alm3` file structure:

- First 10 bytes: metadata length (ASCII digits)
- Next N bytes: metadata
- Remaining: XOR encrypted audio data

Core algorithm: `decrypted[i] = encrypted[i] ^ (i % 18)`

### Requirements

- Python 3.x
- No dependencies

---

## 中文

转换 `.alm3` 格式的加密音频文件，输出为 MP3 格式。

### 使用方法

```bash
# 转换单个文件
python alm3_decoder.py music.alm3

# 批量转换目录下所有 .alm3 文件
python alm3_decoder.py ./my_music_folder/
```

输出文件会保存在原文件同目录，文件名为 `原文件名.alm3.decoded.mp3`

### 原理

`.alm3` 文件结构：

- 前 10 字节：元数据长度（ASCII 数字）
- 接下来 N 字节：元数据
- 剩余部分：XOR 加密的音频数据

转换核心算法：`decrypted[i] = encrypted[i] ^ (i % 18)`

### 环境要求

- Python 3.x
- 无需安装任何依赖

---

## License

MIT
