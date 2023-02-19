from typing import Optional, Any

from pydantic import BaseModel
from backend.stablediffusion.samplers import Sampler


class StableDiffusionSetting(BaseModel):
    prompt: str
    negative_prompt: Optional[str]
    image_height: Optional[int] = 512
    image_width: Optional[int] = 512
    inference_steps: Optional[int] = 20
    guidance_scale: Optional[float] = 7.5
    number_of_images: Optional[int] = 1
    scheduler: Optional[str] = Sampler.DPMSolverMultistepScheduler.value
    seed: Optional[int] = -1
    attention_slicing: Optional[bool] = True
    vae_slicing: Optional[bool] = True


class StableDiffusionImageToImageSetting(StableDiffusionSetting):
    image: Any
    strength: Optional[float] = 0.75


class StableDiffusionImageInpaintingSetting(StableDiffusionSetting):
    image: Any
    mask_image: Any


class StableDiffusionImageDepthToImageSetting(StableDiffusionSetting):
    image: Any
    depth_image: Optional[Any]
    strength: Optional[float] = 0.8
