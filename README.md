# HuggingFace-based Stable Diffusion Generator

- Generates a single stable diffusion image with an input prompt.
- Requires a HuggingFace account and a token.

Sample generated with v1.3 with minor edits on Photoshop and background extended with DALL-E:
![generation](https://user-images.githubusercontent.com/35907066/186797212-54ee322c-154e-4bf5-bc49-09f21893da16.png)

### Requirements

1. `python` 3.9+
2. [HuggingFace](https://huggingface.co/) account

### How to run

1. Install the requirements

```
pip install -r requirements.txt
```

2. Accept the agreement in the [Stable Diffusion v1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) model repo to gain access to the model.
   <img width="761" alt="agreement" src="https://user-images.githubusercontent.com/35907066/186797231-5c907fe4-3c9b-490f-9485-b9c4f71ad0ea.png">

3. Create and retrieve a `READ` token from [HuggingFace Settings](https://huggingface.co/settings/tokens)
   <img width="739" alt="token" src="https://user-images.githubusercontent.com/35907066/186797252-a028f8e6-fbae-41d8-bfb0-8e1553adb305.png">

4. Login with your token in the command below

```
huggingface-cli login
```

5. You can now start generating with:

```
python generate.py <prompt>
```

ex. - `python generate.py "astronaut floating in space while spaceship drifts away"`
