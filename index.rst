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

intro
=====

**spikeinterface report** is a collection of notebooks that

* demonstrate what can be done with [spikeinterface](https://github.com/SpikeInterface).
* show detailed benchmarks for spike sorters.
* serve as a sandbox for future benchmarks that can be integrated in the [spikeforest](https://spikeforest.flatironinstitute.org/) website.
* test out ideas...


All notebooks examples
======================

.. post-list::
   :stop: 10

Notebooks reproducing the figures in the `preprint on bioxiv <https://www.biorxiv.org/content/10.1101/796599v2>`_
================================================================================================================

.. post-list::
   :tags: paper


  
Some ideas we want to test here:
================================

* compute agreement accross sorters for dataset withoput ground truth
* make benchmarks for sorters that separate:

    * the accuracy per GT units
    * how many units are detected (true and false positives)

Often benchmarks report an average of accuracy that mix theses metrics
so a sorter with high accuracy but that does not detect all neurons may have a lower
average accuracy than one detecting more neurons with less precision.

* benchmarks specifically for spike collisions
* benchmarks for probe drift
* benchmarks investigating if high density probes yield better results than lower density probes
* example for parameters optimisations
* further testing of the "ensemble sorting" method



