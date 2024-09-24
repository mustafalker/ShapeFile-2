import geopandas as gpd

shapefile_path = 'C:\\Users\\ulker\\Desktop\\Mustafa ÜLKER\\Ölçümler\\2022\\FABRIKA_KODU=7_and_DONEM=2022_part1\\FABRIKA_KODU=7_and_DONEM=2022_part1.shp'
gdf = gpd.read_file(shapefile_path)

for column in gdf.select_dtypes(include=['object']).columns:
    gdf[column] = gdf[column].apply(lambda x: x.encode('latin1').decode('utf-8') if isinstance(x, str) else x)

half_size = len(gdf) // 2
gdf1 = gdf.iloc[:half_size]  
gdf2 = gdf.iloc[half_size:]  

output_path1 = 'C:\\Users\\ulker\\Desktop\\Mustafa ÜLKER\\Ölçümler\\2022\\FABRIKA_KODU=7_and_DONEM=2022_part1.1\\shapefile_part1.shp'
output_path2 = 'C:\\Users\\ulker\\Desktop\\Mustafa ÜLKER\\Ölçümler\\2022\\FABRIKA_KODU=7_and_DONEM=2022_part1.2\\shapefile_part2.shp'

gdf1.to_file(output_path1, encoding='utf-8')
gdf2.to_file(output_path2, encoding='utf-8')
