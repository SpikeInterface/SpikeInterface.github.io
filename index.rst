.. title: Welcome to spikeinterface report
.. slug: index
.. date: 2020-01-06 11:37:28 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


.. image:: /images/logo.png
   :height: 200 pt

**spikeinterface report** is a collection of notebooks that :

  * demonstrate what can be done with the spikeinterface tool
  * show detailed benchmarks for spike sorter
  * serve as a sandbox for future benchmark that can be integrated in spikeforest
  * test some idea

Some ideas we want to test here:

  * compute agreement accross sorter for none groundth truth dataset
  * make benchmark for sorters that separate:
  
     * the accuracy per GT units
     * how many units are detected
    
    Actual benchmarks make an average of accuracy that mix theses metrics
    so a sorter with high accuracy but that do not detect a cell will have a low
    average accuracy.
    
  * make benchmark for spike collision
  * make benchmark for drift
  * make benchmark if high density make better results than lower density
  * example for parameters optimisations
  * test if "agreement sorting" is relevant
  


  
