#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) 2019-2020 All rights reserved.
# FILENAME:  dapp.py
# VERSION: 	 1.0
# CREATED: 	 2021-09-30 11:04
# AUTHOR: 	 Sitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION: Decentralized App displaying Crowdfunding Contract
#
# HISTORY: 
#*************************************************************
'''
Decentralized App displaying Crowdfunding Contract
'''
### Third-Party Packages ###
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import (
  FileResponse, HTMLResponse, PlainTextResponse
)
from fastapi.templating import Jinja2Templates

### Initiate DAPP as FastAPI App instance ###
dapp = FastAPI()

### Mount static files from /static directory ###
dapp.mount('/static', StaticFiles(directory='static'), name='static')

@dapp.get('/health', response_class=PlainTextResponse, status_code=200)
async def health(): return 'OK'

@dapp.get('/robots.txt', response_class=FileResponse)
async def robot_text():
  return FileResponse('static/robots.txt')

@dapp.get('/', response_class=HTMLResponse)
def index(request: Request):
  ### Set up HTML templates from /templates directory ###
  templates = Jinja2Templates(directory='templates')
  response = templates.TemplateResponse('index.html', { 'request': request })
  return response