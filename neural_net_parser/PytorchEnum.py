import enum
#Use enum class to list constants
#Only use Sequential container
#Convolution Layers
class PytorchConvolutionLayers(enum.Enum):
	Conv1d = 1
	Conv2d = 2
	Conv3d = 3
	ConvTransponse1d = 4
	ConvTranspose2d = 5
	ConvTranspose3d = 6
	Unfold = 7
	Fold = 8

#Pooling Layers
class PytorchPoolingLayers(enum.Enum):
	MaxPool1d = 1
	MaxPool2d = 2
	MaxPool3d = 3
	MaxUnpool1d = 4
	MaxUnpool2d = 5
	MaxUnpool3d = 6
	AvgPool1d = 7
	AvgPool3d = 8
	FractionalMaxPool2d = 9
	LPPool1d = 10
	LPPool2d = 11
	AdaptiveMaxPool1d = 12
	AdaptiveMaxPool2d = 13
	AdaptiveMaxPool3d = 14
	AdaptiveAvgPool1d = 15
	AdaptiveAvgPool2d = 16
	AdaptiveAvgPool3d = 17

#Padding Layers
class PytorchPaddingLayers(enum.Enum):
	ReflectionPad1d = 1
	ReflectionPad2d = 2
	ReplicationPad1d = 3
	ReplicationPad3d = 4
	ZeroPad2d = 5
	ConstantPad1d = 6
	ConstantPad2d = 7
	ConstantPad3d = 8

class PytorchNonlinearActivations(enum.Enum):
	ELU = 1
	Hardshrink = 2
	Hardsigmoid = 3
	Hardtanh = 4
	Hardswish = 5
	LeakyReLU = 6
	LogSigmoid = 7
	MultiheadAttention = 8
	PReLU = 9
	ReLU = 10
	ReLU6 = 11
	SELU = 12
	CELU = 13
	GELU = 14
	Sigmoid = 15
	Softplus = 16
	Softshrink = 17
	Softsign = 18
	Tanh = 19
	Tanhshrink = 20
	Threshold = 21
	#other types of activations
	Softmin = 22
	Softmax = 23
	Softmax2d = 24
	LogSoftmax = 25
	AdaptiveLogSoftmaxWithLoss = 26

class PytorchNormalizationLayers(enum.Enum):
	BatchNorm1d = 1
	BatchNorm2d = 2
	BatchNorm3d = 3
	GroupNorm = 4
	SyncBatchNorm = 5
	InstanceNorm1d = 6
	InstanceNorm2d = 7
	InstanceNorm3d = 8
	LayerNorm = 9
	LocalResponseNorm = 10

class PytorchRecurrentLayers(enum.Enum):
	RNNBase = 1
	RNN = 2
	LSTM = 3
	GRU = 4
	RNNCell = 5
	LSTMCell = 6
	GRUCell = 7

class PytorchTransformerLayers(enum.Enum):
	Transformer = 1
	TransformerEncoder = 2
	TransformerDecoder = 3
	TransformerEncoderLayer = 4
	TransformerDecoderLayer = 5

class PytorchLinearLayers(enum.Enum):
	Identity = 1
	Linear = 2
	Bilinear = 3

class PytorchDropoutLayers(enum.Enum):
	Dropout = 1
	Dropout2d = 2
	Dropout3d = 3
	AlphaDropout = 4

class PytorchSparseLayers(enum.Enum):
	Embedding = 1
	EmbeddingBag = 2

##################TODO, do the rest from DistanceFunctions
