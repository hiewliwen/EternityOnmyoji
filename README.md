<br/>
<p align="center">
  <a href="https://github.com/hiewliwen/EternityOnmyoji">
    <img src="images/Shiranui.png" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">Onmyoji Bot for Eternity Guild</h3>

  <p align="center">
    A Discord bot to assist Seimei in taming the Shikis.
    <br/>
    <br/>
    <a href="https://github.com/hiewliwen/EternityOnmyoji"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/hiewliwen/EternityOnmyoji">View Demo</a>
    .
    <a href="https://github.com/hiewliwen/EternityOnmyoji/issues">Report Bug</a>
    .
    <a href="https://github.com/hiewliwen/EternityOnmyoji/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/hiewliwen/EternityOnmyoji/total) ![Forks](https://img.shields.io/github/forks/hiewliwen/EternityOnmyoji?style=social) ![Issues](https://img.shields.io/github/issues/hiewliwen/EternityOnmyoji) ![License](https://img.shields.io/github/license/hiewliwen/EternityOnmyoji) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

A Discord bot for Eternity guild that helps players with the daily gameplay of Onmyoji. 

It has event reminders and queries for bounty locations and mystery amulet circles. 

Most of the information are from [Eternity Onmyoji](https://onmyojiguide.com/) website. 

## Built With



* [SQLite](https://www.sqlite.org/index.html)
* []()
* [Discord.py](https://github.com/Rapptz/discord.py)

## Getting Started


### Prerequisites

1. Create an new conda environment
```
conda create --name my_env
```

2. Install Python Prerequisites
```
conda install --file requirements.txt
```

3. Create a Discord bot account
[Guide](https://discordpy.readthedocs.io/en/stable/discord.html)

### Installation

1. Clone the repo

```sh
git clone https://github.com/hiewliwen/EternityOnmyoji.git
```

2. Enter your Discord token in [SECRET.py](SECRET.py)

3. Change the Channels/Roles IDs in [CONFIG.py](CONFIG.py)according to your Discord channel

4. Invite the Discord bot into your server. 

5. Run the script. 
```
python3 main.py
```

## Usage

```
BountyLocations:
  by_clue        (.c) Search bounty locations by clue(s).
  by_name        (.n) Search bounty locations by shikigami name.
Misc:
  game_time      (.gt) Display current game time in EST format.
  userinfo       (.ui) Display the information of a specific user.
MysteryCircle:
  mystery_circle (.m) Display the mystery amulet summoning circle for the month.
​No Category:
  help           Shows this message

Type .help command for more info on a command.
You can also type .help category for more info on a category.
```

## Roadmap

See the [open issues](https://github.com/hiewliwen/EternityOnmyoji/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/hiewliwen/EternityOnmyoji/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/hiewliwen/EternityOnmyoji/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/hiewliwen/EternityOnmyoji/blob/main/LICENSE.md) for more information.

## Authors

[HIEW Li Wen](https://github.com/hiewliwen/)

