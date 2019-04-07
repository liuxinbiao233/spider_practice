import requests
import json

from pyecharts import Bar

from wordcloud import WordCloud
import matplotlib.pyplot as plt


url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_468882985?csrf_token='
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
response=requests.post(url,headers=headers,data=user_data)
data=json.loads(response.text)
#print(data)
hotcomments = []
for hotcomment in data['hotComments']:
    item = {
         'nickname':hotcomment['user']['nickname'],
         'content':hotcomment['content'],
         'likedCount':hotcomment['likedCount']
    }
    hotcomments.append(item)
#获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]
#点赞
bar=Bar('热门中点赞数示意图')
bar.add('点赞数',nickname,liked_count,is_stack=True,mark_line=['min','max'],mark_point=['average'])
bar.render()


#词云
content_text = ' '.join(content_list)
wordcloud = WordCloud(font_path=r'/usr/share/fonts/TTF/msyh.ttf',background_color='white',width=800,height=660).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()