from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    wwarara = models.CharField(max_length=10)

class LRmachine(models.Model):
    stock_symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.stock_symbol

    def __len__(self):
        return int(len(self.stock_symbol))

    def Converter(sid):
        import datetime as dt
        import matplotlib.pyplot as plt
        from matplotlib import style
        import pandas as pd
        import numpy as np
        import xlrd
        from sklearn import linear_model
        from sklearn.linear_model import LinearRegression
        from sklearn import datasets
        import calendar
        import json
        from datetime import date
        from pandas_datareader import data
        from PIL import Image
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        plt.figure(clear=True)
        cwd = os.getcwd()
        fname = os.path.join(cwd, "static")
        today = date.today()
        start_date = "2000-01-01"
        end_date = "{}".format(today)
        #sid = input(str("What is your stock id you want to search"))
        df = data.DataReader(sid, "yahoo", start_date, end_date)
        #panel_data.to_csv(path_or_buf = location, index=False)
        print(df.reset_index(level=0, inplace=True)) #it worked!
        date = df["Date"]
        price = df["Adj Close"]
        X = date
        y = price
        X = X.rename_axis("Date")
        y = y.rename_axis("Price")
        X = X.values.astype("datetime64[D]").astype(int) # a aproblem here
        X = pd.Series(X)
        type(y)
        type(X)
        X = X.values.reshape(-1,1)
        Y = y.values.reshape(-1,1)
        lm = linear_model.LinearRegression()
        model = lm.fit(X,y)
        predictions = lm.predict(X)
        #print(predictions)
        linear_regressor = LinearRegression()
        linear_regressor.fit(X, y)
        Y_pred = linear_regressor.predict(X)
        """"plt.plot(X, Y_pred, y, color="red", )
        plt.show()"""
        plt.title("{} price chart with Linear Regression Analysis on it".format(sid))
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.plot(X,y)
        plt.plot(X, Y_pred, color="red")
        try:
            plt.savefig(os.path.join(BASE_DIR, "static", "picture.png"))
        except:
            plt.savefig(os.path.join(fname, 'picture.png'))
        plt.figure(clear=True)
        """plt.title("{} price chart with Linear Regression Analysis on it".format(sid))
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.plot(X,y)
        plt.plot(X, Y_pred, color="red")
        plt.savefig(os.path.join("lulutasoai.pythonanywhere.com", "static", "picture.png"))
        plt.figure(clear=True)"""

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
