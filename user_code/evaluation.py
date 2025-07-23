import math
import numpy as np
from typing import Optional
from typing import Tuple
from threading import Lock


__all__ = [
    "evaluate",
]


# evaluate_random_generator = np.random.default_rng()
# evaluate_upper_bound = 5.0
# evaluate_lock = Lock()

# def evaluate(
#     idea: str,
# )-> Tuple[float, Optional[str]]:
    
#     """
#     对大语言模型生成的答案进行评估，返回分数和评语。

#     Args:
#         idea (str): 大语言模型生成的程序/文本。

#     Returns:
#         Tuple[float, str]: 包含两个元素的元组：
#             - float: 回答的评分（0~100）。
#             - str: 对回答的简要评语或解释信息（可为 None）。
#     """
    
#     with evaluate_lock:
    
#         global evaluate_upper_bound
#         global evaluate_random_generator
        
#         score = evaluate_random_generator.uniform(0.0, evaluate_upper_bound)
#         evaluate_upper_bound = min(
#             max(
#                 0,
#                 evaluate_upper_bound + evaluate_random_generator.uniform(-1.0, 4.0),
#             ),
#             100.0
#         )
#         info = "非常好！" if score >= 80.0 else "一般般！"
#         return score, info

def evaluate(
    idea: str,
) -> Tuple[float, Optional[str]]:
    """
    评估提交的 Python 函数 idea(x) 与目标函数 x^2 在 [-10, 10] 上的拟合程度，
    计算卡方值后归一化为评分，并返回简要评语。

    Args:
        idea (str): 定义一个函数 f(x) 的 Python 代码字符串。

    Returns:
        Tuple[float, Optional[str]]: 包含两个元素：
            - float: 评估得分（0~100，越高越好）。
            - str: 简短评语或解释信息。
    """
    # 安全执行 idea，提取用户定义的 f 函数
    local_env = {}
    try:
        exec(idea, {}, local_env)
        f = local_env.get("f")
        if not callable(f):
            raise ValueError("idea 中没有找到可调用的函数 f(x)")
    except Exception as e:
        return 0.0, f"代码执行失败：{e}"

    # 构造采样点并计算 chi^2 误差
    try:
        xs = np.linspace(-10, 10, 100)
        ys_true = xs ** 2
        ys_pred = np.array([f(x) for x in xs])
        # 避免除以0
        epsilon = 1e-6
        chi2 = np.sum((ys_pred - ys_true) ** 2 / (ys_true + epsilon))
    except Exception as e:
        return 0.0, f"运行时出错：{e}"

    # 将 chi^2 映射到 0~100 分
    # chi2 = 0 时得 100 分；chi2 越大，得分越低；chi2 > 1000 基本归零
    def chi2_to_score(chi2) -> float:
    # S型函数，映射 chi² 到 0~100 分
        return 100.0 / (1.0 + (chi2 / 100.0) ** 0.8)
    # score = max(0.0, 100.0 * math.exp(-chi2 / 100.0))
    score = chi2_to_score(chi2)

    # 生成简评
    if score > 90:
        comment = "拟合非常好，几乎完美！"
    elif score > 70:
        comment = "整体不错，存在些微误差。"
    elif score > 40:
        comment = "拟合较差，可再改进。"
    else:
        comment = "误差较大，建议检查函数实现。"

    return score, None