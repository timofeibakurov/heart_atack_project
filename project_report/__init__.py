from flask import Flask
import pandas as pd
data = pd.read_csv('project_report/static/file/heart.csv')
app = Flask(__name__)
from project_report import routes
