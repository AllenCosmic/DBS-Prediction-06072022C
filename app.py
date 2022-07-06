#!/usr/bin/env python
# coding: utf-8

# In[22]:


from flask import Flask, render_template, request


# In[8]:


get_ipython().system('pip install flask')


# In[23]:


import joblib


# In[24]:


app = Flask(__name__)


# In[25]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("decision_tree")
        pred2 = model2.predict([[rates]])
        result1 = pred1
        result2 = pred2
        return(render_template("index.html", result1 = pred1, result2 = pred2))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))
    


# In[ ]:


if __name__ == "__main__":
    app.run()

