#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7568454294:AAGAwmx-hL_ArwgfIE-ZLlmT3mJbVYSu-uo")
    API_ID = int(os.environ.get("API_ID", "26537149"))
    API_HASH = os.environ.get("API_HASH", "2697a63a384fd9b95520ee63530f6a75")
    AUTH_USERS = "7991268498"

