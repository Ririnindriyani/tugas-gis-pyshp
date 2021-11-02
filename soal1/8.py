import shapefile
h = shapefile.Writer('shapefile8/soal8/soal8')
h.shapeType

h.field('Kolom 1', 'C')
h.field('Kolom 2', 'C')

h.record('ngek', 'satu')

h.poly([
    [[1,3],[5,3],[1,2],[5,2], [1,3]]
    ])

h.close()