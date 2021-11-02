import shapefile 
w = shapefile.Writer("GSIsoal3/nO3soal3")
w.shapeType

w.field('Kolom 1', 'C')
w.field('Kolom 2', 'C')

w.record('ngek', 'satu')
w.record('ngok', 'dua')

w.point(1,1)
w.point(2,2)

w.close()