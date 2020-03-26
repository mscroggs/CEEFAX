# CEEFAX
This repository contains Python code to run a CEEFAX style screen.

Install CEEFAX with:
```shell
pip3 install .
```

## Repository contents
The files that make up CEEFAX (`/ceefax`) are organised as follows:

| Directory    | Contents                                   |
| ------------ | ------------------------------------------ |
| `/ceefax`    | The main ceefax class                      |
| `/ceegraph`  | Terminal graph plotting functions          |
| `/cupt`      | CuPT, the **Cu**rses **P**rinting **T**ool |
| `/error`     | Error logging functionality                |
| `/files`     | Data files needed by pages                 |
| `/fonts`     | Terminal block fonts                       |
| `/functions` | Functions used by multiple pages           |
| `/helpers`   | Url, tweet and file handling helpers       |
| `/page`      | The `Page` and `PageManager` classes       |
| `/printer`   | The `Printer` class that print fonts       |
