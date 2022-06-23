#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 문장을 trim 해야 한다.
# 문장의 첫글자는 대문자 이어야 한다.
# 문장의 마지막은 마침표로 끝나야 한다.


def correct_sentence(sentence: str) -> str:
    txt = sentence.strip()
    if len(txt) == 0:
        return txt

    if txt[0] != txt[0].upper():
        txt = txt[0].upper() + txt[1:]
    if not txt.endswith("."):
        txt += "."
    return txt


if __name__ == "__main__":
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))
    print(correct_sentence("Greetings, friends.."))
