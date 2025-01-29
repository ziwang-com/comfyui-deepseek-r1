# comfyui-deepseek-r1
* comfyui-deepseek-r1 节点插件.Comfyui-deepseek-r1 Node Plugin
* 节点插件安装很简单，copy到comfyui的custom_nodes子目录下即可。
* The installation of the node plugin is very simple, just copy it to the custom_nodes subdirectories of comfyui.
* 
## 2025-1-29：智王发布deepseek-r1懒人包，解压即用
* 下载地址见文末，【智王AI资源中心】
* 相关网址：
* https://github.xyz/ziwang-com/comfyui-deepseek-r1
* https://github.xyz/ziwang-com/zwai-lab
* #
* ComfyUI-r1节点原本是zwai自用的，发布这么久，很奇怪，到目前还是git上面，还是只有我们这个r1插件能够本地化部署。
* 其他都是ollama 和API模式。
* ollama主要是码农，类似linux，配置非常麻烦，大众用户少。
* comfy很简单，美工都是小白，总人数多，已经是AIGC准工业平台。
* 这次是r1官方没有comfy，不然ollama没机会。
* 混元 sd flux官方全部内置comfy。
* nv-sana，虽然也不兼容，官方comfyui-sana插件，因为不好用，连带sana这种能够高速直出4k的模型，一个月了都没有多少人熟悉。
* deepseek发布的Janus-Pro模型，发布次日，也就是今天，git上面就出现了近10个comfy-Janus插件。
* 可能还是r1的兼容性问题。

##2025-1-29: Zhiwang releases Deepseek-r1 Lazy Package, easy to decompress and use
* The download link can be found at the end of the article, 【 Zhiwang AI Resource Center 】
* Related website:
*  https://github.xyz/ziwang-com/comfyui-deepseek-r1
*  https://github.xyz/ziwang-com/zwai-lab
* #
* The ComfyUI-r1 node was originally intended for ZWAI's own use, and it's strange that it has been released for so long. So far, it's still on Git, and only our r1 plugin can be deployed locally.
* The rest are in the ollama and API modes.
* Olama is mainly a code farmer, similar to Linux, with very complicated configuration and few mass users.
* Comfy is very simple. The artists are all novices, and the total number of people is large. It is already an AIGC quasi industrial platform.
* This time it's r1 official and there's no comfy, otherwise Olama wouldn't have had a chance.
* The official hybrid SD flux has all built-in Comfy.
* Nv sana, although not compatible, the official comfyui sana plugin is not very user-friendly, and even models like Sana that can produce 4k at high speed have not been familiar to many people for a month.
* The Janus Pro model released by Deepseek, on the day after its release, almost 10 comedy Janus plugins appeared on Git today.
* Perhaps it's still a compatibility issue with r1.

* ps：
* 过了小一周，r1大火开始蔓延，本地化部署案例也出了不少。
* 不过，好像zwai的deepseek-r1插件方案，仍然是目前唯一支持comfyui的。
* 这个，可能是因为官方没有提供，comfy侧重aigc，美工居多，码农少。
* 插件地址：
* https://github.com/ziwang-com/comfyui-deepseek-r1
* 参见： 全球首发deepseek-r1插件ComfyUI
* 
## 智王deepseek-r1懒人包【使用说明】
## ziwang Deepseek-r1 Lazy Pack 【 Instructions 】
* r1节点包发布后，很多老友想试用，一直找不到简单方便的集成版本法。
* ComfyUI-r1节点和智王deepseek-r1懒人包，没有太多技术含量，绿色软件，解压即用。
* 
* 
* After a week, the R1 fire began to spread, and there were also many localized deployment cases.
* However, it seems that ZWAI's DeepSeek-r1 plugin solution is still the only one currently supporting Comfyui.
* This may be because the official did not provide it. Comfy focuses more on AIGC, with more graphic designers and fewer code farmers.
* 
* 解压后，主要文件目录结构有 Plugin address:
* * d:\zwai-lab-r1\
  * d:\zwai-lab-r1\zw.bat，运行zw.bat即可进入comfyUI系统。
  * d:\zwai-lab-r1\doc\,相关文档目录
  * d:\zwai-lab-r1\doc\deepseek-r1-zwai.json，智网r1测试工作流


## 其他参看 Other references:：
* doc目录下的zwai-lab智王AI工坊文档，
* comfyui-deepseek-r1说明文档
* The zwai lab Zhiwang AI Workshop documentation in the doc directory,
* Comfyui-deepseek-r1 documentation
* 相关网址：Related website:
* https://github.xyz/ziwang-com/comfyui-deepseek-r1
* https://github.xyz/ziwang-com/zwai-lab
* 
* 官方以下版本模型测试ok，其他自己测试：
* The following official versions of the model have been tested OK, please test others yourself:
* DeepSeek-R1-Distill-Llama-8B
* DeepSeek-R1-Distill-Qwen-1.5B
* DeepSeek-R1-Distill-Qwen-7B
* DeepSeek-R1-Distill-Qwen-14B
* 
* 模型下载后，复制到目录:
* D:\zwai-lab-r1\comfyUI\models



## 【官方模型下载地址】[Official model download link]

* https://hf-mirror.com/deepseek-ai/DeepSeek-R1
* https://huggingface.co//deepseek-ai/DeepSeek-R1
* 
* r1懒人包，是zwai-lab智网AI工坊的r1定制版本，主要差异有：
* 最大程度，简化了各种comfyUI节点，和python模型。
* 内置1.5B模型，其他自己下载。
* R1 Lazy Pack is a customized version of ZWAI Lab's intelligent network AI workshop, with the main differences being:
* Maximized simplification of various comfyUI nodes and Python models.
* Built in 1.5B model, download others yourself.


## ps,2025-1-28
* github搜了半天，好像是目前唯一支持comfyui本地化部署deepseek-r1的方案
* 官方没有提供，comfy主要aigc。其他或者ollama 或者api ,都挺啰嗦
* After searching on GitHub for a while, it seems to be the only solution that currently supports localized deployment of DeepSeek-r1 on Comfyui
* Officially not provided, comfy is mainly AIGC. Other options such as Olama or API are quite verbose

## 版本说明
## 2025-1-23,发布v0.1
## 2025-1-28,v0.2
* 删除了系统提示词输入栏
* 14B测试需要，azw_nodes azw_nodes.py的60含，增加了一个cuda模式，需要手动修改，小白勿动。
* 测试环境是3090-i9-64G-3090-24G。
* 1.5B-14B模型测试正常。有问题，大部分应该是显存不够。
* R1-7B大约10-15s答复一个问题，14B要150s。
* 增加一个《r1大模型智障问题测试数据集zw双语版》，方便大家play。
* 
* Removed the system prompt word input field
* The 14B test requires the addition of a CUDA mode to azw_nodes' azw_nodes. py with a value of 60, which needs to be manually modified. Do not touch it, novices.
* The testing environment is 3090-i9-64G-3090-24G.
* The 1.5B-14B model test is normal. There is a problem, most of it should be due to insufficient video memory.
* R1-7B takes approximately 10-15 seconds to answer a question, while 14B takes 150 seconds.
* Add a bilingual version of the "r1 Big Model Intellectual Disability Test Dataset ZW" for everyone to play.

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

## ps
* https://github.com/ziwang-com/zwai-team
* 智王AI开源团队·倡议书
* Zhiwang AI Open Source Team · Proposal
* 各位关注人工智能发展的朋友们，随着人工智能技术的不断进步，我们已经看到了AI在各个领域的广泛应用，尤其是在商业方面的巨大潜力。 然而，仅仅依靠技术的进步还不足以实现可持续的发展，我们还需要将这些技术转化为实际的商业应用，探索AI变现的新机会。 因此，我们在此发起组建一个以“AI变现”为核心目标的开源团体。
* Dear friends who are concerned about the development of artificial intelligence, with the continuous progress of artificial intelligence technology, we have seen the widespread application of AI in various fields, especially in the field of business, with enormous potential. However, relying solely on technological advancements is not enough to achieve sustainable development. We also need to translate these technologies into practical commercial applications and explore new opportunities for AI monetization. Therefore, we hereby initiate the formation of an open-source group with the core goal of "AI monetization".


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
  
