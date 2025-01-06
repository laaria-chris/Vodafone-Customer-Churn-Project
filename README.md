# Customer_Churn
A project to predict whether a telco customer will churn or not

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Contributing</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Scenario
Your company executives at VodaFone have an interest reducing Customer Churn. You have to build a model that predicts customer churn to be used in preventative measures leading to reduced churn.

### Project Structure
The project uses the CRISP-DM Framework. 
Our first part covers the Business Understanding and setting up the criteria for success.  
We head to the second phase where we look at the Datasets we have and analyse them to understand the relationship between features and answer business questions.
We build a model to predict the target variable and evaluate the model performance.
We finalise by a conclsuion of the Business Impact Assessment of the model and its performance.

Finally we deploy the application using an application interface using streamlit.This is an application that implements machine learning algortihms to predict the likelyhood of a customer discountinuing usage of service for Vodafone Telco. Users can interact with the Models on the prediction page, Check training data in Data Page, view visualizations on the dashboard page and see results of their input on History Page. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

These are the key libraries used in the project.

* Jupyter Notebook
* Pandas
* Seaborn
* Matplotlib
* Streamlit
* SciKit Learn
* XGBoost

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

`

### Installation and Usage

_Below is an example of how you can install and run the notebook. This project relies on any external dependencies or services. Internet connectivity is necessary_

1. Clone the repository
   ```git clone https://github.com/laaria-chris/Vodafone-Customer-Churn-Project.git```

2. Navigate to the project directory
    ```sh
    cd Vodafone-Customer-Churn-Project
    ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
    ```

3. Download ```Customer-Churn-Dataset.csv``` and place it in the root directory.

4. Run the notebook

5. To run the project application, execute the following command:-
    ```sh
       streamlit run Home.py

    ```
- A webpage opens up to view the app
- Test a prediction by clicking on the predicitons page



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the  GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Laaria Chris - [www.linkedin.com/in/laaria-chris-641759173](www.linkedin.com/in/ramadhanmwenda)

Project Link: [https://github.com/laaria-chris/Vodafone-Customer-Churn-Project.git](https://github.com/laaria-chris/Vodafone-Customer-Churn-Project.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
 
 Resources I found helpful when building the project.

* [Machine Learning for Absolute Beginners by coderachel](https://medium.com/@coderacheal/machine-learning-for-absolute-beginners-69ce9bb08b46)
* [Imbalanced Data Best Practices](https://rihab-feki.medium.com/imbalanced-data-best-practices-f3b6d0999f38)
* [Framework for Imbalanced Classification Projects](https://machinelearningmastery.com/framework-for-imbalanced-classification-projects/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
