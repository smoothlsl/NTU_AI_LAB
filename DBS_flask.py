#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask


# In[6]:


app = Flask(__name__)


# In[7]:


from flask import request,render_template
import joblib
@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        name = request.form.get("name")
        rates = request.form.get("rates")
        print(name, rates)
        model = joblib.load("DBS Regression Model")
        pred = model.predict([[rates]])
        pred = pred[0][0]
        s = "The predict DBS share price is : "+str(pred)
        return(render_template("main.html", results = s))
    else:
        return(render_template("main.html", results = " "))


# In[8]:


app.run()


# In[ ]:




