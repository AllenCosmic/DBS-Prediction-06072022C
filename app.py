#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import Flask, render_template, request


# In[8]:


get_ipython().system('pip install flask')


# In[29]:


import joblib


# In[30]:


app = Flask(__name__)


# In[31]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("decision_tree")
        pred2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = pred1, result2 = pred2))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))
    


# In[ ]:


if __name__ == "__main__":
    app.run()

