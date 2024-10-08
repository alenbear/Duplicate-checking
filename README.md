# 论文查重项目

## 一、项目简介

本项目旨在设计一个论文查重算法，比较给定原文文件和抄袭版论文文件的相似性，并输出其重复率。项目要求使用 C++、Java 或 Python3 进行开发。

## 二、项目结构

- 在 GitHub 仓库中新建一个以学号命名的文件夹。
- 使用 Visual Studio Community 2017（针对 C++）或其他兼容环境开发。
- 对于 Python 提交时需附带 `requirements.txt` 文件。
- 提交的代码需通过代码质量分析工具的检查，消除所有警告。
- 使用性能分析工具（如 Studio Profiling Tools）查找代码性能瓶颈并进行改进。

## 三、功能需求

### 题目：论文查重

设计一个论文查重算法，比较两个输入文件：原文和经过增删改的抄袭版论文，并输出两者的重复率。

#### 输入输出要求

- 从命令行参数获取文件路径：
  - 原文文件的绝对路径。
  - 抄袭版论文的绝对路径。
  - 输出答案文件的绝对路径。
- 输出结果为浮点型，精确到小数点后两位。

#### 示例

- **原文文件示例**：`今天是星期天，天气晴，今天晚上我要去看电影。`
- **抄袭版文件示例**：`今天是周天，天气晴朗，我晚上要去看电影。`
- **结果输出**：重复率（精确到小数点后两位）。

### 文件输入输出

- **Python**: `python main.py [原文文件] [抄袭版论文的文件] [答案文件]`
- **C/C++**: `main.exe [原文文件] [抄袭版论文的文件] [答案文件]`
- **Java**: `java -jar main.jar [原文文件] [抄袭版论文的文件] [答案文件]`

### 测试说明

- 共18个测试点（不含样例）。测试用于评估功能的正确性。
- 确保提交的代码可正常编译，并生成逻辑相同的可执行文件。

## 四、开发过程记录（PSP 表格）

1. **开始前**：
   - 在 PSP 表格中记录预计在程序开发各步骤上耗费的时间。
2. **项目完成后**：
   - 在 PSP 表格中记录实际花费的时间。

## 五、代码质量和性能分析

1. **代码质量分析**：
   - 使用 Code Quality Analysis 工具分析代码质量，消除所有警告。
2. **性能分析**：
   - 使用 Studio Profiling Tools 分析性能瓶颈，进行代码优化。

## 六、版本控制与单元测试

1. **版本控制**：
   - 使用 GitHub 管理源代码和测试用例，每次有代码进展时及时提交到 GitHub。
   - 保持合理的提交记录，确保项目透明度。

2. **单元测试**：
   - 使用单元测试工具编写至少10个测试用例，确保程序能正确处理各种情况。
   - 使用插件查看测试分支覆盖率等指标，确保代码的全面性和稳定性。

## 七、提交指南

- 对于 C++/Java，需将编译好的程序发布到 GitHub 仓库中的 releases 中。
- 提交时，Python 入口文件需命名为 `main.py`，C/C++ 可执行文件为 `main.exe`，Java 可执行文件为 `main.jar`。
- 文件路径不应含有空格，每个命令行参数之间以空格分隔。

### 示例

```bash
# Python 示例
python main.py C:\tests\orig.txt C:\tests\orig_add.txt C:\tests\ans.txt

# C/C++ 示例
main.exe C:\tests\orig.txt C:\tests\orig_add.txt C:\tests\ans.txt

# Java 示例
java -jar main.jar C:\tests\orig.txt C:\tests\orig_add.txt C:\tests\ans.txt
