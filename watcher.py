# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
06 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from srcs.twitterListener import analyseTwitter

'''Runner for the tweeter listening.
Supposed to run in a crontab.
################################################### '''

def main():
    analyseTwitter()
    return


if __name__ == "__main__":
    main()
