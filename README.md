<p align="center"><img src="static/logo 3x2.png" width= "40%" ></p>

## Inspiration
Ever toured websites such as **Linkedin**, **Fortune500**, **Forbes** and believed it would have been exceptional if you could perceive all the _data_ existing in the website in an easy-to-use format preferable a _CSV_ or _JSON_, and then apply your codes or statistical analysis?
It's a **yes** for several _data scientists_ and _business analysts_ who frequently invest their time trying to find suitable data and regenerate it into a suitable format so that they can apply _data visualization_ and other _data analytics_.
**Datafy** originated at that instant when I was once challenged by my internship company to accumulate the data of top retailing companies in the world. After a day of googling, I landed at a conclusion to use the **Fortune500** website as my reservoir of data. But why stop at one domain when I can apply it for all potential circumstances? And that's how it all started.

[check out the website](https://datafy-fortune500.herokuapp.com/)

[Demo video](https://youtu.be/kc9OiZvno9A)

## What it does
Datafy is a **web scraped data provider website**, effortlessly download _CSV_ and _JSON_ Data of Companies listed in **Fortune 500**

## Datafy for:
1. **Developers**: CSV and JSON format make data convenient to handle and implement various data science tools, PowerBI, and it stands developer-friendly
2. **Procurement & Spend Analytics**: Datafy lets businesses discover the apt vendor or clients that can help their company reach the precise target audience and be lucrative
3. **Investors**: Datafy exhibits revenue change, profit rate, and other former statistics of companies which assists the investors and stockholders get sound shrewdness through data, and statistics
4. **Seekers**: Datafy provides the records of prestigious organizations honored by Fortune 500, where every student and a job seeker endeavors to be an employee

## How I built it
1. **Web Scrapping**: I used **Selenium**, **Chrome driver**, **python** for web scrapping the data from The Fortune500 website.

[Github link to website code](https://github.com/Shakthi-Dhar/DatafyWebsite)

[Github link to web scrapping tool](https://github.com/Shakthi-Dhar/scrapping_api)

2. **Database**: This data that has been scrapped is converted into _JSON_ and _CSV_ format and stored in **Firebase Cloud Storage**
3.**Website**: Developed a _beautiful web application_ (for best UI use in laptop/desktop) that sends a request to download the data from the firebase cloud storage and saves it on the user's local system. 

[Check out the website](https://datafy-fortune500.herokuapp.com/)

## Challenges I ran into
1.**Deployment**: _Heroku_ does not allow any request that lasts for more than _30sec_ and _selenium web scrapping_ is a time-consuming process, hence I need to switch to **Firebase** as my server and send a download request to the database rather than creating one instantaneously.
2.**UI**: The UI is not very compatible with mobile screen resolutions
3.**Download**: Creating a download request in _JSON_ and _CSV_ format was giving some internal server error when hosted.

## Accomplishments that I'm proud of
1. I have learned to use the **Firebase cloud storage** and how to send a download and insert request.
2. Making a **dark-themed UI** that is compatible with most of the device is a great achievement for me
3. Putting my web scrapping skills into help for other data scientists is a commendable achievement

## What I learned
1. Flask Cloud storage
2. HTML, CSS scroll button feature and cards system

## What's next for DATAFY
Currently, Datafy focuses on extracting data from _The Fortune500 website_, but in **LinkedIn**, there are more than **50 million companies** which I aim to extract information from and present it to all the Data scientists out there in the world.
