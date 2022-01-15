FastAPI Stock Screening App 
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/stock-screening-app.svg)](https://github.com/jordanhoare/stock-screening-app/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/stock-screening-app.svg)](https://github.com/jordanhoare/stock-screening-app/issues) [![Current Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/jordanhoare/stock-screening-app) 

![Alt Text](https://media4.giphy.com/media/z0KKfDR5NLVAkBiJay/giphy.gif?cid=790b7611583c8efd8e2958f2dee875629b2e666500b88222&rid=giphy.gif)

A python app that retrieves financial data of Yahoo Finance listed stocks, stores it in a SQL database, and provides an easy-to-use UI to filter by finance metrics.  

 
## Project Features
- [x] instantiate the project using pyenv, poetry
- [x] connect to SQLite with sqlalchemy object related mapping
- [x] add SemanticUI & filter functionality
- [x] script to fetch stock data from yfinance
- [ ] dockerize the app
- [ ] create Github Action to batch scrape
- [ ] create a click-through higher level summary
- [ ] regression modelling for buying markers
- [ ] create api to email on key indicator markers


</br>

## Requirements (Python)  
- Pyenv
- Poetry 

</br>

## Installation
To demo this application: clone the repo, navigate to the project folder and run `poetry shell` to open the venv.  Run the ` __main__.py ` file to start the server.  You can then access the web UI @ `http://127.0.0.1:8000/`


</br>

</br>


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
</p>
