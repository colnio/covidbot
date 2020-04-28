#!/bin/bash

docker run -td --restart unless-stopped -v `pwd`:/app --name bot_prod bot
