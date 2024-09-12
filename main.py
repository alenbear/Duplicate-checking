import sys
import textdistance
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz


def classify_text_by_length(text, char_threshold=50000, word_threshold=10000):
    num_chars = len(text)
    num_words = len(text.split())

    if num_chars > char_threshold or num_words > word_threshold:
        return 'Large Text'
    else:
        return 'Small Text'


def compare_files(original_file_path, plagiarized_file_path):
    """
    使用 textdistance 库、scikit-learn 和 fuzzywuzzy 库比较两个文件的相似度，并融合成一个综合相似度。
    """
    try:
        # 读取原文文件和抄袭版文件的内容
        with open(original_file_path, 'r', encoding='utf-8') as original_file, \
                open(plagiarized_file_path, 'r', encoding='utf-8') as plagiarized_file:

            original_content = original_file.read()
            plagiarized_content = plagiarized_file.read()

            # 判断文本大小
            text_size_category = classify_text_by_length(original_content)
            print('文本类型:', text_size_category)
            if text_size_category == 'Large Text':
                levenshtein_weight = 0.2
                cosine_weight = 0.6
                fuzzy_weight = 0.2
            else:
                levenshtein_weight = 0.4
                cosine_weight = 0.2
                fuzzy_weight = 0.4

            # 使用 Levenshtein 距离计算相似度
            levenshtein_similarity = textdistance.levenshtein.normalized_similarity(original_content,
                                                                                    plagiarized_content)

            # 使用 TF-IDF 向量化和余弦相似度计算
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform([original_content, plagiarized_content])
            cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

            # 使用 fuzzywuzzy 计算相似度
            fuzzy_similarity = fuzz.ratio(original_content, plagiarized_content) / 100.0

            # 融合多个相似度值
            combined_similarity = (
                    levenshtein_weight * levenshtein_similarity +
                    cosine_weight * cosine_sim +
                    fuzzy_weight * fuzzy_similarity
            )

    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        sys.exit(1)

    # 返回综合相似度
    return combined_similarity


def main():
    # 检查命令行参数数量
    if len(sys.argv) != 4:
        print("使用方法: python main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        sys.exit(1)

    # 获取命令行参数
    original_file_path = sys.argv[1]
    plagiarized_file_path = sys.argv[2]
    answer_file_path = sys.argv[3]

    # 计算综合相似度
    combined_similarity = compare_files(original_file_path, plagiarized_file_path)

    # 将相似度结果写入答案文件
    try:
        with open(answer_file_path, 'w', encoding='utf-8') as answer_file:
            answer_file.write(f"综合相似度: {combined_similarity * 100:.2f}%\n")
        print(f"综合相似度已写入文件: {answer_file_path}")
    except Exception as e:
        print(f"写入文件时发生错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
