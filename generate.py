import sys
import logging
import torch

from diffusers import StableDiffusionPipeline, DDIMScheduler

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_single(prompt: str):
    # This will substitute the default PNDM scheduler for DDIM
    # see the experiment here for a visualization with different schedulers
    # https://www.reddit.com/r/StableDiffusion/comments/wwm2at/sampler_vs_steps_comparison_low_to_mid_step_counts
    scheduler = DDIMScheduler(
        beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear"
    )

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        scheduler=scheduler,
        num_inference_steps=16,
        use_auth_token=True,
    ).to(DEVICE)

    with torch.autocast(DEVICE):
        image = pipe(prompt)["sample"][0]

    export_filename = f"{prompt}.png"
    image.save(export_filename)

    logger.info(f"Saved to {export_filename}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] is None:
        logger.error(
            'Please pass a prompt. ex. - python run.py "astronaut floating while spaceship drifts away"'
        )

    prompt = sys.argv[1]
    generate_single(prompt=prompt)
