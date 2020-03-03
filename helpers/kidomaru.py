import pandas as pd
import json

EXCEL_FILE = 'Kidomaru Coloring.xlsx'
JSON_FILE = 'Colour.JSON'

def create_json(input_xlsx, output_json):

    colour_excel = pd.read_excel(input_xlsx,
                                 sheet_name = None, 
                                 header = None, 
                                 nrows = 78)
        
    colour_dict = {}
    for row_letter, row_colour_df in colour_excel.items():    
        # colour_list = [[row_number+1, colours.tolist()] for row_number, colours in row_colour_df.iterrows()]    
        colour_dict[row_letter] = dict([[row_number+1, colours.tolist()] for row_number, colours in row_colour_df.iterrows()])
        
    with open(output_json, 'w') as json_file:
        json.dump(colour_dict, json_file)
        

def read_colour(input_json, row_letter, column_number):
    
    with open(input_json, 'r') as json_file:
        return (json.load(json_file)[row_letter][column_number])
    
C = read_colour(JSON_FILE, 'C', '28')
print(C)
        
    