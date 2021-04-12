# GIS with Laguerre-Voronoi Diagrams

This project explores the different applications of Laguerre-Voronoi Diagrams to different geospatial datasets



## Features
The main features of this project include,
 *
 *

# Getting Started
The instructions here will get your development environment setup for this project.

## Prerequisites
To build this project you need,
 * To clone this [GitHub Gist](https://gist.github.com/sunayana/a3a564058e97752f726ca65d56fab529)
 * Then for Linux / MacOS environments set the `PYTHONPATH` to the directory of the Gist above.
 * If you do not have pipenv installed make sure to install it using the instructions found [here](https://pipenv-fork.readthedocs.io/en/latest/install.html)

## Installing
:warning: The project has to be forked to your own namespace before cloning.

Clone the project  

    $ git clone git@github.com:dai-mo/gis-laguerre.git
      
Change directory
      
    $ cd gis-laguerre

Create the `.env` file with the following entries
```
DHS_DATA_DIR = "<path_to_dhs_data>"
GADM_DATA_DIR = "<path_to_gadm_36_country_boundary_shapefile>"
OUT_DIR = "<path_to_output_directory>"
```

Set up the environment for the project   

    $ pipenv shell
    $ pipenv install
    
## Building     
Build artifact locally (in the _target_ directory)     

    $ ...

## Testing
Run tests
    $ ...
    
## Executing 
Run the program locally by executing,
    $ ...

## Code style check
...

## Publish
To make the artifact available for other dependent projects, install artifact locally.

    $ ...
    
Publish the artifact to a global artifact store.

    $ ...

## Deployment
This project can be deployed by ....

## Configuration / Environment
This project requires the following configuration / environment variables to run,
 *
 *

# Main Dependencies
The main dependencies of this project include,
 * 
 * 

# Versioning
We use [Semantic Versioning]. For the versions available, see the [tags on this repository].

# Support
Please open an issue for support.

# Releases
Releases for this repository are available [here](https://github.com/dai-mo/gis-laguerre/releases).

# Contributing
Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

# Authors
Please refer to the list of [contributors] who participated in this project.

# Acknowledgments
Thanks to,
*  the [Solve For Good](https://www.solveforgood.org/proj/47/) project: Creating a well-being data layer using machine learning, satellite imagery and ground-truth data.
*  [Gijs van den Dool](https://www.linkedin.com/in/gvddool/) for extensive discussions related to Voronoi Diagrams and their use in GIS which finally led to weighted Voronoi Diagrams being used for this project. 
*  [Kathleen Buckingham](https://www.wri.org/profile/kathleen-buckingham) & [Rong Fang](https://www.wri.org/profile/rong-fang) of the [World Resources Institute](https://www.wri.org/) 
*  [Carlos Mougan](https://cmougan.github.io/) of the Solve For Good Team.
*  GitHub Gist by Devert Alexandre on [Laguerre Vornoi Diagrams](https://gist.github.com/marmakoide/45d5389252683ae09c2df49d0548a627)


[Semantic Versioning]:http://semver.org/
[tags on this repository]:https://github.com/dai-mo/gis-laguerre/tags
[contributors]:https://github.com/dai-mo/gis-laguerre/graphs/contributors
[CONTRIBUTING.md]:CONTRIBUTING.md
[LICENSE.md]:LICENSE.md
