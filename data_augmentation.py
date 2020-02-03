from keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img

messi_images = 200 #Nnumber of messi images in the dataset, chnage accordingly
ronaldo_images = 200 #Nnumber of roanldo images in the dataset, chnage accordingly
path = 'dataset/train'

datagen = ImageDataGenerator(
			
			rotation_range = 40,
			width_shift_range = 0.2,
			height_shift_range = 0.2,
			shear_range = 0.2,
			zoom_range = 0.2,
			horizontal_flip = True,
			fill_mode = 'nearest')

for i in range(ronaldo_images):

	j = i+1
	img = load_img(path+'/ronaldo/ronaldo_'+str(j)+'.jpeg')
	x = img_to_array(img)
	x = x.reshape((1,)+x.shape)

	k = 0
	for batch in datagen.flow(x, batch_size = 1, save_to_dir = path+'/ronaldo', save_prefix = 'ronaldo_', save_format = 'jpeg'):
		k+=1
		if k>20:
			break


for i in range(messi_images):
	j = i+1
	img = load_img(path+'/messi/messi_'+str(j)+'.jpeg')
	x = img_to_array(img)
	x = x.reshape((1,)+x.shape)

	k = 0
	for batch in datagen.flow(x, batch_size = 1, save_to_dir = path+'/messi', save_prefix = 'messi*', save_format = 'jpeg'):
		k+=1
		if k>20:
			break