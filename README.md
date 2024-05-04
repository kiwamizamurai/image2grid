<div align="center">
  <h1>image2grid</h1>
  <img src="https://raw.githubusercontent.com/kiwamizamurai/image2grid/main/example.png" alt="example output by image2grid" width="400" height="300">
  <p>
  Generate grid-like images or gifs for your GitHub README Profile.<br />Inspired by <a href=https://github.com/mathdroid/crop-github-images-cli>crop-github-images-cli</a>
  </p>
</div>

[![Publish to PyPI](https://github.com/kiwamizamurai/image2grid/actions/workflows/publish-to-pypi.yaml/badge.svg)](https://github.com/kiwamizamurai/image2grid/actions/workflows/publish-to-pypi.yaml)

## Table of contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Contribution](#contribution)
- [Thanks](#thanks)

## Features

1. Split the image into a grid
2. Create gists and upload files

## Usage

```bash
❯ image2grid ./example.gif
❯ image2grid ./example.png -t PAT
```

scoped [gist] [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) is required if you create a gists.

## Installation

```bash
❯ pipx install image2grid
```

## Contribution

Whether it's reporting bugs, suggesting features, maintaining packages, or submitting a PR, contribution is always welcome! Please read CONTRIBUTING.md for details on how to contribute to bottom.

![Alt](https://repobeats.axiom.co/api/embed/72ed4cd2868b94489518a171f0404b6de7386c74.svg "Repobeats analytics image")

## Thanks

- This project is very much inspired by [crop-github-images-cli](https://github.com/mathdroid/crop-github-images-cli)
- This project is made with reference to [bottom](https://github.com/ClementTsang/bottom)
