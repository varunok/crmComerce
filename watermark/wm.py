# -*- coding: utf-8 -*-


import os
from selenium import webdriver
from PIL import Image, ImageEnhance



class CreateWatermark(object):
    isCreated = False
    """docstring for CreateWatermark"""
    def __init__(self, arg):
            super(CreateWatermark, self).__init__()
            self.arg = arg
        # try:
            url = "http://google.com.ua"
            path_to_phantomjs = '/'.join([os.getcwd(), 'media', 'phantomjs'])
            driver = webdriver.PhantomJS(path_to_phantomjs)
            width_image = len(self.arg)*20+10
            driver.set_window_size(width_image, 50)
            driver.get(url)
            path_to_wm_html = '/'.join([os.getcwd(), 'watermark', 'wm.html'])
            self.htmlString = htmlString
            driver.execute_script("document.write('{}');".format(self._mutable_word()))
            try:
                os.mkdir('media/watermark')
            except:
                pass
            driver.save_screenshot('media/watermark/watermark.png')
            self.isCreated = True
        # except:
        #     pass

    def _mutable_word(self):
        self.htmlString = self.htmlString.replace('\n', ' ')

        if '.' in self.arg:
            self.first_word = self.arg.split('.')[0]
            self.word_after_dot = self.arg.split('.')[1:]
            if len(self.word_after_dot) > 1:
                self.word_after_dot = '.'.join(self.word_after_dot)
            else:
                self.word_after_dot = self.word_after_dot[0]

            self.htmlString = self.htmlString.replace('first_word', self.first_word)
            self.htmlString = self.htmlString.replace('word_after_dot', self.word_after_dot)
        else:
            self.htmlString = self.htmlString.replace('first_word', '')
            self.htmlString = self.htmlString.replace('.word_after_dot', self.arg)

        return self.htmlString


class AddWatermark(object):
    def __init__(self, image, to_save=None):
        self.image = Image.open(image)
        self.to_save = to_save
        if self.to_save:
            self._add_watermark(self.image).save(self.to_save)

    def _add_watermark(self, image, opacity=0.3, wm_interval=0):
        watermark = Image.open('media/watermark/watermark.png')
        assert opacity >= 0 and opacity <= 1
        if opacity < 1:
            if watermark.mode != 'RGBA':
                watermark = watermark.convert('RGBA')
            else:
                watermark = watermark.copy()
            alpha = watermark.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
            watermark.putalpha(alpha)
        layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
        # for y in range(0, image.size[1], watermark.size[1]+wm_interval):
        #     for x in range(0, image.size[0], watermark.size[0]+wm_interval):
        #         layer.paste(watermark, (x, y))
        watermark = watermark.resize((image.size[0]/2, image.size[1]/2))
        layer.paste(watermark, (image.size[0] - watermark.size[0], image.size[1] - watermark.size[1]))
        return Image.composite(layer, image, layer)

    def watermark_in_photo(self):
        return self._add_watermark(self.image)


# img_title = Image.open('Tryndamere_OriginalSkin_old.jpg')
# watermark = Image.open('testing.png')
# add_watermark(img_title, watermark, 0.5, 2).save('new_img.jpg')

htmlString = """
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        .logo a {
          font-size: 35px;
          line-height: 35px;
          color: #bbbab8;
          text-decoration: none;
          font-family: "codpro";
        }
        .logo a span {
          color: #fccd1b;
        }
    </style>
</head>
<body>
    <div class="logo">
        <a href="#"><span>first_word</span>.word_after_dot</a>
    </div>
</body>
</html>
"""