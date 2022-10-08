# make sure you're logged in with `huggingface-cli login`
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("mps")

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
image = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
image = pipe(prompt, num_inference_steps=20)["sample"][0]
image.save("mps_device_test_output.png")
