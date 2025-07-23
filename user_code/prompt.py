__all__ = [
    "system_prompt",
    "prologue_section",
    "epilogue_section",
]


system_prompt = "你是一个哲学家，总是思考事物的深层意义。每次回答都带有深刻的哲理，或者提问让人思考人生的奥义。"
system_prompt = "你是一个函数拟合家，总是拟合函数"

prologue_section = (
    "我现在正在测试 IdeaSearch IdeaSearcher能否顺利运行。"
    " IdeaSearch IdeaSearcher会依据一个智能算法不断从岛屿中选择 idea ，"
    "然后说给你（大语言模型）听，让你知道我们搜寻 idea 的目的与已有的 idea ，看看你能否提出更好的点子。\n"
    "每次说给你听的 prompt 包含三个部分，现在这个部分是 prologue section 。"
    "接下来是 examples section ：\n"
)


epilogue_section = (
    "最后，这里是 epilogue section 。你可以看到，由于这只是一个用于测试IdeaSearcher运行的模板项目，"
    "所有的 examples 的得分都是随机的，请你也随便说点啥吧。"
)

prologue_section = """请你给出一个Python函数，形如：
def f(x):
    return x + 1
你的目标是拟合一个未知的函数，你可以使用多项式、指数函数、三角函数及他们的组合，但是形式不一定复杂。下面是一些例子，你能看到已有函数的表现效果，请仔细比较得分的高低。如果分数比较低，请不要拘泥于原有的形式，勇于探索！
"""

epilogue_section = "请开始你的拟合。注意，输出纯函数，不要包含在Python的代码块中，这会导致识别异常。不要添加任何的文字说明！"