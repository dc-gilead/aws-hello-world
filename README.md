# Python Hello World


## Description

This is just a basic hello world app written in Python that runs inside of Docker
This is a test after installing the python module

## Mac Setup

### Install Brew

You can visit this page: https://brew.sh/ or you can run the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Brew install


```
brew install macvim
brew install node
brew install rbenv
brew install readline
brew install terraform
brew install terraform-ls
brew install tfsec
brew install tox
brew install yarn
```

### Setup Python

```
brew install python@3.9
python3 -m pip install --upgrade pip
```

### Alias macvim as vim

Edit `~/.profile` add the following:

```
alias vim='mvim -v'
```

### Install Docker Desktop

Download the correct package based on the CHIP you have installed on your Mac

[https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)

### Setup VIM

* Copy the following [vimrc](https://github.com/briataws/vim) into `~/.vimrc`

* Install vbundle

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

* Run `:PluginInstall` against .vimrc. When you open the .vimrc you will get a bunch of errors just press `q	` over and over untill they go away. 

* coc might fail to install correctly. If that happens do the following

```
cd ~/.vim/bundle/coc.nvim
npm install
yarn install
```

* Configure coc for terraform-ls by editing `.vim/bundle/coc.nvim/.vim/coc-settings.json` with this content

```
{
  "eslint.validate": ["typescript"],
  "eslint.lintTask.options": [".", "--ext", ".ts"],
  "typescript.format.insertSpaceAfterFunctionKeywordForAnonymousFunctions": false,
  "typescript.format.insertSpaceAfterOpeningAndBeforeClosingNonemptyBraces": true,
  "typescript.suggestionActions.enabled": false
}
```


### Author
Brian Carpio

briataws@amazon.com

