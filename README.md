Following https://www.youtube.com/watch?v=ltLNYA3lWAQ

Setup virtual env
```
python3 -m venv venv
```

Activate
```
source venv/bin/activate
```

>> MPS only
>> Install pytorch preview
>> ```
>> pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
>> ```

Install other requirements
```
pip install -r requirements.txt
```

Login to Hugging Face
```
$ huggingface-cli login
```


