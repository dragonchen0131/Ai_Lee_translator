# Ai_Lee_translator
**An ancient/modern chinese translator with a unique voice**
By using transformer and voice model to train a unique voice to speak ancient chinese

## Translator Part
 This model runs in 
 python 3.10
 torch == 1.9
 
 **If you want to run the preprocessing part**
 This project runs in 
 python 3.10
 Pytorch == 1.9
 Flask == 2.0.0
 jieba == 0.42.1
 pytorch_lightning == 1.9 
 kenlm
## Voice model part
 This project runs in 
 python 3.10
### Do these things below before you run this code:
run these bash codes in your cmd

```bash
#change direct to ur folder
cd ~/yourProjectFolder

# Clone GPT_Sovits repo
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

#install needed toolkits
pip install -r requirements.txt

# activate API
python api_v2.py --tts_config config.py --bind_addr 127.0.0.1 --port 9880
```

