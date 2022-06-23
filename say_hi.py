#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 이름과 나이를 입력받아, 인사말을 출력하는 함수
def say_hi(name: str, age: int) -> str:
    print("Hi, I'm {} ! I'm {} years old.".format(name, age))


if __name__ == "__main__":
    say_hi("John", 20)
