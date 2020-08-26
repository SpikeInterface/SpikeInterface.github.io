This repo contain sources for auto generated blog with nikola
of spikeinterace example https://spikeinterface.github.io



## Note to add a new post


The **master branch** contain the html stuff for the blog : **Never edit the master branch**

We have to edit the **scr branch** 

The first time:
  * pip install nikola
  * git clone git@github.com:SpikeInterface/SpikeInterface.github.io.git
  * cd SpikeInterface.github.io
  * git checkout src   # **very very very important**
  
Every new post:
  * git checkout src   # **very very very important**
  * git pull origin src
  * nikola new_post -f ipynb  #  this is create a notebook inside a folder becarefull to choice a very explicit title
  * edit the notebook
  * nikola serve -b ## this check locally the blog
  * then 2 options:
    * push to src branch with : git push origin src (no puplication)
    * publish and push (to master under the hood) : nikola github_deploy


More details here : https://getnikola.com/handbook.html
