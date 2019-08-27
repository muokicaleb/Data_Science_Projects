#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
from requests import post


# In[3]:


post_data = {
    "curr_id": "6408",
    "smlID": "1159963",
    "header": "AAPL+Historical+Data",
    "st_date": "08/27/2009",
    "end_date": '08/22/2019',
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action": "historical_data"

}

url_header = {
    "Host": "www.investing.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "173",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.investing.com/equities/safaricom-historical-data",
    "Cookie": "PHPSESSID=bf701n9pdqang2dlpbio9alu5a; adBlockerNewUserDomains=1566886624; StickySession=id.92576375680.767_www.investing.com; adbBLk=1; billboardCounter_1=0; G_ENABLED_IDPS=google; r_p_s_n=1; SideBlockUser=%61%3a%32%3a%7b%73%3a%31%30%3a%22%73%74%61%63%6b%5f%73%69%7a%65%22%3b%61%3a%31%3a%7b%73%3a%31%31%3a%22%6c%61%73%74%5f%71%75%6f%74%65%73%22%3b%69%3a%38%3b%7d%73%3a%36%3a%22%73%74%61%63%6b%73%22%3b%61%3a%31%3a%7b%73%3a%31%31%3a%22%6c%61%73%74%5f%71%75%6f%74%65%73%22%3b%61%3a%31%3a%7b%69%3a%30%3b%61%3a%33%3a%7b%73%3a%37%3a%22%70%61%69%72%5f%49%44%22%3b%73%3a%34%3a%22%36%34%30%38%22%3b%73%3a%31%30%3a%22%70%61%69%72%5f%74%69%74%6c%65%22%3b%73%3a%30%3a%22%22%3b%73%3a%39%3a%22%70%61%69%72%5f%6c%69%6e%6b%22%3b%73%3a%32%38%3a%22%2f%65%71%75%69%74%69%65%73%2f%61%70%70%6c%65%2d%63%6f%6d%70%75%74%65%72%2d%69%6e%63%22%3b%7d%7d%7d%7d; sideBlockTimeframe=max; geoC=KE; gtmFired=OK; nyxDorf=Z2YyYGYuNWE1Yz4sNWdlbj5tN3JjZTo6PTo%2F",
}
url = "https://www.investing.com/instruments/HistoricalDataAjax"


# In[4]:


response = post(url, headers=url_header, data=post_data)


# In[5]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[6]:


aa = soup.find("table", {"id": "curr_table"}).findAll("tr")


# In[7]:


with open('outfile.csv', 'a+') as f:
        f.write("date,\tyear,\tprice,\topen,\thigh,\tlow,\tvol,\tchange")
        f.close()
for tr in aa:
    tds = tr.find_all('td')
    dat_list = []
    for t in tds:
        dat_list.append(t.text)
    with open('outfile.csv', 'a+') as f:
        for item in dat_list:
            f.write("%s,\t" % item)
        f.write("\n")


# In[ ]:




