# FreqTrade Strategies

Common, popular, and hand-made personal strategies that I'm testing.

#### The most effective strategy is the BusyGuy, and it won´t receive public updates. You can use it at your own risk if you like.

# Compatibility

Last FreqTrade compatibility version: **2024.11 - Interface 2**

# How to run

You should have your own structure to run the FreqTrade and optionally the FreqTrade UI. Please check out the [FreqTrade](https://freqtrade.io/) website for more information about the first steps.

To run my strategies, place the strategy file and its `{Strategy Name}.json` single file inside the `strategies` folder.

Files from the `config` folder should be placed inside the FreqTrade `user_data` folder, you should indicate the path for the configuration files on the execution command line.

For a multiple bots routine, the `config.json` file is the base for all your bots and you don´t need to duplicate it. The `BusyGuy.config.json`, for example, contains only a specific configuration for that strategy execution and can override some parts of the base configuration.

**If some required files mentioned below do not exist, you may receive some fatal errors because of unexistent files. 
For example, the database and logs files, but you can create them manually or just start the container again.**

## Docker-compose example file

```
version: '3'
services:
    
  BusyGuy:
    image: freqtradeorg/freqtrade:2024.6
    restart: unless-stopped
    volumes:
      - ./user_data:/freqtrade/user_data
      # fix datetime issue, for linux operation systems
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "8082:8080"
    command: >
      trade
      --logfile /freqtrade/user_data/logs/freqtrade_BusyGuy.log
      --db-url sqlite:////freqtrade/user_data/databases/tradesv3_BusyGuy.sqlite
      --config /freqtrade/user_data/configs/config.json
      --config /freqtrade/user_data/configs/BusyGuy.config.json
      --strategy BusyGuy
```

Check out the docker-compose example file and run it with:

`docker-compose --file docker-compose.example.yml up`


# Sponsors

To be honest, achieving a great quality trading bot strategy is not easy and requires a bunch of tests, research, and spending resources. For this reason, only the Busy Guy strategy is public.

I have other strategies that are actively in development, with consistent testing and growth. Some of them are already being used in the live market.

> Keep in mind that I can not guarantee your profits but I give you what I use for myself, so I expect you to have great results.

If you want to have access to my private strategies, please contact me by email: mf-ft-bots.q8kcc@passmail.net

# Buy me a coffee

Totally not required, but if you want to recognize my efforts, please contribute via the Crypto Networks below. Thank you so much!

```
Solana: 7qMcg2tb4LGe2JzAXvYW9anto9ZTwLj6U2cEaG2ZSozU
Polygon: 0xC234c9Efb266b47FEA0c19B910F59847952b10b3
Bitcoin: bc1q6kdhngruw9mf7lfsenslrzyu3gh8slm4mme5m3
Litecoin: ltc1qp8d484ztpm97vx822yqru2mv7paa5z02yetgnf
```
