from dataclasses import dataclass, field
from typing import List
from custom_types import DetectionSamplingMethod, SampleFrom, MultipleAnimalReduction, RegressionMethod, DepthEstimationModel


@dataclass
class Config:
    # general parameters
    data_dir: str = ""  # where the data is stored
    min_depth: float = 1.  # minimum sampled distance
    max_depth: float = 20.  # maximum sampled distance

    # file extension parameters
    depth_image_extensions: List[str] = field(default_factory=lambda: [".exr"])
    intensity_image_extensions: List[str] = field(default_factory=lambda: [".png", ".PNG", ".jpg", ".jpeg", ".JPG", ".JPEG"])

    # detection parameters
    bbox_confidence_threshold: float = 0.4  # minimal confidence of detections
    # detect_humans: bool = False  # whether to detect humans and include their distance estimations in the output

    # depth estimation parameters
    depth_estimation_model: DepthEstimationModel = DepthEstimationModel.UniDepthv2  # one of DPT|DEPTH_ANYTHING

    # visualization parameters
    make_figures: bool = True  # save figures in results directory

    # calibration parameters
    # calibrate_metric: bool = False  # whether to calibrate in metric or in disparity space
    calibration_regression_method: RegressionMethod = RegressionMethod.PieceWise  # one of RANSAC|LEASTSQUARES|POLY|RANSAC_POLY
    # calibration_mask_animals: bool = False  # whether to mask animals during calibration


    # sampling_parameters
    detection_sampling_method: DetectionSamplingMethod = DetectionSamplingMethod.BBOX_PERCENTILE  # one of BBOX_BOTTOM|BBOX_PERCENTILE|SAM
    # multiple_animal_reduction: MultipleAnimalReduction = MultipleAnimalReduction.NONE  # one of NONE|MEDIAN|ONLY_CENTERMOST|
    # sample_from: SampleFrom = SampleFrom.DETECTION  # one of REFERENCE|DETECTION
    bbox_sampling_percentile: int = 20  # percentile of depth values sampled from detected bounding boxes. Only used
    # if detection_sampling_method is equal to DetectionSamplingMethod.BBOX_PERCENTILE.

    # extras
    detect_heights: bool = False
