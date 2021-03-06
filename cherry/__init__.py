# -*- coding: utf-8 -*-

"""
Naive Bayes Classifier
~~~~~~~~~~~~~~~~~~~~~
cherry is a python classifier library
usage:
   >>> import cherry
   >>> result = cherry.classify('警方召开了全省集中打击赌博违法犯罪活动专项行动电视电话会议。会议的重点是“查处”六合彩、赌球赌马等赌博活动。')
   >>> result.percentage
   [('normal.dat', 0.7310585786300049), ('gamble.dat', 0.2689414213699951)]
   >>> result.words_list
   [('查处', 1.6550930245052333), ('电视电话会议', 0.844162808288905), ('活动', 3.0746199776976972), ('赌博', 1.8186042209197311), ('警方', 2.7900729573442176), ('六合彩', 1.4727714677112775), ('违法犯罪', 2.7900729573442176), ('全省', 1.0673063596031147), ('集中', 1.1626165394074395), ('召开', 1.2496279163970687), ('打击', 3.0687863598132381), ('专项', 1.5373099888488495), ('赌球', 1.7604535401630592), ('会议', 2.0969257767842722), ('重点', 2.0228178046305505), ('赌马', 0.1510156277289596), ('行动', 2.3482402050651787)]

:copyright: (c) 2018-2019 by Windson Yang
:license: MIT License, see LICENSE for more details.
"""

# workflow: search -> display -> train -> classify -> performance
from .api import classify, train, performance, search, display
