### 🏁 Some strategies are under active development phase, or having the final strategy being validated with the current market status, a testing mode on with live market data.

# FreqTrade Strategies
common, popular and hand-made personal strategies that I'm testing.

**!!! The latest stable strategy is the Busy Guy, others are not updated.**

# Compatibility

Last FreqTrade compatibily version: **2024.10**

# How to run

You should have you own structure to run the FreqTrade and optionally the FreqTrade UI. Please check out the [FreqTrade](https://freqtrade.io/) website for more information about the first steps.

To run my strategies, place the strategy file and its `{Strategy Name}.json` single file inside the `strategies` folder.

Files from the `config` folder should be placed inside the FreqTrade `user_data` folder, you should indicate the path for the configuration files on the execution command line.

For a multiple bots routine, the `config.json` file is the base for all your bots and you don´t need to duplicate it. The `BusyGuy.config.json`, per example, contains only specific configuration for that strategy execution and can override some parts of the base configuration.

**If some required files mentioned below do not exists, you maybe receive some fatal errors because of unexistent files. 
Per example, the database and logs files, but you can create them manually or just start the container again.**

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


# Buy me a coffee

Tottally not required, but if you want to recognize my efforts, please contribute via the Crypto Networks below. Thank you so much!

```
Solana: 7qMcg2tb4LGe2JzAXvYW9anto9ZTwLj6U2cEaG2ZSozU
Polygon: 0xC234c9Efb266b47FEA0c19B910F59847952b10b3
Bitcoin: bc1q6kdhngruw9mf7lfsenslrzyu3gh8slm4mme5m3
Litecoin: ltc1qp8d484ztpm97vx822yqru2mv7paa5z02yetgnf
```
