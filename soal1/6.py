import shapefile
f = shapefile.Writer('shapefile6/soal6/soal6')
f.shapeType

f.field('Kolom 1', 'C')
f.field('Kolom 2', 'C')

f.record('ngek', 'satu')

f.poly([[[1,3],[5,3]]])

f.close()