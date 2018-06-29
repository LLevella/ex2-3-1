import chardet
import json
import xml.etree.ElementTree as ET
import os

def input_text_data(str_file_name):
    with open(str_file_name, 'rb') as f:
        txt_fr = f.read()
        encod = chardet.detect(txt_fr)
        s = txt_fr.decode(encod['encoding'])
    return s


def input_json_data(str_file_name):
    sjson = json.loads(input_text_data(str_file_name))
    s = ''
    for sj in sjson['rss']['channel']['items']:
        s += sj['description']
    return s


def input_xml_data(str_file_name):
    tree = ET.ElementTree(ET.fromstring(input_text_data(str_file_name)))
    descs = tree.findall("*/item/description")
    s = ''
    for desc in descs:
        s += desc.text
    return s


def text_data_to_string(s_file, s_end):
    str_file_name = s_file + '.' + s_end
    if s_end == "txt":
        return input_text_data(str_file_name)
    if s_end == "json":
        return input_json_data(str_file_name)
    if s_end == "xml":
        return input_xml_data(str_file_name)


def text_to_words(n_letters, intext):
    symbols = ',.!?:;"\''
    words_list  = [ w.strip(symbols) for w in intext.split() if len(w.strip(symbols)) > n_letters]
    return words_list


def list_to_dict(n_words, words_list):
    words_dict = {w: words_list.count(w) for w in words_list}
    counted_words_list = sorted(words_dict.items(), key = lambda vx: vx[1], reverse=True)[:n_words]
    return counted_words_list


def file_analys(s_beg, s_end):
    s = text_data_to_string(s_beg, s_end)
    lw = text_to_words(6, s)
    low = list_to_dict(10, lw)
    return low
