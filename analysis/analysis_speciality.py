# -*- coding: utf-8 -*-

import json
import codecs
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

ALL_SUBJECTS = ["物理", "化学", "生物", "历史", "地理", "政治", "技术"]
ALL_COUNTER = {}

def drawSubjects(sub_data, spec) :
    subjects = sub_data['subject']
    ret = []
    for sub in ALL_SUBJECTS:
        if subjects.find(sub) != -1:
            ret.append(sub)
    return ret

# all_counter = { one_spec : {spec_class : "spec", school_couner: 1, no_request_school: 1, sub_wuli: 1 , sub_wuli_huaxue : 1}, ...}
#
#
def disposeOneSpec(sub_data, spec):
    if spec not in ALL_COUNTER:
        one_dict = {'spec_class': sub_data['spec_class'], 'school_couner': 0, 'no_request_school': 0, 'sub_wuli': 0,
                    'sub_huaxue': 0, 'sub_shengwu': 0, 'sub_lishi': 0, 'sub_dili': 0, 'sub_zhengzhi': 0, 'sub_jishu': 0}
        ALL_COUNTER[spec] = one_dict

    if spec in ALL_COUNTER:
        one_spec_dict = ALL_COUNTER[spec]
        one_spec_dict['spec_class'] = sub_data['spec_class']
        one_spec_dict['school_couner'] += 1
        subjects = drawSubjects(sub_data, spec)
        for sub in subjects:
            if sub == '物理':
                one_spec_dict['sub_wuli'] += 1
            elif sub == '化学':
                one_spec_dict['sub_huaxue'] += 1
            elif sub == '生物':
                one_spec_dict['sub_shengwu'] += 1
            elif sub == '历史':
                one_spec_dict['sub_lishi'] += 1
            elif sub == '地理':
                one_spec_dict['sub_dili'] += 1
            elif sub == '政治':
                one_spec_dict['sub_zhengzhi'] += 1
            elif sub == '技术':
                one_spec_dict['sub_jishu'] += 1
            else:
                one_spec_dict['no_request_school'] += 1
        if len(subjects) == 0:
            one_spec_dict['no_request_school'] +=1


def writeCsvFile(file):
    fd = open(file, 'w')
    fd.write('专业, 专业大类, 有该专业的学校数量, 物理, 化学, 生物, 历史, 地理, 政治, 技术, 没有学科要求的学校数量\n')
    for one_spec in ALL_COUNTER.keys():
        one_dict = ALL_COUNTER[one_spec]
        line = one_spec + ',' + one_dict['spec_class'] + ',' + str(one_dict['school_couner']) + ',' + \
               str(one_dict['sub_wuli']) + ',' + str(one_dict['sub_huaxue']) + ',' + str(one_dict['sub_shengwu']) + ',' + \
               str(one_dict['sub_lishi']) + ',' + str(one_dict['sub_dili']) + ',' + str(one_dict['sub_zhengzhi']) + ',' + \
               str(one_dict['sub_jishu']) + ',' + str(one_dict['no_request_school']) + '\n'
        fd.write(line)
    fd.close()

if __name__ == '__main__':
    fd = codecs.open('../data_cn.json', 'r', encoding='utf-8')
    lines = fd.readlines()
    regex = re.compile(r'\\(?![/u"])')
    i = 1
    spec_school_counter = {}

    for line in lines:
        ls = line.strip()
        fixed = regex.sub(r"\\\\", ls)
        js = json.loads(fixed)
        print i
        print js
        i += 1
        specialities = js['specialities']
        if len(specialities) > 1:
            specs = specialities.split(',')
            for one_sub in specs:
                disposeOneSpec(js, one_sub)
        else :
            spec_class = js['spec_class']
            disposeOneSpec(js, spec_class)
    fd.close()

    writeCsvFile('专业统计结果.csv')


