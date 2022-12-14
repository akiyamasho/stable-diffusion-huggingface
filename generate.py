import os
import sys
import logging
import torch

from diffusers import StableDiffusionPipeline

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EXPORT_FOLDER = "output"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_single(prompt: str):
    pipe = StableDiffusionPipeline.from_pretrained(  # type: ignore
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=True,
    ).to(DEVICE)

    if torch.cuda.is_available():
        with torch.autocast(DEVICE):  # type: ignore
            image = pipe(prompt)["sample"][0]
    else:
        image = pipe(prompt)["sample"][0]

    # Export
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)
    export_path = f"{prompt}.png"
    image.save(export_path)

    logger.info(f"Saved to {export_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] is None:
        logger.error(
            'Please pass a prompt. ex. - python run.py "astronaut floating while spaceship drifts away"'
        )

    prompt = sys.argv[1]
    generate_single(prompt=prompt)
