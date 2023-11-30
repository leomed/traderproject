data = {
  "Meta Data": {
    "1. Information": "Daily Prices (open, high, low, close) and Volumes",
    "2. Symbol": "IBM",
    "3. Last Refreshed": "2023-11-28",
    "4. Output Size": "Compact",
    "5. Time Zone": "US/Eastern"
  },
  "Time Series (Daily)": {
    "2023-11-28": {
      "1. open": "155.4400",
      "2. high": "155.7450",
      "3. low": "154.8600",
      "4. close": "155.6500",
      "5. volume": "2666182"
    },"2023-11-27": {
      "1. open": "154.9900",
      "2. high": "156.1350",
      "3. low": "154.7500",
      "4. close": "155.5700",
      "5. volume": "4053093"
    },
    "2023-11-24": {
      "1. open": "155.1300",
      "2. high": "155.4000",
      "3. low": "153.9200",
      "4. close": "155.1800",
      "5. volume": "1799161"
    },
    "2023-11-22": {
      "1. open": "154.5000",
      "2. high": "155.7050",
      "3. low": "154.1600",
      "4. close": "155.1300",
      "5. volume": "3045091"
    },
    "2023-11-21": {
      "1. open": "154.6000",
      "2. high": "154.6600",
      "3. low": "153.5100",
      "4. close": "153.9100",
      "5. volume": "2859508"
    },
    "2023-11-20": {
      "1. open": "152.5100",
      "2. high": "154.6800",
      "3. low": "152.3500",
      "4. close": "154.3500",
      "5. volume": "3658936"
    },
    "2023-11-17": {
      "1. open": "153.2900",
      "2. high": "153.5000",
      "3. low": "152.4601",
      "4. close": "152.8900",
      "5. volume": "4426676"
    },
    "2023-11-16": {
      "1. open": "153.0000",
      "2. high": "153.3500",
      "3. low": "152.1300",
      "4. close": "153.0600",
      "5. volume": "3519172"
    },
         }}






dict = data["Time Series (Daily)"]


new_list = [(key,value) for (key, value) in dict.items()]



# yesterday_closed = float(new_list[0][1]["4. close"])
# day_before_yesterday_closed = float(new_list[1][1]["4. close"])

yesterday_closed = -50
day_before_yesterday_closed = 10

print(yesterday_closed)
print(day_before_yesterday_closed)
difference = yesterday_closed - day_before_yesterday_closed

percentage = abs(round(difference,2))

if percentage > 5:
  print("Be careful")
else:
  print("Not")
