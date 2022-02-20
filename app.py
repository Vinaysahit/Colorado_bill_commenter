#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.set_page_config(page_title = "Feedback Form", layout = "wide")


# In[8]:



with st.container():
  st.markdown("<h1 style='text-align: center; color: white;'>Feedback</h1>", unsafe_allow_html=True)
  st.write("---------- ")
  st.header("You can comment on the rule. Get your voice heard to the rule makers")
  st.write("---------")


# In[4]:


form_link = """
<form action="https://formsubmit.co/onymzlsc@mailparser.io" method="POST">
     <label for="bill">Choose a bill:</label>
     <select id="bill" name="bill">
       <option value="House bill">House bill</option>
     </select>
     <input type="hidden" name ="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your full name" required>
     <input type="text" name="Verification" placeholder="State ID number/ License Number" required>
     <textarea name = "message" placeholder ="Please enter you Feedback here" required></textarea>
     <button type="submit">Send</button>
     
</form>
"""
l_col,r_col = st.columns(2)
with l_col:
  st.markdown(form_link, unsafe_allow_html=True)
with r_col:
  st.empty()


# In[5]:


def load_css(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# In[6]:


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html =True)
local_css("style.css")

