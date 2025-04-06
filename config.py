#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7310893289:AAG2kK1vyEuhyM3UdVdppoipLqNd4VQ1wfE")
    API_ID = int(os.environ.get("API_ID", "28962746"))
    API_HASH = os.environ.get("API_HASH", "727457f88d661b08e636188a949cd9f3")
    AUTH_USERS = "7991268498"

