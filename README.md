# Python Hello World


## Description

This is just a basic hello world app written in Python that runs inside of Docker
This is a test after installing the python module

## Mac Setup

### Setup git

```
git config --global init.defaultBranch main
git config --global core.editor vim
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

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
pip install virtualenv
pip install pylint
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

* Run `:PluginInstall` against .vimrc. When you open the .vimrc you will get a bunch of errors just press `q	` over and over untill they go away then press <esc> and type `:PluginInstall`

* coc might fail to install correctly. If that happens do the following

```
cd ~/.vim/bundle/coc.nvim
npm install
yarn install
```

* Read about navigating NerdTree here [https://catonmat.net/vim-plugins-nerdtree-vim](https://catonmat.net/vim-plugins-nerdtree-vim)

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

### Application Setup

* Setup virtualenv and install app dependencies

```
git clone git@github.com:briataws/aws-hello-world.git
cd aws-hello-world
virtualenv venv --system-site-packages
source venv/bin/activate
pip install -r hello_world/requirements.txt
```

* Verify tox is working

```
tox
```

The following files should get created and `tox` should exit with a 0 return code

```
test-reports/unit-test.xml
coverage.xml
```

Output should finish with

```
unit: commands succeeded
pylint: commands succeeded
congratulations :)
```

* Build the container 

```
docker built -t aws-hello-world . 
```

* Run the container

```
docker run -p 8080:8080 aws-hello-world
```

* Manually verify the container works

```
curl http://localhost:8080
```

Should return

```
{"text":{"What":null,"When":null,"Who":null}}
```

* Run behavior/functional tests against running container

```
SERVER_HOST=http://localhost:8080
tox -e behave
```

Successful output should be

```
behave: commands succeeded
congratulations :)
```


## Author
Brian Carpio

[briataws@amazon.com](mailto:briataws@amazon.com)

