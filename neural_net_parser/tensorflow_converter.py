import keras.models
import example_nets.tensorflow.AlexNet as AlexNet
import os.path
import json
#method used for testing
def keras_to_json(model):
	model_json_string = model.to_json()
	return json.loads(model_json_string)

#json will be generated from ui
def json_to_keras(json_config):
	return keras.models.model_from_json(json_config)

#hdf5 contains architecture, weight values, compile() info
#TODO: this is not production method, this file should be pushed to s3
def keras_to_hdf5(model, name_to_save):
	file_path = "./" + name_to_save + ".h5"
	model.save(name_to_save + ".h5")
	assert os.path.isfile(file_path)

def json_to_hdf5(json_config, name_to_save):
	model = json_to_keras(json_config)
	keras_to_hdf5(json_to_keras, name_to_save)
	assert os.path.isfile(file_path)

def hdf5_to_keras(hdf5_path):
	assert hdf5_path[-3:] == ".h5"
	reconstructed_model = keras.models.load_model(hdf5_path)
	return reconstructed_model

def assert_AlexNet_json():
	expected_json = {'class_name': 'Sequential', 
					 'config': {'name': 'sequential', 
					 'layers': [{'class_name': 'InputLayer', 'config': {'batch_input_shape': [None, 224, 224, 3], 'dtype': 'float32', 'sparse': False, 'ragged': False, 'name': 'conv2d_input'}}, 
					 			{'class_name': 'Conv2D', 'config': {'name': 'conv2d', 'trainable': True, 'batch_input_shape': [None, 224, 224, 3], 'dtype': 'float32', 'filters': 96, 'kernel_size': [11, 11], 'strides': [4, 4], 'padding': 'valid', 'data_format': 'channels_last', 'dilation_rate': [1, 1], 'groups': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, 
					 			{'class_name': 'MaxPooling2D', 'config': {'name': 'max_pooling2d', 'trainable': True, 'dtype': 'float32', 'pool_size': [2, 2], 'padding': 'valid', 'strides': [2, 2], 'data_format': 'channels_last'}}, 
					 			{'class_name': 'Conv2D', 'config': {'name': 'conv2d_1', 'trainable': True, 'dtype': 'float32', 'filters': 256, 'kernel_size': [11, 11], 'strides': [1, 1], 'padding': 'valid', 'data_format': 'channels_last', 'dilation_rate': [1, 1], 'groups': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_1', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, 
					 			{'class_name': 'MaxPooling2D', 'config': {'name': 'max_pooling2d_1', 'trainable': True, 'dtype': 'float32', 'pool_size': [2, 2], 'padding': 'valid', 'strides': [2, 2], 'data_format': 'channels_last'}}, 
					 			{'class_name': 'Conv2D', 'config': {'name': 'conv2d_2', 'trainable': True, 'dtype': 'float32', 'filters': 384, 'kernel_size': [3, 3], 'strides': [1, 1], 'padding': 'valid', 'data_format': 'channels_last', 'dilation_rate': [1, 1], 'groups': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_2', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, 
					 			{'class_name': 'Conv2D', 'config': {'name': 'conv2d_3', 'trainable': True, 'dtype': 'float32', 'filters': 384, 'kernel_size': [3, 3], 'strides': [1, 1], 'padding': 'valid', 'data_format': 'channels_last', 'dilation_rate': [1, 1], 'groups': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_3', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, {'class_name': 'Conv2D', 'config': {'name': 'conv2d_4', 'trainable': True, 'dtype': 'float32', 'filters': 256, 'kernel_size': [3, 3], 'strides': [1, 1], 'padding': 'valid', 'data_format': 'channels_last', 'dilation_rate': [1, 1], 'groups': 1, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_4', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, {'class_name': 'MaxPooling2D', 'config': {'name': 'max_pooling2d_2', 'trainable': True, 'dtype': 'float32', 'pool_size': [2, 2], 'padding': 'valid', 'strides': [2, 2], 'data_format': 'channels_last'}}, {'class_name': 'Flatten', 'config': {'name': 'flatten', 'trainable': True, 'dtype': 'float32', 'data_format': 'channels_last'}}, 
					 			{'class_name': 'Dense', 'config': {'name': 'dense', 'trainable': True, 'batch_input_shape': [None, 150528], 'dtype': 'float32', 'units': 4096, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_5', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, {'class_name': 'Dropout', 'config': {'name': 'dropout', 'trainable': True, 'dtype': 'float32', 'rate': 0.4, 'noise_shape': None, 'seed': None}}, 
					 			{'class_name': 'Dense', 'config': {'name': 'dense_1', 'trainable': True, 'dtype': 'float32', 'units': 4096, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_6', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, 
					 			{'class_name': 'Dropout', 'config': {'name': 'dropout_1', 'trainable': True, 'dtype': 'float32', 'rate': 0.4, 'noise_shape': None, 'seed': None}}, {'class_name': 'Dense', 'config': {'name': 'dense_2', 'trainable': True, 'dtype': 'float32', 'units': 1000, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_7', 'trainable': True, 'dtype': 'float32', 'activation': 'relu'}}, 
					 			{'class_name': 'Dropout', 'config': {'name': 'dropout_2', 'trainable': True, 'dtype': 'float32', 'rate': 0.4, 'noise_shape': None, 'seed': None}}, 
					 			{'class_name': 'Dense', 'config': {'name': 'dense_3', 'trainable': True, 'dtype': 'float32', 'units': 17, 'activation': 'linear', 'use_bias': True, 'kernel_initializer': {'class_name': 'GlorotUniform', 'config': {'seed': None}}, 'bias_initializer': {'class_name': 'Zeros', 'config': {}}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}}, 
					 			{'class_name': 'Activation', 'config': {'name': 'activation_8', 'trainable': True, 'dtype': 'float32', 'activation': 'softmax'}}]}, 
					 			'keras_version': '2.4.0', 'backend': 'tensorflow'}

	alex_net_json = keras_to_json(AlexNet.AlexNet())
	print(alex_net_json)
	print(expected_json)
	#seems like this test fails because the numbering gets changed for each layer(i.e. conv2d_*_input)
	assert alex_net_json == expected_json