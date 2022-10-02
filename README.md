<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>



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



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/badal8381/spokentutorial">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Spoken Tutorial</h3>

  <p align="center">
    A web application with features like Text To Speech and VideoMerge
    <br />
    <br />
    <a href="https://github.com/badal8381/spokentutorial">View Demo</a>
    ·
    <a href="https://github.com/badal8381/spokentutorial/issues">Report Bug</a>
    ·
    <a href="https://github.com/badal8381/spokentutorial/issues">Request Feature</a>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
- Text To Speech takes a text file as input and gives a voiceover of it. You can upload your transcript as a text file and get it converted into speech within few seconds..
- VideoMerge takes video and audio files as input and return a new video after merging and compressing it..

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![django][django]][django-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python3

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/badal8381/spokentutorial.git
   ```
2. cd into the cloned directory
   ```sh
   cd spokentutorial
   ```
3. Create a python virtual environment
   ```sh
   virtualenv venv
   ```
4. Activate the virtual environment 
   ```sh
   source venv/bin/activate
   ```
5. Install the required pakages from requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
6. Run the Django server
   ```sh
   python manage.py runserver
   ```

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

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/badal8381/spokentutorial.svg?style=for-the-badge
[contributors-url]: https://github.com/badal8381/spokentutorial/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/badal8381/spokentutorial.svg?style=for-the-badge
[forks-url]: https://github.com/badal8381/spokentutorial/network/members
[stars-shield]: https://img.shields.io/github/stars/badal8381/spokentutorial.svg?style=for-the-badge
[stars-url]: https://github.com/badal8381/spokentutorial/stargazers
[issues-shield]: https://img.shields.io/github/issues/badal8381/spokentutorial.svg?style=for-the-badge
[issues-url]: https://github.com/badal8381/spokentutorial/issues
[product-screenshot]: images/screenshot.png
[django]: https://img.shields.io/badge/django-092C1E?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://www.djangoproject.com/