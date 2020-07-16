import glassdoorscrapping as gs
import pandas as pd

path = 'C:/Users/Dell/Desktop/R & VS/data science/Data_Science_proj/chromedriver.exe'


df = gs.get_jobs('data scientist',110, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
