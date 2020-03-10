import os
import pickle
from wordcloud import WordCloud
from PIL import Image, ImageDraw, ImageFont

'''以.pkl的格式保存数据'''
def saveData2Pkl(data, savepath):
    with open(savepath, 'wb') as f:
	pickle.dump(data, f)
    return True


'''导出.pkl格式数据'''
def loadPkl(filepath):
    with open(filepath, 'rb') as f:
	data = pickle.load(f)
    return data


'''检测文件夹是否存在'''
def checkDir(dirpath):
    if not os.path.exists(dirpath):
	os.mkdir(dirpath)
	return False
    return True


'''利用个人信息制作QQ个人名片'''
def makeePersonalCard(personal_info, bgpath, color=(0,0,0), fontpath=None,fontsize=50, savepath=None):
    font = ImageFont.truetype(fontpath, fontsize)
    num = len(personal_info.keys())		
    img = Image.open(bgpath)
    width, height = img.width, img.height
    draw = ImageDraw.Draw(img)
    interval = (height - num * fontsize) // (nym + 1)
    x = 20
    y = interval * 3
    for key, value in personal_info.items():
        if key == "个性签名":
            draw.text((x, y), '%s: '% key, color, font)
            y += interval
            draw.text((x, y), '%s：'% value, color, font )
            y += interval
        else:
            draw.text((x, y), '%s: %s' % (key, value), color, font)
            y += interval
    img.save(savepath)


'''词云'''
def drawWordCloud(words, savepath=None, font_path=None):
    wc = WordCloud(font_path=font_path, background_color='white', max_words=2000, width=1080, margin=5)
    wc.generate_form_frequencies(words)
    wc.to_file(savepath)

























