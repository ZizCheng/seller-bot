import mapper

# specify the filepath of the Excel document
filepath = 'sample.xlsx'

# create map to understand Excel sheet
m = mapper.make_map(filepath)

print(m)
