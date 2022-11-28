<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br/>
<h3 align="center">Project Portfolio</h3>

  <p align="center">
    <br/>
    <br />
    <a href="https://bit.ly/portifolio-heitor-louzeiro">View Demo</a>
    ·
    <a href="https://github.com/HeitorLouzeiro/portifolio/issues">Report Bug</a>
    ·
    <a href="https://github.com/HeitorLouzeiro/portifolio/issues">Request Feature</a>
  </p>
</div>



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
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#collaborators">Collaborators</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was made to improve and disseminate my projects online in a practical and easy way and improving my knowledge with DJANGO in the BACKEND and using languages ​​to help in the FRONTEND such as JAVASCRIPT, and using markup language HTML, CSS and BOOTSTRAP in the construction of the web site.
* [Portfolio](https://bit.ly/portifolio-heitor-louzeiro)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![SQLite][SQLite]][SQLite]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![HTML][HTML]][HTML-url]
* [![CSS][CSS]][CSS-url]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
### 1.User Login Page.
<p align="center">
      <img src="src/assets/images/login.png" alt="Login">
    <br/>
</p>

  ### 2.Home Page. 
<p align="center">
    <img src="src/assets/images/home.png" alt="Home Page">
    <br/>
</p>

  ### 3.Dark Mode
<p align="center">
    <img src="src/assets/images/darkmode.gif" alt="Dark Mode">
    <br/>
</p>

  ### 4.About Me. 
<p align="center">
    <img src="src/assets/images/aboutme.png" alt="About me">
    <br/>
</p>
    
  ### 5.Curriculum page. 
<p align="center">
    <img src="src/assets/images/curriculum.png" alt="Curriculum">
    <br/>
</p>

  ### 6.Services page. 
<p align="center">
    <img src="src/assets/images/services.png" alt="Services">
    <br/>
</p>

  ### 7.Portfolio page. 
<p align="center">
    <img src="src/assets/images/portfolio.png" alt="Portfolio">
    <br/>
</p>

  ### 8.Contact Page. 
<p align="center">
    <img src="src/assets/images/contact.png" alt="Contact">
    <br/>
</p>

  ### 9.Send Emails. 
<p align="center">
    <img src="src/assets/images/sendemail.gif" alt="Send email">
    <br/>
</p>

  ### 10.CV Page. 
<p align="center">
    <img src="src/assets/images/CV.png" alt="Cv">
    <br/>
</p>


  ### 11.Save CV. 
<p align="center">
    <img src="src/assets/images/cv-pdf.png" alt="Save CV">
    <br/>
</p>
    
  ### 12.PDF CV. 
<p align="center">
    <img src="src/assets/images/cv.gif" alt="PDF Save CV">
    <br/>
</p>  

  ### 13.CRUD Modal. 
<p align="center">
    <img src="src/assets/images/crud.gif" alt="CRUD Modal">
    <br/>
</p>
<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HeitorLouzeiro/portifolio.git
   ```
2. Access the project folder in terminal/cmd
   ```sh
   cd portifolio
   ```
3. Create a virtualenv with Python 3.9.0.
   ```sh
   python -m venv venv
   ```
4. Activate virtualenv.
    * Ubunto
    ```sh
    source venv/bin/activate
    ```

    * MacOs
    ```sh
    source venv/bin/activate
    ```

    * Windows 
    ```sh
     venv/scripts/activate
    ```

5. Install as dependencies.
    ```sh
     pip install -r requirements.txt
    ```

6. Configure an instance with .env.
    ```sh
     cp .env-example .env
    ```
    or

    Copy the env-example to a new file called .env and then open it and change the variable values ​​if necessary

   
7.  Change the .env variables, put your email and gmail password, if you have two-factor security follow the tutorial below.
   * [Support Google](https://support.google.com/accounts/answer/185833?hl=pt-BR)
    
8. Run the migrations.
    ```sh
     python manage.py migrate
    ```

9.  Create a Superuser.
    ```sh
     python manage.py createsuperuser
    ``` 
    
10. Run the application.
    ```sh
     python manage.py runserver
    ```   

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- ROADMAP -->
## Roadmap
  - [x] User Login Page
  - [x] Home Page
  - [x] Create Data Home
  - [x] Edit Data Home
  - [x] Dark Mode
  - [x] About Me
  - [x] Create Data About me
  - [x] Curriculum page
  - [x] Services page
  - [x] Portfolio page
  - [x] Contact Page
  - [x] Send Emails
  - [x] CV Page
  - [x] Save CV
  - [x] CRUD Social Media
  - [x] CRUD Skills
  - [x] CRUD Progress Bar
  - [x] CRUD Card (About Me, Education, Service, Portfolio)


See the [open issues](https://github.com/HeitorLouzeiro/portifolio/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Improvements`)
3. Commit your Changes (`git commit -m 'Add my new Enhancements'`)
4. Push to the Branch (`git push origin feature/Improvements`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/42551436?s=400&u=608a3a665aa424e0d6d59b01fa634650979b72ad&v=4" width="160px;" alt="Foto do Heitor Louzeiro no GitHub"/><br>
        <sub>
          <b>Heitor Louzeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](license) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<div align='center'>  
  <a href="https://www.instagram.com/heitorlouzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank">
  </a> 
  <a href = "mailto:heitorlouzeirodev@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank">    
  </a>
  <a href="https://www.linkedin.com/in/heitor-louzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a> 
</div>

Project Link: [https://github.com/HeitorLouzeiro/portifolio](https://github.com/HeitorLouzeiro/portifolio)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HeitorLouzeiro/contact-django.svg?style=for-the-badge
[contributors-url]: https://github.com/HeitorLouzeiro/contact-django/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HeitorLouzeiro/contact-django.svg?style=for-the-badge
[forks-url]: https://github.com/HeitorLouzeiro/contact-django/network/members
[stars-shield]: https://img.shields.io/github/stars/HeitorLouzeiro/contact-django.svg?style=for-the-badge
[stars-url]: https://github.com/HeitorLouzeiro/contact-django/stargazers
[issues-shield]: https://img.shields.io/github/issues/HeitorLouzeiro/contact-django.svg?style=for-the-badge
[issues-url]: https://github.com/HeitorLouzeiro/contact-django/issues
[license-shield]: https://img.shields.io/github/license/HeitorLouzeiro/contact-django.svg?style=for-the-badge
[license-url]: https://github.com/HeitorLouzeiro/contact-django/blob/master/license
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/heitor-louzeiro

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/

[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://javascript.info/document



[SQLite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/index.html

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[HTML]:https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://github.com/HeitorLouzeiro/contact-django/#

[CSS]: 	https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://github.com/HeitorLouzeiro/contact-django/#

