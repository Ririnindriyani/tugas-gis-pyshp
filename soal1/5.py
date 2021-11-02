import shapefile
e = shapefile.Writer('shapefile/soal5/soal5')
e.shapeType

e.field('Kolom 1', 'C')
e.field('Kolom 2', 'C')

e.record('ngek', 'satu')

e.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]	])

e.close()