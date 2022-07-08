from os.path import join

datapath = '/MRI_DATA/more_project/raw_data'
subj_id = '210145'
subjs = ['23223','342423', '1234123']
ses = '1'
task = 'movie'
img_names = ['image1.jpg', 'image2.jpg', 'cocaine1.jpg', 'cocaine2.jpg', 'heroin1.jpg']
response_file = '_'.join([task, 'responses.csv'])
response_filepath = datapath + join(subj_id, ses, task, response_file)

for img_name in img_names:
    img_path = '/MRI_DATA/more_project/raw_data/' + subj_id + '/' + ses + '/' + task + '/' + img_name

img_paths = map(lambda x: join(datapath, x, ses, task, y), subjs, img_names)
print(list(img_paths))