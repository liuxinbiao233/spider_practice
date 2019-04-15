STOP_WORDS_PATH = './stop_words.txt' # 敏感/禁止词文件
GREY_OUTPUT_PATH = './output/WordCloudDefautColors.png'  # 随机配色词云存放路径
PAINTED_OUTPUT_PATH = './output/WordCloudColorsByImg.png'# 基于背景图着色的词云存放路径
MAX_WORD = 120                                           # 词云最大单词数量
headers={
    'Host': 'music.163.com',
    'Origin':'https://music.163.com',
    'Referer': 'https://music.163.com/song?id=468882985',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
user_data={
    'params': 'HltL+mbVeUhLabt3IgydWiNvA2hAdwx2KRQs+Mjc5Ra9nJWpeF1id0xh9Ez1L2gzMHIxTydR7GB0QPbfJw2R5E6jMEnCQl8f8RLzk0DkFBeCl/caafs2p2UPomQz1oqjXxr9M6W2abv1re9st4PCt3uT1uWDNPil4JsLbDfaUWLykVZjQnT//JDK52f55RJy',
    'encSecKey':'ad7a7318514b54e958d9c697ef1603d6dd06da17a27a714692990749ec4ab7031da621d9e667ba8603ebc135e87621db55edc371e71972f794d4576f88e37a60bc71cf998c93f7bb6627a256f56475e27f2fb384665d4de9a7a2538a7aea1ea6f30fb8d0b4dd7b8df5ad1e15303576c93ebab4635aaeb6336b6cfc308bd9052c'
}