#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:21:37 2019

@author: angelo
"""

from count_words import count_words
from termcolor import colored

test_list = {
    ("a e i o u", 1): 5,
    (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        7,
    ): 9,
    (
        """BGP: Border Gateway Protocol.
              It is the Internet’s de facto interdomain routing protocol.
              It is well known to have many security vulnerabilities due to the very nature of its underlying assumptions of trust amongindependently operated networks.
              2017 incidents per country:
                  BR		2853
                  US		 890
                  IR		 651
                  IN		 406
                  ID		 312""",
        2,
    ): 14,
}

if __name__ == "__main__":
    for test_case, result in test_list.items():
        val = count_words(*test_case)
        if val == result:
            print("Test case: {}\t".format(test_case), colored("OK", "green"))
        else:
            print(
                "Test case: {}\t".format(test_case),
                colored(
                    "NOK, risultato atteso {}, risultato fornito {}".format(
                        result, val
                    ),
                    "red",
                ),
            )
