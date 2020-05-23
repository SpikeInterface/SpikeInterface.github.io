
* pip install nikola
* git clone git@github.com:SpikeInterface/SpikeInterface.github.io.git
* cd SpikeInterface.github.io
* git checkout src   # very very very important
* nikola new_post -f ipynb  #  this is create a notebook inside a folder becarefull to choice a very explicit title
* edit the notebook

Then 2 options:
  * push to src branch with : git push origin src
  * publish and push (to master under the hood) : nikola github_deploy 
