# HuggingFace-based Stable Diffusion Generator

Generates a single stable diffusion image with an input prompt.
Requires a HuggingFace account and a token.

### Requirements

1. `python` 3.9+
2. [HuggingFace](https://huggingface.co/) account

### How to run

1. Install the requirements

```
pip install -r requirements.txt
```

2. Accept the agreement in the [Stable Diffusion v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) model repo to gain access to the model.

3. Create and retrieve a `READ` token from [HuggingFace Settings](https://huggingface.co/settings/tokens)

4. Login with your token in the command below

```
huggingface-cli login
```

5. You can now start generating with:

```
python generate.py <prompt>
```

ex. - `python generate.py "astronaut floating in space while spaceship drifts away"`
