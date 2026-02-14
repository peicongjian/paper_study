# Paper Summaries - NVMe, SSD, AI Infrastructure, Storage

Quick summaries of papers related to NVMe, SSD, AI infrastructure, and storage.

---

## Paper 1

# Paper Summary: ByteHouse: A Cloud-Native OLAP Engine with Incremental Computation and Multi-Modal Retrieval

## File: 2602.08226v1.pdf

## Abstract
ByteHouse: ByteDance’s Cloud-Native Data Warehouse for Real-Time Multimodal Data Analytics Yuxing Han Yu Lin Yifeng Dong Xuanhe Zhou ByteDance ByteDance ByteDance Shanghai Jiao Tong Univ. hanyuxing@bytedance.com linyu.michael@tiktok.com dongyifeng@bytedance.com zhouxuanhe@sjtu.edu.cn XinDong Peng Xinhui Tian Zhiyuan You Yingzhong Guo ByteDance ByteDance ByteDance ByteDance pengxindong@bytedance.co...

## Key Points
### 1. Background Problem
To address these challenges, we introduce Video ByteHouse (https:// bytehouse.cloud), a cloud-native data warehouse Distributed Cache Unified Table Engine Deduplication Video designed for real-time multimodal data analytics.
### 2. Solution Approach
To address these challenges, we introduce Video ByteHouse (https:// bytehouse.cloud), a cloud-native data warehouse Distributed Cache Unified Table Engine Deduplication Video designed for real-time multimodal data analytics.
### 3. Innovation
Evaluations on (e.g., delta-aware computation) and the data level (e.g., handling internal and standard workloads show that ByteHouse achieves newly ingested rows).
### 4. Results
Evaluations on (e.g., delta-aware computation) and the data level (e.g., handling internal and standard workloads show that ByteHouse achieves newly ingested rows).
### 5. Related Work
However, in ByteDance’s production envi- ronments, existing systems fall short due to limitations such as I/O- ByteHouse Ecosystem Log Analysis inefficient multimodal storage, inflexible query optimization (e.g., Text Hybrid Data Hybrid Data Hybrid Data failing to optimize multimodal access patterns), and performance Search Processing Analytics Text/Image Retrieval degradation caused by resource disaggregation (e.g., loss of data lo- Image Incremental Processing Multi-Modal Search cality in remote storage).

---

## Paper 2

# Paper Summary: FusionANNS: An Efficient CPU/GPU Cooperative Processing Architecture for Billion-scale Approximate Nearest Neighbor Search

## File: 2409.16576v1.pdf

## Abstract
FusionANNS: An Efficient CPU/GPU Cooperative Processing Architecture for Billion-scale Approximate Nearest Neighbor Search Bing Tian† , Haikun Liu† , Yuhang Tang† , Shihai Xiao‡ , Zhuohui Duan† , Xiaofei Liao† , Xuecang Zhang‡ , Junhua Zhu‡ , Yu Zhang† † National Engineering Research Center for Big Data Technology and System, Service Computing Technology and System Lab/Cluster and Grid Computing L...

## Key Points
### 1. Background Problem
Knowledge Interface With Knowledge Ever-increasing vector datasets pose significant challenges in 3.Query Request LLM Store 4.Knowledge terms of performance, cost, and accuracy for ANNS services.
### 2. Solution Approach
Specifically, the most relevant knowledge from the vector database, allow- we propose three novel designs: (1) multi-tiered indexing to ing the LLM to use that knowledge as additional context for avoid data swapping between CPUs and GPU, (2) heuristic more accurate inference.
### 3. Innovation
Specifically, the most relevant knowledge from the vector database, allow- we propose three novel designs: (1) multi-tiered indexing to ing the LLM to use that knowledge as additional context for avoid data swapping between CPUs and GPU, (2) heuristic more accurate inference.
### 4. Results
Experimental results show For example, state-of-the-art IVF-based RUMMY [9] and that FusionANNS achieves 1) 9.4-13.1× higher query per graph-based Bang [10] require terabyte-scale memory space second (QPS) and 5.7-8.8× higher cost efficiency compared to accommodate billion-scale vectors and their indices.
### 5. Related Work
To simplify the problem, we use a priority queue Q (i.e., a that is commonly experienced in previous GPU-accelerated max-heap) to maintain the current top-k nearest neighbours.

---

## Paper 3

# Paper Summary: Software-Hardware Co-design for Fast and Scalable Training of Deep Learning Recommendation Models

## File: 2104.05158v7.pdf

## Abstract
Software-Hardware Co-design for Fast and Scalable Training of Deep Learning Recommendation Models ∗ Dheevatsa Mudigere†‡ , Yuchen Hao†‡ , Jianyu Huang†‡ , Zhihao Jia§ , Andrew Tulloch‡ , Srinivas Sridharan‡ , Xing Liu‡ , Mustafa Ozdal‡ , Jade Nie‡ , Jongsoo Park‡ , Liang Luo‡ , Jie (Amy) Yang‡ , Leon Gao‡ , Dmytro Ivchenko‡ , Aarti Basant‡ , Yuxi Hu‡ , Jiyan Yang‡ , Ehsan K. Ardestani‡ , Xiaodong ...

## Key Points
### 1. Background Problem
rameters and therefore terabytes in size poses a serious challenge to ISCA ’22, June 18–22, 2022, New York, NY, USA D.
### 2. Solution Approach
Software-Hardware Co-design for Fast and Scalable Training of Deep Learning Recommendation Models ∗ Dheevatsa Mudigere†‡ , Yuchen Hao†‡ , Jianyu Huang†‡ , Zhihao Jia§ , Andrew Tulloch‡ , Srinivas Sridharan‡ , Xing Liu‡ , Mustafa Ozdal‡ , Jade Nie‡ , Jongsoo Park‡ , Liang Luo‡ , Jie (Amy) Yang‡ , Leon Gao‡ , Dmytro Ivchenko‡ , Aarti Basant‡ , Yuxi Hu‡ , Jiyan Yang‡ , Ehsan K.
### 3. Innovation
Neo employs a novel 4D parallelism strategy zations, such as MLCommons (MLPerf) [38, 52].
### 4. Results
As a that Neo outperforms existing systems by up to 40× for training result, DLRMs generally exhibit much lower arithmetic intensity 12-trillion-parameter DLRM models deployed in production.
### 5. Related Work
As a that Neo outperforms existing systems by up to 40× for training result, DLRMs generally exhibit much lower arithmetic intensity 12-trillion-parameter DLRM models deployed in production.

---

## Paper 4

# Paper Summary: Creative Ownership in the Age of AI

## File: 2602.12270v1.pdf

## Abstract
Creative Ownership in the Age of AI Annie Liang∗ Jay Lu† arXiv:2602.12270v1 [econ.TH] 12 Feb 2026 February 13, 2026 Abstract Copyright law focuses on whether a new work is “substantially similar” to an existing one, but generative AI can closely imitate style without copying content, a capability now central to ongoing litigation. We argue that exist- ing definitions of infringement are ill-suited...

## Key Points
### 1. Background Problem
Our paper in particular addresses the following problem, as described in de Rassenfosse et al.
### 2. Solution Approach
We argue that exist- ing definitions of infringement are ill-suited to this setting and propose a new criterion: a generative AI output infringes on an existing work if it could not have been generated without that work in its training corpus.
### 3. Innovation
Creative Ownership in the Age of AI Annie Liang∗ Jay Lu† arXiv:2602.12270v1 [econ.TH] 12 Feb 2026 February 13, 2026 Abstract Copyright law focuses on whether a new work is “substantially similar” to an existing one, but generative AI can closely imitate style without copying content, a capability now central to ongoing litigation.
### 4. Results
Our results characterize structural properties of permissible gener- ation and reveal a sharp asymptotic dichotomy: when the process of organic creations is light-tailed, dependence on individual works eventually vanishes, so that regulation imposes no limits on AI generation; with heavy-tailed creations, regulation can be persistently constraining.
### 5. Related Work
Creative Ownership in the Age of AI Annie Liang∗ Jay Lu† arXiv:2602.12270v1 [econ.TH] 12 Feb 2026 February 13, 2026 Abstract Copyright law focuses on whether a new work is “substantially similar” to an existing one, but generative AI can closely imitate style without copying content, a capability now central to ongoing litigation.

---

## Paper 5

# Paper Summary: CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use

## File: 2602.12268v1.pdf

## Abstract
CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use Zhen Zhang1 Kaiqiang Song2 Xun Wang2 Yebowen Hu3 Weixiang Yan 1 Chenyang Zhao4 Henry Peng Zou 5 Haoyun Deng 2 Sathish Reddy Indurthi 2 Shujian Liu 2 Simin Ma 2 Xiaoyang Wang 2 Xin Eric Wang †1 Song Wang †2 1 University of California, Santa Barbara 2 Zoom Video Communications 3 University of Central Fl...

## Key Points
### 1. Background Problem
However, training general-purpose agents to master such interactions through reinforcement learning (RL) remains a huge challenge.
### 2. Solution Approach
We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards.
### 3. Innovation
If the action is a final reply, the current turn terminates, and any subsequent user query initiates a new turn.
### 4. Results
The results match or even outperform similarly sized open-source baselines, including the judging model.
### 5. Related Work
First, existing work largely relies on verifiable rewards [8].

---

## Paper 6

# Paper Summary: Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting

## File: 2602.12256v1.pdf

## Abstract
Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting Alex Chudic Gül Çalıklı alex@freetobook.co.uk handangul.calikli@glasgow.ac.uk US Booking Services Ltd. (freetobook) University of Glasgow United Kingdom United Kingdom Abstract Beyond verification, unit tests serve as executable documentation Unit testing is essential for verifying the functional correctness of th...

## Key Points
### 1. Background Problem
Following the discovery of Vaswani selecting examples based on the combined similarity of problem et al.
### 2. Solution Approach
(freetobook) University of Glasgow United Kingdom United Kingdom Abstract Beyond verification, unit tests serve as executable documentation Unit testing is essential for verifying the functional correctness of that developers rely on to understand program behavior, design in- code modules (e.g., classes, methods), but manually writing unit tent, and edge cases, particularly during maintenance and evolution.
### 3. Innovation
By high proportion of the LLM-generated test cases fail due to com- measuring the coverage improvement of the newly generated test pilation or execution errors, in most cases caused by minor is- cases, we aim to provide actionable insights into the real-world sues, e.g., syntactic issues or missing imports [30, 45].
### 4. Results
As a result, the quality and structure of test code directly affect arXiv:2602.12256v1 [cs.SE] 12 Feb 2026 tests is often labor-intensive and time-consuming.
### 5. Related Work
The tradi- artifact sources, comprising human, SBST, or LLM, affects the qual- tional approaches, such as random-based [25, 26], constraint-based ity of LLM-generated unit tests as program comprehension artifacts [42], and search-based testing [14–16], have demonstrated their and their contribution to improving existing test suites by evaluat- ability to generate tests with reasonable test coverage.

---

## Paper 7

# Paper Summary: A technical curriculum on language-oriented artificial intelligence in translation and specialised communication

## File: 2602.12251v1.pdf

## Abstract
A Technical Curriculum on Language-Oriented Artificial Intelligence in Translation and Specialised Communication Ralph Krüger Institute of Translation and Multilingual Communication TH Köln – University of Applied Sciences Cologne, Germany ralph.krueger@th-koeln.de arXiv:2602.12251v1 [cs.CL] 12 Feb 2026 Abstract models (LLMs) has widened the scope of automa- tion in the L&T industry to a conside...

## Key Points
### 1. Background Problem
We always start Commons 4.0 licence, no derivative works, attribution, CC- by trying AI solutions to solve language problems.“ (https: BY-ND.
### 2. Solution Approach
Re- in the spirit of the human-centered AI approach sults suggest the didactic effectiveness of (Shneiderman, 2020) – L&T industry stakehold- the curriculum, but participant feedback ers require domain-specific AI literacy, as con- indicates that it should be embedded into ceptualised, e.g., in the AI literacy framework higher-level didactic scaffolding – e.g., in proposed in Krüger (2024) and Krüger (forth- the form of lecturer support – in order to coming).
### 3. Innovation
Further- eracy among stakeholders in the fields of more, LLMs can augment traditional translation translation and specialised communication technologies with new features that were previ- by exposing them to the conceptual and ously beyond the scope of these technologies (e.g., technical/algorithmic foundations of mod- augmenting traditional automatic translation qual- ern language-oriented AI in an accessi- ity control with meaning-based source- and target- ble way.
### 4. Results
The post-test questionnaire was completed by by a hidden layer in the network (excluding the ac- 15 participants, resulting in a survey attrition rate tivation function at this point).
### 5. Related Work
computational thinking as well as algo- The current LLM-driven automation cycle in the rithmic awareness and algorithmic agency, L&T industry is shaping up to be both more ex- ultimately contributing to their digital re- tensive and more invasive than previous automa- silience in AI-driven work environments.

---

## Paper 8

# Paper Summary: VIRENA: Virtual Arena for Research, Education, and Democratic Innovation

## File: 2602.12207v1.pdf

## Abstract
VIRENA ∗ Virtual Arena for Research, Education, and Democratic Innovation Emma Hoes† K. Jonathan Klüser Fabrizio Gilardi Department of Political Science arXiv:2602.12207v1 [cs.HC] 12 Feb 2026 University of Zurich February 13, 2026 Abstract Digital platforms shape how people communicate, deliberate, and form opin- ions. Studying these dynamics has become increasingly difficult due to restricted dat...

## Key Points
### 1. Background Problem
† Corresponding author: hoes@ipz.uzh.ch 1 1 Introduction 1.1 The Challenge of Studying Digital Communication Social media platforms have become central to public discourse, yet studying how people behave, communicate, and are influenced in these environments has become increasingly difficult.
### 2. Solution Approach
VIRENA makes possible research designs that were previously impractical: studying human–AI interaction in realistic social contexts, experimentally comparing moderation interventions, and observing group deliberation as it unfolds.
### 3. Innovation
This preprint will be updated as new features are released.
### 4. Results
Simplified ethical review: Because VIRENA operates in fully isolated environments with no connection to real social media accounts, institutional review boards can evaluate studies without the complications associated with real-platform experiments, such as uncontrolled exposure to harmful content or risks to participants’ digital footprints.
### 5. Related Work
VIRENA makes possible research designs that were previously impractical: studying human–AI interaction in realistic social contexts, experimentally comparing moderation interventions, and observing group deliberation as it unfolds.

---

## Paper 9

# Paper Summary: Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education

## File: 2602.12196v1.pdf

## Abstract
Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education Mohamed Huti1 Alasdair Mackintosh1 Amy Waldock1 Dominic Andrews1 Maxime Lelièvre1 Moritz Boos1 Tobias Murray1 arXiv:2602.12196v1 [cs.CL] 12 Feb 2026 Paul Atherton1 Robin A. A. Ince1 Oliver G. B. Garrod1 1 Fab AI Abstract AI models have achieved state-of-the-art results in textual re...

## Key Points
### 1. Background Problem
Visual Reasoning Benchmark: Evaluating Multimodal LLMs on Classroom-Authentic Visual Problems from Primary Education Mohamed Huti1 Alasdair Mackintosh1 Amy Waldock1 Dominic Andrews1 Maxime Lelièvre1 Moritz Boos1 Tobias Murray1 arXiv:2602.12196v1 [cs.CL] 12 Feb 2026 Paul Atherton1 Robin A.
### 2. Solution Approach
This paper introduces the visual reasoning benchmark (VRB), a novel dataset designed to evaluate Multimodal Large Language Models (MLLMs) on their ability to solve authentic visual problems from classrooms.
### 3. Innovation
This paper introduces the visual reasoning benchmark (VRB), a novel dataset designed to evaluate Multimodal Large Language Models (MLLMs) on their ability to solve authentic visual problems from classrooms.
### 4. Results
Garrod1 1 Fab AI Abstract AI models have achieved state-of-the-art results in textual reasoning; however, their ability to reason over spatial and relational structures remains a critical bottleneck— particularly in early-grade maths, which relies heavily on visuals.
### 5. Related Work
2 Related Work Research on visual reasoning has developed along distinct trajectories, each addressing different aspects of the challenge.

---

## Paper 10

# Paper Summary: SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization

## File: 2602.12187v1.pdf

## Abstract
SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization Sunghwan Kim Wooseok Jeong Serin Kim Department of Artificial Intelligence Department of Computer Science and Department of Artificial Intelligence Yonsei University Engineering Yonsei University Seoul, Republic of Korea Konkuk University Seoul, Republic of Korea happysnail06@yonsei.ac.kr Seoul, Rep...

## Key Points
### 1. Background Problem
Crucially, our benchmark is distinguished in two ways: challenges for content creators, motivating research on optimiza- (1) Comprehensive generative search environment.
### 2. Solution Approach
Motivated by these large-scale retrieval with generative capabilities, these systems per- gaps, we introduce SAGEO Arena, a realistic and reproducible envi- form generative search, providing synthesized answers that directly ronment for stage-level SAGEO analysis.
### 3. Innovation
SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization Sunghwan Kim Wooseok Jeong Serin Kim Department of Artificial Intelligence Department of Computer Science and Department of Artificial Intelligence Yonsei University Engineering Yonsei University Seoul, Republic of Korea Konkuk University Seoul, Republic of Korea happysnail06@yonsei.ac.kr Seoul, Republic of Korea kimserin@yonsei.ac.kr oseoko8@gmail.com Sangam Lee Dongha Lee∗ arXiv:2602.12187v1 [cs.IR] 12 Feb 2026 Department of Artificial Intelligence Department of Artificial Intelligence Yonsei University Yonsei University Seoul, Republic of Korea Seoul, Republic of Korea salee@yonsei.ac.kr donalee@yonsei.ac.kr Abstract Keywords Search-Augmented Generative Engines (SAGE) have emerged as a Search-Augmented Generative Engine, Generative Engine Opti- new paradigm for information access, bridging web-scale retrieval mization, Search Engine Optimization, Benchmark, Evaluation with generative capabilities to deliver synthesized answers.
### 4. Results
To achieve this, we integrate a full genera- exposure online is fundamentally changing.
### 5. Related Work
Specifically, existing benchmarks //doi.org/XXXXXXX.XXXXXXX lack end-to-end visibility evaluation of optimization strategies, op- erating on pre-determined candidate documents that abstract away 1 Introduction retrieval and reranking preceding generation.

---

## Paper 11

# Paper Summary: Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation

## File: 2602.12172v1.pdf

## Abstract
Published as a conference paper at ICLR 2026 P EDAGOGICALLY-I NSPIRED DATA S YNTHESIS FOR L ANGUAGE M ODEL K NOWLEDGE D ISTILLATION Bowei He1,2 , Yankai Chen1,2,∗ , Xiaokun Zhang3 , Linghe Kong4 , Philip S. Yu5 , Xue Liu1,2 , Chen Ma3,∗ 1 MBZUAI, 2 McGill, 3 CityUHK, 4 SJTU, 5 UIC A BSTRACT arXiv:2602.12172v1 [cs.AI] 12 Feb 2026 Knowledge distillation from Large Language Models (LLMs) to smaller m...

## Key Points
### 1. Background Problem
Beyond these, counterfactual data synthesis (Feng et al., 2024a) has been proposed to encourage more robust reasoning by exposing the student to alternative problem- solving perspectives.
### 2. Solution Approach
In this paper, we propose a novel pedagogically-inspired framework for LLM knowledge distillation that draws from fundamental educa- tional principles.
### 3. Innovation
In this paper, we propose a novel pedagogically-inspired framework for LLM knowledge distillation that draws from fundamental educa- tional principles.
### 4. Results
Extensive experiments using LLaMA-3.1/3.2 and Qwen2.5 as student models demonstrate that IOA achieves significant improvements over baseline distillation methods, with student models retaining 94.7% of teacher performance on DollyEval while using less than 1/10th of the parameters.
### 5. Related Work
Based on such inspirations, we analyze the drawbacks of existing methods as follows: 1) Knowledge Identification: Current synthetic data generation lacks knowledge-aware targeting and fails to identify the specific knowledge that SLMs require to develop certain capabilities.

---

## Paper 12

# Paper Summary: On the Adoption of AI Coding Agents in Open-source Android and iOS Development

## File: 2602.12144v1.pdf

## Abstract
On the Adoption of AI Coding Agents in Open-source Android and iOS Development Muhammad Ahmad Khan Hasnain Ali Muneeb Rana 25030004@lums.edu.pk 25280088@lums.edu.pk muneebrana625@gmail.com Lahore University of Management Lahore University of Management Xtra App Studios Sciences Sciences Multan, Pakistan Lahore, Pakistan Lahore, Pakistan Muhammad Saqib Ilyas Abdul Ali Bangash saqibm@lums.edu.pk abd...

## Key Points
### 1. Background Problem
This exclusion left us with 193 projects address this issue, we applied Bayesian add-𝛼 smoothing [8].
### 2. Solution Approach
ment, yet their impact on mobile development has received little Mobile development involves complex settings of design, logic empirical attention.
### 3. Innovation
ACM, New York, NY, USA, 5 pages.
### 4. Results
have received 2x more AI-authored PRs and have achieved higher To address this gap, we analyzed 2, 901 AI-authored PRs in 193 PR acceptance rate (71%) than iOS (63%), with significant agent- verified Android and iOS open-source GitHub repositories from level variation on Android.
### 5. Related Work
The combined results highlight where agent- Implication: PR resolution efficiency depends on mobile platform, PR task generated changes align well with existing review practices and category, and agent choice.

---

## Paper 13

# Paper Summary: Embodied AI Agents for Team Collaboration in Co-located Blue-Collar Work

## File: 2602.12136v1.pdf

## Abstract
Embodied AI Agents for Team Collaboration in Co-located Blue-Collar Work (CAI- BLUE) Embodied AI Agents for Blue-Collar Work Kaisa Väänänen Tauchi Research Centre, Faculty of Information Technology and Communication Sciences, Tampere University, Finland, kaisa.vaananen@tuni.fi Niels van Berkel Department of Computer Science, Aalborg University, Denmark, nielsvanberkel@cs.aau.dk Donald McMillan Dep...

## Key Points
### 1. Background Problem
When a mechanical issue arises, the AI assists the team by analysing sensor data and suggesting potential causes.
### 2. Solution Approach
We outline open questions related to embodied AI agent design around worker inclusion, agency, transformation of blue-collar collaboration practices over time, and forms of acceptable AI embodiments.
### 3. Innovation
From the context of our newly started CAI-BLUE research project, we present two speculative scenarios from industrial and maintenance contexts that illustrate how embodied AI agents can support shared situational awareness and facilitate inclusive communication across experience levels.
### 4. Results
<!-- Describe results -->

### 5. Related Work
We outline open questions related to embodied AI agent design around worker inclusion, agency, transformation of blue-collar collaboration practices over time, and forms of acceptable AI embodiments.

---

## Paper 14

# Paper Summary: Capability-Oriented Training Induced Alignment Risk

## File: 2602.12124v1.pdf

## Abstract
Capability-Oriented Training Induced Alignment Risk Yujun Zhou1,* , Yue Huang1,* , Han Bao1,* , Kehan Guo1 , Zhenwen Liang3 Pin-Yu Chen2 , Tian Gao2 , Werner Geyer2 , Nuno Moniz1 , Nitesh V. Chawla1 , Xiangliang Zhang1 1 University of Notre Dame 2 IBM Research 3 Tencent AI Lab * Equal Contribution {yzhou25,xzhang33}@nd.edu Abstract: While most AI alignment research focuses on preventing models fro...

## Key Points
### 1. Background Problem
Our findings reveal that capability-oriented training induced risks pose a fundamental challenge to current alignment approaches, suggesting that future AI safety work must extend beyond content moderation to rigorously auditing and securing the training environments and reward mechanisms themselves.
### 2. Solution Approach
To test this, we design a suite of four diverse “vulnerability games”, each presenting a unique, exploitable flaw related to context-conditional compliance, proxy metrics, reward tampering, and self-evaluation.
### 3. Innovation
More critically, we find that these exploitative strategies are not narrow “tricks” but generalizable skills; they can be transferred to new tasks and even “distilled” from a capable teacher model to other student models through data alone.
### 4. Results
It has been shown that in certain strategic situations, such as simulated corporate environments, current models can learn to conceal their true intentions to achieve their goals (Greenblatt et al., 2024; Hammond et al., 2025; Denison et al., 2024).
### 5. Related Work
To test this, we design a suite of four diverse “vulnerability games”, each presenting a unique, exploitable flaw related to context-conditional compliance, proxy metrics, reward tampering, and self-evaluation.

---

## Paper 15

# Paper Summary: KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite

## File: 2602.12117v1.pdf

## Abstract
KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite Jiakang Shen Qinghui Chen Runtong Wang Shandong University Shandong University Shandong University School of Control Science and School of Control Science and School of Control Science and Engineering Engineering Engineering Jinan, Shandong, China Jinan, Shandong, China Jinan, Shandong, ...

## Key Points
### 1. Background Problem
To overcome these challenges, this study introduces the Kolmogorov–Arnold Network-based Feature Interac- Keywords tion Framework (KAN-FIF), a lightweight multimodal architecture Tropical Cyclone Estimation; FY-4 series meteorological satellite; that integrates MLP and CNN layers with spline-parameterized Kolmogorov–Arnold Network; Edge-device AI applications; Multi- KAN layers.
### 2. Solution Approach
To overcome these challenges, this study introduces the Kolmogorov–Arnold Network-based Feature Interac- Keywords tion Framework (KAN-FIF), a lightweight multimodal architecture Tropical Cyclone Estimation; FY-4 series meteorological satellite; that integrates MLP and CNN layers with spline-parameterized Kolmogorov–Arnold Network; Edge-device AI applications; Multi- KAN layers.
### 3. Innovation
ACM, New York, NY, USA, 9 pages.
### 4. Results
KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite Jiakang Shen Qinghui Chen Runtong Wang Shandong University Shandong University Shandong University School of Control Science and School of Control Science and School of Control Science and Engineering Engineering Engineering Jinan, Shandong, China Jinan, Shandong, China Jinan, Shandong, China 202300171054@mail.sdu.edu.cn 202420785@mail.sdu.edu.cn 202300171170@mail.sdu.edu.cn Chenrui Xu Jinglin Zhang∗ Cong Bai arXiv:2602.12117v1 [cs.LG] 12 Feb 2026 Shandong University Shandong University Zhejiang University of Technology School of Control Science and School of Control Science and College of Computer Science Engineering Engineering Hangzhou, Zhejiang, China Jinan, Shandong, China Jinan, Shandong, China congbai@zjut.edu.cn 202300171055@mail.sdu.edu.cn jinglin.zhang@sdu.edu.cn Feng Zhang Fudan University Department of Atmospheric and Oceanic Sciences and Institutes of Atmospheric Sciences Shanghai, China fengzhang@fudan.edu.cn Abstract board achieved a 14.41ms per-sample inference latency with the Tropical cyclones (TC) are among the most destructive natural KAN-FIF framework, demonstrating promising feasibility for oper- disasters, causing catastrophic damage to coastal regions through ational TC monitoring and extending deployability to edge-device extreme winds, heavy rainfall, and storm surges.
### 5. Related Work
yet it is hindered by the computational inefficiency and high pa- rameter counts of existing methods on resource-constrained edge CCS Concepts devices.

---

## Paper 16

# Paper Summary: The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context

## File: 2602.12108v1.pdf

## Abstract
The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context Xiaoyuan Liu1,2 , Tian Liang1 , Dongyang Ma1 , Deyu Zhou , Haitao Mi1 , Pinjia He2 , Yan Wang1,† 1 Tencent AI Lab 2 The Chinese University of Hong Kong, Shenzhen † Project Lead xyliu.cs@gmail.com, yanwang.branden@gmail.com In the world of Harry Potter, when Dumbledore’s mind is overburdened, he extracts memories into a arX...

## Key Points
### 1. Background Problem
Further analysis shows that the improvements are consistent across diverse problem aspects, and that the learned tool-use patterns adapt accordingly to different tasks.
### 2. Solution Approach
We introduce StateLM, a new class of foundation models endowed with an internal reasoning loop to manage their own state.
### 3. Innovation
We introduce StateLM, a new class of foundation models endowed with an internal reasoning loop to manage their own state.
### 4. Results
On long-document QA tasks, StateLMs consistently outperform standard LLMs across all model scales; on the chat memory task, they achieve absolute accuracy improvements of 10% to 20% over standard LLMs.
### 5. Related Work
2 Related Work: Human as the Wizard The core challenge of statelessness has not gone unnoticed.

---

## Paper 17

# Paper Summary: DeepSight: An All-in-One LM Safety Toolkit

## File: 2602.12092v1.pdf

## Abstract
—­ -- 上海人工智能实验室 -:=-.==.. � Shanghai Artificial Intelligence Laboratory DeepSight DeepSight: An All-in-One LM Safety Toolkit Bo Zhang∗ , Jiaxuan Guo∗ , Lijun Li∗ , Dongrui Liu∗ , Sujin Chen, Guanxu Chen, Zhijie Zheng, Qihao Lin, Lewen Yan, Chen Qian, Yijin Zhou, Yuyao Wu, Shaoxiong Guo, Tianyi Du, Jingyi Yang, Xuhao Hu, Ziqi Miao, Xiaoya Lu, Jing ShaoB , Xia Hu Shanghai AI Laboratory  github.com/...

## Key Points
### 1. Background Problem
To systematically address these issues, we propose an open-source project, namely DeepSight, to practice a new safety evaluation-diagnosis integrated paradigm.
### 2. Solution Approach
To systematically address these issues, we propose an open-source project, namely DeepSight, to practice a new safety evaluation-diagnosis integrated paradigm.
### 3. Innovation
To systematically address these issues, we propose an open-source project, namely DeepSight, to practice a new safety evaluation-diagnosis integrated paradigm.
### 4. Results
2 DeepSight Framework 2.1 Overview While traditional evaluation often isolates evaluation and diagnosis, resulting in misaligned goals where evaluation identifies external risks without addressing internal root causes, DeepSight connects them into 3 DeepSight: An All-in-One LM Safety Toolkit a verifiable engineering loop, effectively transitioning from black-box assessment to white-box insight.
### 5. Related Work
21 4 Related Work 23 4.1 Evaluation Frameworks .

---

## Paper 18

# Paper Summary: Choose Your Agent: Tradeoffs in Adopting AI Advisors, Coaches, and Delegates in Multi-Party Negotiation

## File: 2602.12089v1.pdf

## Abstract
Choose Your Agent: Tradeoffs in Adopting AI Advisors, Coaches, and Delegates in Multi-Party Negotiation KEHANG ZHU∗ , Harvard University, United States NITHUM THAIN, Google DeepMind, United States VIVIAN TSAI, Google DeepMind, United States JAMES WEXLER, Google DeepMind, United States CRYSTAL QIAN, Google DeepMind, United States arXiv:2602.12089v1 [cs.GT] 12 Feb 2026 As AI usage becomes more preva...

## Key Points
### 1. Background Problem
A central challenge in this new economy is the tension between control and delegation: specifically, the normative question of when users should offload decision-making, and the behavioral question of when they actually do.
### 2. Solution Approach
Choose Your Agent: Tradeoffs in Adopting AI Advisors, Coaches, and Delegates in Multi-Party Negotiation KEHANG ZHU∗ , Harvard University, United States NITHUM THAIN, Google DeepMind, United States VIVIAN TSAI, Google DeepMind, United States JAMES WEXLER, Google DeepMind, United States CRYSTAL QIAN, Google DeepMind, United States arXiv:2602.12089v1 [cs.GT] 12 Feb 2026 As AI usage becomes more prevalent in social contexts, understanding agent-user interaction is critical to designing systems that improve both individual and group outcomes.
### 3. Innovation
Authors’ Contact Information: Kehang Zhu, kehangzhu@gmail.com, Harvard University, Cambridge, United States; Nithum Thain, Google DeepMind, United States; Vivian Tsai, Google DeepMind, United States; James Wexler, Google DeepMind, United States; Crystal Qian, Google DeepMind, New York, United States.
### 4. Results
Each game, presented in randomized order, grants access to a single LLM assistance modality: proactive recommendations from an Advisor, reactive feedback from a Coach, or autonomous execution by a Delegate; all modalities are powered by an underlying LLM that achieves superhuman performance in an all-agent environment.
### 5. Related Work
2 Related Work 2.1 Negotiation and Group Decision Making LLM-based agents demonstrate increasingly strong social capabilities across negotiation, persuasion, mediation, and multi-agent coordination tasks [1, 5, 31, 41, 42, 60, 62, 63, 65].

