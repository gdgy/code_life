# !/usr/bin/python
# -*- coding:UTF-8 -*-
__author__ = 'shaoyong_li'
import traceback
import weka.core.jvm as jvm
import weka.core.version as version


def main():
    """
    Just runs some example code.
    """

    print version.weka_version()


if __name__ == "__main__":
    try:
        jvm.start()
        main()
    except Exception , e:
        print(traceback.format_exc())
    finally:
        jvm.stop()
