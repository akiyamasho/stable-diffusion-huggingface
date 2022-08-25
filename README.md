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

# Prompt Suffixes

You can use these prompt suffixes to generate decent-looking outputs.
### Places

Add your description of a place at the start of the prompt.

1. "`[description of place]`, tone mapped, shiny, intricate, cinematic lighting, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by terry moore and greg rutkowski and alphonse mucha" (thanks to @jquesnelle)

![old harbour, tone mapped, shiny, intricate, cinematic lighting, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by terry moore and greg rutkowski and alphonse mucha](https://user-images.githubusercontent.com/35907066/186828185-dd0d3a00-b787-4bf3-8222-eeb94baa53c4.png)

### Humans

Add your description of a human at the start of the prompt.

1. "`[description of human]` Clean Cel shaded vector art. Shutterstock. behance hd by lois van baarle, artgerm, Helen huang, by makoto shinkai and ilya kuvshinov, rossdraws, illustration" (credit: [The_Bravinator on Reddit](https://www.reddit.com/user/The_Bravinator/))
![anime girl wearing a kimono, Clean Cel shaded vector art  Shutterstock  behance hd by lois van baarle, artgerm, Helen huang, by makoto shinkai and ilya kuvshinov, rossdraws, illustration](https://user-images.githubusercontent.com/35907066/186828179-d267f0d5-0078-4d01-9c99-dec351bb2fa5.png)