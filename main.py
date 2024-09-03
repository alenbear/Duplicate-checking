import sys
import textdistance

def compare_files_with_textdistance(original_file_path, plagiarized_file_path):
    """
    使用 textdistance 库比较两个文件的相似度。
    """
    try:
        # 读取原文文件和抄袭版文件的内容
        with open(original_file_path, 'r', encoding='utf-8') as original_file, \
             open(plagiarized_file_path, 'r', encoding='utf-8') as plagiarized_file:

            original_content = original_file.read()
            plagiarized_content = plagiarized_file.read()

            # 使用 Levenshtein 距离计算相似度
            similarity = textdistance.levenshtein.normalized_similarity(original_content, plagiarized_content)

    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        sys.exit(1)

    # 返回相似度
    return similarity

def main():
    # 检查命令行参数数量
    if len(sys.argv) != 3:
        print("使用方法: python main.py [原文文件] [抄袭版论文的文件]")
        sys.exit(1)

    # 获取命令行参数
    original_file_path = sys.argv[1]
    plagiarized_file_path = sys.argv[2]

    # 计算相似度
    similarity = compare_files_with_textdistance(original_file_path, plagiarized_file_path)
    print(f"文件相似度: {similarity:.2f}")

if __name__ == "__main__":
    main()
