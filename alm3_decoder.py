"""
ALM3 Audio File Decoder
转换 .alm3 格式的音频文件

Usage:
    python alm3_decoder.py <file.alm3>
    python alm3_decoder.py <directory>  # 批量处理目录下所有 .alm3 文件
"""

import os
import sys
import glob


def decrypt_alm3(file_path):
    """转换单个 .alm3 文件"""
    try:
        output_path = file_path + ".decoded.mp3"

        with open(file_path, "rb") as f:
            # 读取前 10 字节获取元数据长度
            header_len_bytes = f.read(10)
            try:
                meta_len = int(header_len_bytes.decode("utf-8").strip("\x00").strip())
            except ValueError:
                print(f"[错误] {file_path}: 无法解析文件头，可能不是 alm3 格式")
                return False

            f.seek(10 + meta_len)
            encrypted_data = f.read()

        # key = position % 18
        decrypted_data = bytearray(len(encrypted_data))
        for i in range(len(encrypted_data)):
            decrypted_data[i] = encrypted_data[i] ^ (i % 18)

        with open(output_path, "wb") as out_f:
            out_f.write(decrypted_data)

        print(f"[成功] {os.path.basename(file_path)} -> {os.path.basename(output_path)}")
        return True

    except Exception as e:
        print(f"[失败] {file_path}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("用法: python alm3_decoder.py <file.alm3 或 目录路径>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isfile(target):
        decrypt_alm3(target)
    elif os.path.isdir(target):
        files = glob.glob(os.path.join(target, "*.alm3"))
        if not files:
            print(f"目录 {target} 中没有找到 .alm3 文件")
            sys.exit(1)
        print(f"找到 {len(files)} 个文件，开始转换...\n")
        success = sum(1 for f in files if decrypt_alm3(f))
        print(f"\n完成: {success}/{len(files)} 个文件转换成功")
    else:
        print(f"路径不存在: {target}")
        sys.exit(1)


if __name__ == "__main__":
    main()
