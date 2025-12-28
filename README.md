# ALM3 Converter

转换 `.alm3` 格式的加密音频文件，输出为 MP3 格式。

## 使用方法

```bash
# 转换单个文件
python alm3_decoder.py music.alm3

# 批量转换目录下所有 .alm3 文件
python alm3_decoder.py ./my_music_folder/
```

输出文件会保存在原文件同目录，文件名为 `原文件名.alm3.decoded.mp3`

## 原理

`.alm3` 文件结构：

- 前 10 字节：元数据长度（ASCII 数字）
- 接下来 N 字节：元数据
- 剩余部分：XOR 加密的音频数据

转换核心算法：`decrypted[i] = encrypted[i] ^ (i % 18)`

## 环境要求

- Python 3.x
- 无需安装任何依赖

## License

MIT
