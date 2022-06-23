#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 문자열에서 첫번째 단어를 찾으세요.
# 주어진 문장에는 . 과 , 가 있습니다.
# String can start with a letter, or a dot or space.
# a word can contain an appstrophe and it's a part of the word.
# the whole text can be represented with one word and that's it
# "Hello, World!" -> "Hello"
# "greeings, friends" -> "greetings"
# endwith


def first_word(text: str) -> str:
    if len(text) == 0:
        return text
    txt = text.strip().split()
    word = txt[0].strip(".,;:!-?\"'")
    return word


if __name__ == "__main__":
    print(first_word(""))
    print(first_word("Hello, World!"))
    print(first_word("greetings, friends"))
