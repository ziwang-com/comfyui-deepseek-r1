# comfyui-deepseek-r1
* comfyui-deepseek-r1 节点插件.Comfyui-deepseek-r1 Node Plugin
* 节点插件安装很简单，copy到comfyui的custom_nodes子目录下即可。
* The installation of the node plugin is very simple, just copy it to the custom_nodes subdirectories of comfyui.
* 

## ps,2025-1-28
* github搜了半天，好像是目前唯一支持comfyui本地化部署deepseek-r1的方案
* 官方没有提供，comfy主要aigc。其他或者ollama 或者api ,都挺啰嗦
* After searching on GitHub for a while, it seems to be the only solution that currently supports localized deployment of DeepSeek-r1 on Comfyui
* Officially not provided, comfy is mainly AIGC. Other options such as Olama or API are quite verbose

## 版本说明
## 2025-1-23,发布首v0.1
## 2025-1-28,v0.2
* 删除了系统提示词输入栏
* 14B测试需要，azw_nodes azw_nodes.py的60含，增加了一个cuda模式，需要手动修改，小白勿动。
* 测试环境是3090-24G，各组14B以下模型测试正常。有问题，大部分应该是显存不够。
* 增加一个《r1大模型智障问题测试数据集zw双语版》，方便大家play。
*Removed the system prompt word input field
*The 14B test requires the addition of a CUDA mode to azw_nodes' azw_nodes. py with a value of 60, which needs to be manually modified. Do not touch it, novices.
*The testing environment is 3090-24G, and the models below 14B in each group are tested normally. There is a problem, most of it should be due to insufficient video memory.
*Add a bilingual version of the "r1 Big Model Intellectual Disability Test Dataset ZW" for everyone to play.

## 模型文件在：The model file is located at:
* https://hf-mirror.com/deepseek-ai/DeepSeek-R1
* https://huggingface.co//deepseek-ai/DeepSeek-R1
* #
* 下载复制到models的deepseek\目录下即可
* 目前测试通过的有：
* *Download and copy to the deepseed directory of models
* Currently, the following have passed the test:
* #
* ComfyUI\models\deepseek\DeepSeek-R1-Distill-Llama-8B
* ComfyUI\models\deepseek\DeepSeek-R1-Distill-Qwen-1.5B
* ComfyUI\models\deepseek\DeepSeek-R1-Distill-Qwen-7B
* ComfyUI\models\deepseek\DeepSeek-R1-Distill-Qwen-14B

![deep-r1-run](https://github.com/user-attachments/assets/506626f7-170c-4b38-9613-4ccb19984ed7)



## 【智王AI开源组-网络社群】
![xh008](https://github.com/user-attachments/assets/4191bb09-1a33-4904-9e3f-2982d44e416f)
* zw网站：http://www.ziwang.com
* meta-font原字库：http://www.meta-font.vip，短域名 m-f.vip
* @ps，因为智王AI开源组正在转型，网站在调整升级。
* 建议大家使用github项目网站，支持留言、发帖，互动更加方便。
* #
* 智王Git网址：https://github.com/ziwang-com/
* zwai-lab项目网址：https://github.com/ziwang-com/zwai-lab

## ziwang AI Open Source Group - Online Community

* ZW website: http://www.ziwang.com
* Meta font Original Font Library: http://www.meta-font.vip , short domain m-f.vip
* @ ps, as the Zhiwang AI open source team is undergoing transformation, the website is undergoing adjustments and upgrades.
* It is recommended that everyone use the GitHub project website, which supports commenting and posting, making interaction more convenient.
* #
* Zhiwang Git website: https://github.com/ziwang-com/
* ZWAI Lab project website: https://github.com/ziwang-com/zwai-lab

## 【智王AI资源库】
* Github项目网址：https://github.com/ziwang-com/zwai-lab
* 百度网盘-链接:  https://pan.baidu.com/s/1EH19ablXVLYQP1f-IaPS-Q?pwd=hiks  提取码:hiks 
* 阿里云盘-链接:  https://www.alipan.com/s/pZ5qewjCec8  提取码: fs64
* #
* QQ社群，都是千人大群，欢迎加入，共同学习。
* QQ群文件，和网盘，有海量AI资源/模型/文档，提供免费下载。
* 微信群请先+管理员微信：zwpython，注明：加群。

-------------
## 【ziwang AI Resource Library】
* Github: https://github.com/ziwang-com/zwai-lab
* Baidu Cloud Drive - Link: https://pan.baidu.com/s/1EH19ablXVLYQP1f-IaPS-Q?pwd=hiks Extract code: hiks
* Alibaba Cloud Drive - Link: https://www.alipan.com/s/pZ5qewjCec8 Extract code: fs64
* #
* QQ community is a large group of thousands of people, welcome to join and learn together.
* QQ group files, online disks/official account, and massive AI resources/models/documents are available for free download. Scan to join for free.

* WeChat group, please first add the administrator's WeChat: zwpython， Note: Add to group.
  
