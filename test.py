import unittest
from main import classify_text_by_length, compare_files  # 确保从正确的模块导入函数
import os


class TestTextSimilarity(unittest.TestCase):

    def test_compare_files_with_textdistance(self):
        """
        测试 compare_files_with_textdistance 函数，计算抄袭文件的相似度。
        """
        original_file_path = os.path.join('orig.txt')
        plagiarized_files = [
            os.path.join('orig_0.8_add.txt'),
            os.path.join('orig_0.8_del.txt'),
            os.path.join('orig_0.8_dis_1.txt'),
            os.path.join('orig_0.8_dis_10.txt'),
            os.path.join('orig_0.8_dis_15.txt')
        ]

        # 测试每个抄袭文件与原文件的相似度
        results = []
        for plagiarized_file in plagiarized_files:
            similarity_score = compare_files(original_file_path, plagiarized_file)
            print(f"相似度 ({plagiarized_file}): {similarity_score:.2f}")


if __name__ == '__test__':
    unittest.main()
