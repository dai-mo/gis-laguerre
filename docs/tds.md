# Data Preparation for Geospatial Analysis & ML with Laguerre-Voronoi in Python

In this article the application of Laguerre-Vornoi tessellation to Demographic and Health Survey (DHS) data is explored. 
A pipeline for cleaning and transforming the DHS data is proposed along with the associated python code.

## Demographic and Health Survey data
DHS surveys contain confidential information that could potentially be used to identify an individual through unique information. To avoid this the [DHS Program](https://dhsprogram.com/) has developed an approach to degrade accuracy of the GPS coordinates so that true place of residence cannot be derived. In all DHS surveys the center GPS coordinate of the populated place in a cluster is recorded and separate degradation error values are applied depending on whether a cluster is _urban_ or _rural_. A random error of 5 km maximum in rural areas and 2 km maximum in urban areas is applied, this decreases the likelihood of household identification by tenfold. The new list of coordinates can be thought of as having a circular error buffer zone of (5km or 2km) within which actual value resides. This degradation poses a challenge for further data analysis and machine learning tasks on this data.

## Laguerre Voronoi Diagrams
Introduced in 1985 in <a href="#ref1">[1]</a>, Laguerre Voronoi diagrams are an extension of the concept of Voronoi diagrams for $n$ points in the plane to that of Laguerre geometry for $n$ circles in the plane. It is a partition of the Euclidean plane into polygonal cells defined from a set of circles and are also known as [Power Diagrams](https://en.wikipedia.org/wiki/Power_diagram). The diagrams used in this article were generated from the [GitHub Gist](https://gist.github.com/sunayana/a3a564058e97752f726ca65d56fab529)
![image.png](../images/laguerre-voronoi-example.png)

## Laguerre Voronoi Tessellation of DHS Data
Due to the nature of the degradation introduced in the DHS Data, Laguerre Voronoi tessellation of the DHS dataset is a viable model to create polygonal partition of the map of a country for further data analysis. India is taken as an example for introducing the pipeline.
### Preprocessing DHS Data
Note that the intersection of 0 degrees latitude (Equator) and 0 degrees longitude(Prime Meridian) on the map falls in the middle of the 
Atlantic Ocean, in the Gulf of Guinea off the coast of western Africa.
![image.png](../images/0N0E.png)
<figcaption>
The image is from <a href="#ref3">[3]</a>.
</figcaption>
Hence all entries from any country specific DHS GeoDataFrame could be dropped which has both latitude and longitude entries are 0.0.

## Acknowledgements
## References
<ol>
    <li is="ref1">Imai, H., Iri, M. & Murota, K.(1985). Voronoi Diagram in the Laguerre Geometry and Its Applications, SIAM Journal of Computing, 14(1), 93--105. doi:10.1137/0214006</li>
    <li is="ref2"> Guidelines On The Use of DHS GPS Data https://dhsprogram.com/pubs/pdf/SAR8/SAR8.pdf</li>
    <li is="ref3"> What is at Zero Degrees Latitude and Zero Degrees Longitude? https://www.geographyrealm.com/zero-degrees-latitude-and-zero-degrees-longitude/</li>
    
</ol>