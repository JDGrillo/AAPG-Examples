# https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
import os
import glob
import pandas as pd
# specify the directory where the files exist
os.chdir("data-files")

# specify which kinds of files we're looking to combine
extension = "csv"

# extract all of the file names which meet our previous specifications, all csv files in the directory we've chosen
# this is using something call list comprehension to create a list of all the file names we'll be using
# https://www.programiz.com/python-programming/list-comprehension
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

# combine all files into a single pandas dataframe using concat
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

combined_csv.to_csv( "../combined-files/combined-csv.csv", index=False, encoding='utf-8-sig')