
from flask import Flask, render_template, request,jsonify,flash
from selenium import webdriver
import time
from flask_cors import CORS,cross_origin
# import requests
from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/results',methods=['POST','GET'])
@cross_origin()
def index():
    try:
        if request.method == 'POST':
            searchString = request.form['content'].replace(" ",'-')
            # # , headers={'User-Agent': 'Mozilla/5.0'}
            # # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            # naukri_url = requests.get('https://www.naukri.com/java-developer-jobs?k=java%20developer')
            # print(naukri_url.reason)
            # print(naukri_url.encoding)
            # print(naukri_url.headers['content-type'])
            # naukri_url.encoding=naukri_url.apparent_encoding
            # naukri_job_search_page = bs(naukri_url.content, "html.parser")
            # # print(naukri_job_search_page.prettify())
            # print(naukri_url.text)
            # jobs_list = naukri_job_search_page.find("div", { "class": "companyInfo"})
            # print(searchString+'-jobs')
            # print(jobs_list)
            details=[]
            
            options = webdriver.ChromeOptions()

            naukri_url = 'https://www.naukri.com/'+searchString+'-jobs?'

            driver = webdriver.Chrome(executable_path="chromedriver", options=options)
            driver.get(naukri_url)

            time.sleep(5)

            soup = bs(driver.page_source,'html5lib')

            print(soup.prettify())

            listOfInfo = soup.find_all("article", { "class": "jobTuple"})
            
            driver.close()
            for lists in listOfInfo:
                try:
                    # print(lists.div.div.div.a.text)
                    company_name = lists.div.div.div.a.text
                    # print(company_name.a.text)
                    
                    # print(company)

                except:
                    company_name = 'No company available'

                try:
                    
                    # job title
                    job_title_name = lists.div.div.a.text
                    


                except:
                    job_title_name = "No job title"

                
                try:

                    # Experience
                    experience_tag = lists.find_all("li",{"class": "experience"})
                    experience=experience_tag[0].text
                    # print(experience_tag[0].text)

                except:
                    experience = 'No experince required'  

                try:
                    # Salary
                    salary_tag = lists.find_all("li",{"class": "salary"})
                    salary = salary_tag[0].text 
                except:
                    salary = "No salary"

                try:
                    # Location
                    location_tag = lists.find_all("li",{"class": "location"})
                    location = location_tag[0].text 
                except:
                    location = "No Location"


                try:
                    # JD
                    job_description_tag = lists.find_all("div",{"class":"job-description"})
                    job_description = job_description_tag[0].text
                    print(job_description)
                except:
                    job_description = "No Location"
            
                mydict = {"Company": company_name,"Job Title": job_title_name, "Experience": experience, "Salary": salary, "Location": location,"Job Description": job_description}
                details.append(mydict)
            dataFrame = pd.DataFrame(details)

        # Storing the data into Pandas
        # DataFrame 
        # for i in range(0,len(details)):
            print(mydict.values())
            
            
        # Converting Pandas DataFrame
        # into CSV file
            dataFrame.to_csv("static/"+ searchString + '.csv')
            return render_template("result.html", details=details[0:(len(details)-1)],searchString=searchString)

    except Exception as e:
        print(e)
        return render_template("error.html")

@app.route("/downloads")    
@cross_origin
def download():
    # print(request.form['content'])
    # return send_file(request.form['content'] + '.csv', as_attachment=True )
    # return render_template('result.html')
    try:
        print(request.form['content'])
    except Exception as e:
        pass


if __name__ == "__main__":
    
    app.run(debug=True)