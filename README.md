# Sports Data Analytics
## Counter Strike 2 Data Analysis

This project is part of the Sports Data Analytics course at the Hochschule Luzern (HSLU) as part of the Masters in Data Science. The goal of this project is to analyze data from the a sport or e-sport of our choice. We chose to analyze data from the game Counter Strike 2 because of its popularity, availability of data and personal interest in the game.

### Data

The data used in this project is from the [HLTV](https://www.hltv.org/) website. HLTV is a website that covers the competitive scene of Counter Strike 2. The data was scraped from the website using the [HLTV API] provided by Kaggle. The data contains information about Weapons, Maps, Players, Teams, Matches and Tournaments.

<details>
<summary>Folder Structure</summary>

    📦Sports-Data-Analytics
    ┣ 📂.vscode
    ┃ ┗ 📜settings.json
    ┣ 📂data
    ┃ ┣ 📜csgo_professional_games.csv
    ┃ ┣ 📜csgo_professional_players.csv
    ┃ ┣ 📜maps_statistics.csv
    ┃ ┣ 📜top_100_players.csv
    ┃ ┗ 📜weapons_statistics.csv
    ┣ 📂document_files
    ┃ ┣ 📂figure-html
    ┃ ┃ ┣ 📜cell-12-output-2.png
    ┃ ┃ ┗ 📜fig-polar-output-1.png
    ┃ ┗ 📂libs
    ┃ ┃ ┣ 📂bootstrap
    ┃ ┃ ┃ ┣ 📜bootstrap-dark.min.css
    ┃ ┃ ┃ ┣ 📜bootstrap-icons.css
    ┃ ┃ ┃ ┣ 📜bootstrap-icons.woff
    ┃ ┃ ┃ ┣ 📜bootstrap.min.css
    ┃ ┃ ┃ ┗ 📜bootstrap.min.js
    ┃ ┃ ┣ 📂clipboard
    ┃ ┃ ┃ ┗ 📜clipboard.min.js
    ┃ ┃ ┣ 📂quarto-contrib
    ┃ ┃ ┃ ┗ 📂glightbox
    ┃ ┃ ┃ ┃ ┣ 📜glightbox.min.css
    ┃ ┃ ┃ ┃ ┣ 📜glightbox.min.js
    ┃ ┃ ┃ ┃ ┗ 📜lightbox.css
    ┃ ┃ ┣ 📂quarto-html
    ┃ ┃ ┃ ┣ 📜anchor.min.js
    ┃ ┃ ┃ ┣ 📜popper.min.js
    ┃ ┃ ┃ ┣ 📜quarto-syntax-highlighting-dark.css
    ┃ ┃ ┃ ┣ 📜quarto-syntax-highlighting.css
    ┃ ┃ ┃ ┣ 📜quarto.js
    ┃ ┃ ┃ ┣ 📜tippy.css
    ┃ ┃ ┃ ┗ 📜tippy.umd.min.js
    ┃ ┃ ┗ 📂quarto-ojs
    ┃ ┃ ┃ ┣ 📜quarto-ojs-runtime.js
    ┃ ┃ ┃ ┗ 📜quarto-ojs.css
    ┣ 📂resources
    ┃ ┣ 📜csgo gameplay1.jpg
    ┃ ┣ 📜csgo logo.jpg
    ┃ ┗ 📜de_mirage-map-callouts.jpg
    ┣ 📜.gitattributes
    ┣ 📜document.qmd
    ┣ 📜index.html
    ┣ 📜journal.pdf
    ┣ 📜journal.qmd
    ┗ 📜README.md

</details>

### Analysis

The analysis is divided into the following sections:

- Weapons Analysis
- Maps Analysis
- Players (Casual) Analysis
- Players (Professional) Analysis
- Tournament Matches Analysis

Most plots were done using Plotly and hence are interactive, hover, zoom and selecting areas is possible to see further information.

### Software

The analysis was done using the Python 3 and Quarto, mixing code and markdown in the same document. The document was exported to HTML using the Quarto software.

Libraries used include:
- Pandas
- Numpy
- Matplotlib
- Plotly

I hope you enjoy the analysis and feel free to reach out if you have any questions or suggestions.

