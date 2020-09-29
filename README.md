This repo contains source codes for the [SpikeInterface Reports](https://spikeinterface.github.io) page. 
The blog is auto-generated blog with Nikola.



## Add a new post


The **master branch** contains the html pages for the blog: **Never edit the master branch**


In order to add a new post, you can edit the **scr branch**.

First, get Nikola:
  
`pip install nikola`
  
Next, clone this repo and checkout the **src** branch:
```
git clone git@github.com:SpikeInterface/SpikeInterface.github.io.git
cd SpikeInterface.github.io
git checkout src 
```
  
To create a new post:
  * `git checkout src`  
  * `git pull origin src`  (make sure you are in sync with the remote repo)
  * `nikola new_post -f ipynb`  (create a notebook called *new_post* inside a the posts folder)
  * Edit the *new_post* notebook
  * `nikola build` (build the blog locally)
  * `nikola serve -b`  (open the blog in the browser locally)
  * `git push origin src` (push your changes: not published yet!)
  * `nikola github_deploy` (publish and push your post)


More details on how to use Nikola can be found [https://getnikola.com/handbook.html](here).
