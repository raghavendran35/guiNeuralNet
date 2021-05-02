"""
Pytorch-to-JSON, JSON-to-Pytorch converter
"""
import onnx
import json
from google.protobuf.json_format import MessageToJson, Parse

from torch.autograd import Variable

########Helpful: https://stackoverflow.com/questions/42703500/best-way-to-save-a-trained-model-in-pytorch
#We will save model state_dict, because only layers with learnable parameters
#exist in state_dict. Non-learnable stuff in optimizer. Need to check about
#edge case layers

"""
Seems like we have to do pytorch->onnx->json
And also json->onnx->pytorch
"""

######should trigger service call to DDB, S3
def save_pytorch_optimizer(path_to_save_at, optimizer):
	torch.save(optimizer.state_dict(), path_to_save_at)

######should trigger service call to DDB, S3
def save_pytorch_model_params(path_to_save_at, model):
	torch.save(model.state_dict(), path_to_save_at)

def convert_pytorch_to_onnx(pytorch_weights_path, model_type, example_input):
	"""
	path_save_to_at:
	model_type: The class corresponding to the NeuralNet
	"""
	#model class instance
	trained_model = model_type()

	#load weights from file
	state_dict = torch.load(pytorch_weights_path)

	#load weights into model net architecture defined by class
	trained_model.load_state_dict(torch.load(pytorch_model_path))

	#export trained model to ONNX
	torch.onnx.export(trained_model, )







"""
Convert onnx model to JSON
"""
def convert_onnx_to_json(onnx_model_path):
	onnx_model = onnx.load(onnx_model_path)
	s = MessageToJson(onnx_model)
	onnx_json = json.loads(s)
	return onnx_json


"""
Convert JSON to String
"""
def convert_json_to_string(json_to_convert):
	onnx_str = json.dumps(json_to_convert)
	