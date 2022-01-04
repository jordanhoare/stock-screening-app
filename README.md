FastAPI Stock Screening App 
============
[![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://jordanhoare.com/stock-app) [![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/stock-screening-app.svg)](https://github.com/jordanhoare/stock-screening-app/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/stock-screening-app.svg)](https://github.com/jordanhoare/stock-screening-app/issues) [![Current Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/jordanhoare/stock-screening-app) 

![Alt Text](https://media4.giphy.com/media/z0KKfDR5NLVAkBiJay/giphy.gif?cid=790b7611583c8efd8e2958f2dee875629b2e666500b88222&rid=giphy.gif)

This is a python application powered by FastAPI and yfinance that provides an easy to use UI to retrieve financial data.  


## Project check-list 
- [x] connect to SQLite 
- [x] define a function to query the db, 
- [x] app.post to fetch stock data from yfinance
- [x] store data using sqlalchemy
- [x] add SemanticUI & filter functionality
- [ ] create a click-through higher level summary
- [ ] create api to email on key indicator markers


## Future improvements
- [ ] host on an external db (AWS or Postgres) 
- [ ] host via firebase for a live demo


## Local
Clone this repo to your desktop and run `_______` to install all the dependencies.

Using bash/unix cl: navigate to `/stock_screening_app` then run `chmod +x run` to launch uvicorn using `./run`.


## Deploying to Heroku
You can deploy the app to Heroku using:
`heroku login`
`heroku create`
`git push heroku master`



## Links
<p align="center">
    <a href="https://www.linkedin.com/in/jordan-hoare/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="https://www.kaggle.com/jordanhoare">
        <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="mailto:jordanhoare0@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="https://www.facebook.com/profile.php?id=100011746816986">
        <img
            src="https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white" />
    </a>
</p>