import unittest
from main import compare_files  # 确保从正确的模块导入函数
import os


class TestSimilarity(unittest.TestCase):

    def test_compare_files(self):
        """
        测试 compare_files 函数，计算抄袭文件的相似度。
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
        for plagiarized_file in plagiarized_files:
            similarity_score = compare_files(original_file_path, plagiarized_file)
            print(f"相似度 ({plagiarized_file}): {similarity_score:.2f}")

    def test_empty_file_path(self):
        """
        测试当文件路径为空时，函数的行为。
        """
        with self.assertRaises(SystemExit):
            compare_files('', 'orig_0.8_add.txt')  # 原文件路径为空

        with self.assertRaises(SystemExit):
            compare_files('orig.txt', '')  # 抄袭文件路径为空

        with self.assertRaises(SystemExit):
            compare_files('', '')  # 两个路径都为空

    def test_invalid_file_path(self):
        """
        测试当文件路径不存在时，函数的行为。
        """
        with self.assertRaises(SystemExit):
            compare_files('non_existing_file.txt', 'orig_0.8_add.txt')  # 原文件路径不存在

        with self.assertRaises(SystemExit):
            compare_files('orig.txt', 'non_existing_file.txt')  # 抄袭文件路径不存在

        with self.assertRaises(SystemExit):
            compare_files('non_existing_file.txt', 'another_non_existing_file.txt')  # 两个路径都不存在


if __name__ == '__main__':
    unittest.main()
