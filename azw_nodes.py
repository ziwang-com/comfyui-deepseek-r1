# -*- coding: utf-8 -*- 
#
#from .zw_def  import *
from .zw_tool  import *
#from .zw_srt  import *
#
#from icecream import ic as cpp
#cpp=print
#
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
from folder_paths import models_dir
from comfy import model_management, model_patcher

#

#------------------
#
deep_model_folder_path = Path(models_dir) / 'deepseek'
deep_model_folder_path.mkdir(parents=True, exist_ok=True)
#
#-------------
#
class DeepModel:
    def __init__(self, model, patcher, tokenizer=None, processor=None):
        self.model = model
        self.tokenizer = tokenizer
        self.processor = processor
        self.patcher = patcher
        
        # hook modelClass.device setter
        def set_value(self, new_value):
            pass
        model.__class__.device = property(fget=model.__class__.device.fget, fset=set_value)
        


class DeepLoader:
    @classmethod
    def INPUT_TYPES(cls):
        model_lst = []
        for folder in deep_model_folder_path.iterdir():
            if folder.is_dir():
                config_file = folder / 'config.json'
                if config_file.is_file():
                    relative_path = str(folder.relative_to(deep_model_folder_path))
                    model_lst.append(relative_path)
        return {
            "required": {
                "model_name": (model_lst, {}),
            }
        }
        
    RETURN_TYPES = ("DEEP_MODEL", )
    RETURN_NAMES = ("model", )
    FUNCTION = "load_model"
    CATEGORY = "ComfyUI-DeepSeek-R1"

    def load_model(self, model_name):
        offload_device = torch.device('cpu')
        #offload_device = torch.device('cuda')
        load_device = model_management.get_torch_device()
        model = AutoModelForCausalLM.from_pretrained(
            deep_model_folder_path / model_name, 
            device_map=offload_device, 
            torch_dtype="auto", 
        )
        tokenizer = AutoTokenizer.from_pretrained(deep_model_folder_path / model_name)
        patcher = model_patcher.ModelPatcher(model, load_device=load_device, offload_device=offload_device)
        #patcher = model_patcher.ModelPatcher(model, load_device=load_device offload_device=NoneNone) #, offload_device=offload_device)
        
        return (DeepModel(model, patcher, tokenizer=tokenizer), )

class DeepGen:

    @classmethod
    def INPUT_TYPES(cls):
        DEFAULT_INSTRUCT = ''
        return {
            "required": {
                "deep_model": ("DEEP_MODEL",),
                #"prompt": ("STRING", {"defaultInput": True,}),
                #
                #"system_instruction": ("STRING", {"default": DEFAULT_INSTRUCT, "multiline": True}),
                "user_prompt": ("STRING", {"default": "", "multiline": True}),
                "seed": ("INT", {"default": 888, "min": 0, "max": 0xffffffffffffffff}),
                "max_tokens": ("INT", {"default": 500, "min": 0, "max": 0xffffffffffffffff}),
                "temperature": ("FLOAT", {"default": 1, "min": 0, "max": 2}),
                "top_k": ("INT", {"default": 50, "min": 0, "max": 101}),
                "top_p": ("FLOAT", {"default": 1, "min": 0, "max": 1}),
            },
       
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "deep_xgen"
    CATEGORY = "ComfyUI-DeepSeek-R1"


    def deep_xgen(self, deep_model,  user_prompt, seed=0, temperature=1.0, max_tokens=500, top_k=50, top_p=1.0, **kwargs):
        set_seed(seed % 9999999)
        system_instruction=''
        messages = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt.format(**kwargs)},
            #{"role": "user", "content": user_prompt},
        ]
        tokenizer = deep_model.tokenizer
        model = deep_model.model
        patcher = deep_model.patcher
        model_management.load_model_gpu(patcher)
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return (response, )

#    
#----------------
#
NODE_CLASS_MAPPINGS = {
    #
    'deep_load': DeepLoader,
    'deep_gen': DeepGen,
    #
    
}


#----------
#
