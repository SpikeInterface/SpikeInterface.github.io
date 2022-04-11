.. title: Welcome to SpikeInterface Reports
.. slug: index
.. date: 2020-01-06 11:37:28 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


.. image:: /images/logo.png
   :height: 200 pt
   :align: center

Introduction
============

**SpikeInterface Reports** is a collection of notebooks to:

* demonstrate what can be done with `SpikeInterface <https://github.com/SpikeInterface>`_.
* show detailed benchmarks for spike sorters.
* push code that generated figures on papers related to spikeinterface (spikeinterface, probeinterface, collision)
* serve as a sandbox for future benchmarks that can be integrated in the `SpikeForest <https://spikeforest.flatironinstitute.org/>`_ website.
* demonstrate sortingcomponents_examples
* test out other ideas!


Notebooks reproducing the figures in `collision preprint <https://www.biorxiv.org/content/10.1101/2021.11.29.470450v1>`_
========================================================================================================================

.. post-list::
   :tags: collision_paper_2021


Notebooks reproducing the figures in `probeinterface preprint <https://osf.io/jr3w5/>`_
=======================================================================================

.. post-list::
   :tags: pi_paper_2021


Notebooks reproducing the figures in the `elife paper 2020 <https://elifesciences.org/articles/61834>`_
=======================================================================================================

.. post-list::
   :tags: paper


Notebooks examples for sorting components
=========================================

.. post-list::
   :tags: sortingcomponents_examples   

   
Notebooks with NEW API
======================

.. post-list::
   :tags: new_api

All notebooks
=============

.. post-list::
   :stop: 10


  
Other ideas we want to test here:
=================================

* compute agreement across sorters for dataset without ground truth
* make benchmarks for sorters that separate:

    * the accuracy per GT units
    * how many units are detected (true and false positives)

Often benchmarks report an average of accuracy that mixes different metrics.
A sorter with high accuracy that does not detect all neurons may have a lower average accuracy than one detecting more
neurons with less precision.

Furthermore, we plan to add benchmarks on specific aspects of extracellular recordings:

* benchmarks specifically for spike collisions
* benchmarks for probe drift
* benchmarks investigating if high-density probes yield better results than lower-density probes
* example for parameters optimisations
* further testing of the "ensemble sorting" method

