from typing import List
from typing import Optional


__all__ = [
    "generate_prompt_func",
]


def generate_prompt_func(
    ideas: List[str], 
    scores: List[float], 
    infos: List[Optional[str]]
)-> str:

    nmax = min(20, len(scores))

    # 当前策略：取后 nmax 个得分作为代表
    chosen_indexs = list(range(len(scores) - nmax, len(scores)))

    prompt = '给你一些示例函数，请你参考它们设计一个更好拟合程度的函数。'
    info = infos[chosen_indexs[0]]
    assert info is not None
    prompt += f'\n\n此函数可以用于拟合 EEC，它的综合得分是 {scores[chosen_indexs[0]]}\n' + info

    for index in chosen_indexs[1:]:
        info = infos[index]
        assert info is not None
        prompt += f'\n\n此函数相比于上一个函数，为一个优化版本，其全局拟合程度更好。它的综合得分是 {scores[index]}\n' + info

    prompt += '\n你现在应该开始生成函数'

    return prompt
