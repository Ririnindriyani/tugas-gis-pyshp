import shapefile
g = shapefile.Writer('shapefile7/soal7/soal7', shapefile.POLYLINE)
g.shapeType

g.field('Kolom 1', 'C')
g.field('Kolom 2', 'C')

g.record('ngek', 'satu')

g.line([[[1,3],[5,3],[1,2],[5,2]]])

g.close()