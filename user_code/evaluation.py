import hashlib
from typing import Optional
from typing import Tuple


__all__ = [
    "evaluate",
]


def string_to_score(
    s: str,
)-> float:
    
    # 计算 SHA256 哈希值
    hash_bytes = hashlib.sha256(s.encode()).digest()
    
    # 取前 4 个字节，转为整数
    hash_int = int.from_bytes(hash_bytes[:4], 'big')
    
    # 映射到 0 ~ 10000 之间的整数
    score = hash_int % 10001
    
    # 转为两位小数
    return round(score / 100, 2)


def evaluate(
    idea: str,
)-> Tuple[float, Optional[str]]:
    
    """
    对大语言模型生成的答案进行评估，返回分数和评语。

    Args:
        idea (str): 大语言模型生成的程序/文本。

    Returns:
        Tuple[float, str]: 包含两个元素的元组：
            - float: 回答的评分（0~100）。
            - str: 对回答的简要评语或解释信息（可为 None）。
    """
    
    score = string_to_score(idea)
    info = "非常好！" if score >= 80.0 else "一般般！"
    return score, info