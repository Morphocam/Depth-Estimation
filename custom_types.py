from enum import Enum, auto


class DetectionSamplingMethod(Enum):
    BBOX_BOTTOM = auto()
    BBOX_PERCENTILE = auto()
    SAM = auto()


class SampleFrom(Enum):
    REFERENCE = auto()
    DETECTION = auto()


class MultipleAnimalReduction(Enum):
    NONE = auto()
    MEDIAN = auto()
    ONLY_CENTERMOST = auto()


class RegressionMethod(Enum):
    RANSAC = auto()
    PieceWise = auto()
    POLY = auto()
    RANSAC_POLY = auto()
    QUADRATIC = auto()
    LEASTSQUARES = auto()


class DepthEstimationModel(Enum):
    DPT = auto()
    DEPTH_AHYTHING_METRIC = auto()
    DepthPro = auto()
    METRIC_3D_V2_VIT_S = auto()
    DPT_PYTORCH = auto()
    UniDepthv2 = auto()