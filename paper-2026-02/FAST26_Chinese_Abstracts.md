# FAST26 技术议题及其摘要

## 引言
FAST26（16th USENIX Conference on File and Storage Technologies）是存储领域的重要学术会议，于2026年2月召开。本文档整理了会议的技术议题及其摘要的中文翻译。

## Spring Accepted Papers

### OdinANN: Direct Insert for Consistently Stable Performance in Billion-Scale Graph-Based Vector Search
**作者：** Hao Guo and Youyou Lu, Tsinghua University

**摘要：** Approximate Nearest Neighbor Search (ANNS) is widely used in various scenarios. For billion-scale ANNS, on-disk graph-based indexes, which organize the vectors as a graph and store them on disk, are favored for their performance and cost-efficiency. However, existing indexes can not maintain a stable search performance while inserting new vectors. In this paper, we propose to use direct insert, which directly inserts vectors into the on-disk index, rather than buffering them in memory and merging them to disk in batches like existing systems. This approach can even out the interference of insert with frontend search, thus stabilizing the performance. We evaluate direct insert by integrating it into a billion-scale graph-based ANNS index named OdinANN. With a fixed insert rate, OdinANN outperforms state-of-the-art ANNS indexes in search latency and throughput, and it consistently shows stable performance in billion-scale vector datasets.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### SkySync: Accelerating File Synchronization with Collaborative Delta Generation
**作者：** Zhihao Zhang, Xiamen University and Alibaba Cloud; Huiba Li, Alibaba Cloud; Lu Tang, Xiamen University; Guangtao Xue, Shanghai Jiao Tong University; Jiwu Shu, Tsinghua University; Yiming Zhang, Shanghai Jiao Tong University and Xiamen University

**摘要：** File synchronization (sync) is of increasing significance for not only intra-cloud but also inter-cloud applications and services, as cloud computing is evolving into the Sky computing paradigm with the illusion of utility computing on an infrastructure of multiple geographically-distributed clouds. However, existing file sync schemes, mainly including fixed-sized chunking (FSC) based sync and content-defined-chunking (CDC) based sync, heavily rely on complex algorithms for generating the delta data. These algorithms perform costly processing operations including (i) file chunking, (ii) chunk checksum computation, and (iii) chunk searching, which incur high computational overhead thus lowering sync performance. This paper presents SkySync, a novel file sync scheme based on collaborative delta generation. Our insight is that the conventional storage layer has already maintained rich metadata (like checksums and cryptographic digests) for management purpose, e.g., to verify integrity and detect errors. Therefore, we leverage the existent metadata of the storage layer to obtain the chunk checksums with simple adaptation and combination, thus effectively reducing the computational overhead. We further streamline the chunk searching process by reusing checksum data produced during prior computations. We have implemented the FSC-based and CDC-based SkySync schemes by enhancing the communication protocol of the state-of-the-art rsync and dsync, respectively. Evaluation results show that compared to the existing file sync schemes (rsync and dsync), SkySync significantly reduces the computational overhead by up to 89.3% and improves the client and server sync performance by 1.1× ∼2×, while maintaining a consistent level of network traffic.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### CETOFS: A High-Performance File System with Host-Server Collaboration for Remote Storage
**作者：** Wenqing Jia, Dejun Jiang, and Jin Xiong, State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; and University of Chinese Academy of Sciences

**摘要：** With the development of high-performance RDMA network and modern storage devices, disaggregated NVMe SSDs have become increasingly popular due to the high resource utilization and superior performance. Although existing kernel file systems (e.g., Ext4) can directly access the disaggregated SSD via the NVMe-over-RDMA protocol, the data path suffers from heavy kernel stack overhead and thus degraded performance. The extra networking latency introduced in accessing remote storage also prevents file system from achieving scalable concurrent accesses and efficient failure-atomic IO. In this paper, we present CETOFS, a high-performance file system with host-server collaboration for disaggregated NVMe SSD. CETOFS designs a userspace-kernel collaborative architecture to place data plane entirely in userspace meanwhile separate permission checking from in-kernel control plane. Then CETOFS exploits the processing capability of remote storage server to offload three tasks: permission checking, concurrency control, and failure-atomic IO guaranteeing. The offloading mechanisms greatly reduce the networking overhead. We implement CETOFS and evaluate it against both kernel and userspace file systems. The evaluation shows CETOFS achieves high-performance data path that reduces latency by up to 52% for single-threaded file access and improves throughput by up to 19X for concurrent accesses.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### Preparation Meets Opportunity: Enhancing Data Preprocessing for ML Training With Seneca
**作者：** Omkar Desai, Syracuse University; Ziyang Jiao, Huaibei Normal University; Shuyi Pei, Samsung Semiconductor; Janki Bhimani, Florida International University; Bryan S. Kim, Syracuse University

**摘要：** Input data preprocessing is a common bottleneck when concurrently training multimedia machine learning (ML) models in modern systems. To alleviate these bottlenecks and reduce the training time for concurrent jobs, we present Seneca, a data loading system that optimizes cache partitioning and data sampling for the data storage and ingestion (DSI) pipeline. The design of Seneca contains two key techniques. First, Seneca uses a performance model for the data pipeline to optimally partition the cache for three different forms of data (encoded, decoded, and augmented). Second, Seneca opportunistically serves cached data over uncached ones during random batch sampling so that concurrent jobs benefit from each other. We implement Seneca by modifying PyTorch and demonstrate its effectiveness by comparing it against several state-of-the-art caching systems for DNN training. Seneca reduces the makespan by 45.23% compared to PyTorch and increases data processing throughput by up to 3.45× compared to the next best dataloader.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### DRBoost: Boosting Degraded Read Performance in MSR-Coded Storage Clusters
**作者：** Xiao Niu, Guangyan Zhang, Zhiyue Li, and Sijie Cai, Tsinghua University

**摘要：** Minimum Storage Regenerating (MSR) codes have strong potential for building efficient and reliable storage systems due to their excellent fault tolerance and low repair bandwidth. However, to meet MSR code constraints and optimize storage performance, systems often adopt large chunk sizes. This leads to significant I/O amplification during degraded reads, as entire chunks must be reconstructed to access a single object. In this paper, we propose DRBoost, an approach that boosts degraded read performance in MSR-coded storage clusters by reducing repair bandwidth and eliminating access fragmentation for healthy data. DRBoost introduces three key techniques: (1) a partial-chunk reconstruction algorithm that reduces repair bandwidth by leveraging two forms of data reuse; (2) a reconstruction-friendly coding layout that improves reuse efficiency and accommodates objects of diverse sizes; and (3) a fragmentation-free storage layout that avoids unnecessary request splitting. Extensive experiments under various conditions and workloads show that DRBoost reduces degraded read latency by one to two orders of magnitude, significantly improving system responsiveness.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### PolarStore: High-Performance Data Compression for Large-Scale Cloud-Native Databases
**作者：** Qingda Hu, Xinjun (Jimmy) Yang, Feifei Li, Junru Li, Ya Lin, Yuqi Zhou, Yicong Zhu, Junwei Zhang, Rongbiao Xie, Ling Zhou, Bin Wu, and Wenchao Zhou, Alibaba Cloud Computing

**摘要：** In recent years, resource elasticity and cost optimization have become essential for RDBMSs. While cloud-native RDBMSs provide elastic computing resources via disaggregated computing and storage, storage costs remain a critical user concern. Consequently, data compression emerges as an effective strategy to reduce storage costs. However, existing compression approaches in RDBMSs present a stark trade-off: software-based approaches incur significant performance overheads, while hardware-based alternatives lack the flexibility required for diverse database workloads.  In this paper, we present PolarStore, a compressed shared storage system for cloud-native RDBMSs. PolarStore employs a dual-layer compression mechanism that combines in-storage compression in PolarCSD hardware with lightweight compression in software. This design leverages the strengths of both approaches. PolarStore also incorporates database-oriented optimizations to maintain high performance on critical I/O paths. Drawing from large-scale deployment experiences, we also introduce hardware improvements for PolarCSD to ensure host-level stability and propose a compression-aware scheduling scheme to improve cluster-level space efficiency. PolarStore is currently deployed on thousands of storage servers within PolarDB, managing over 100 PB of data. It achieves a compression ratio of 3.55 and reduces storage costs by approximately 60%. Remarkably, these savings are achieved while maintaining performance comparable to uncompressed clusters.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### Cost-efficient Archive Cloud Storage with Tape: Design and Deployment
**作者：** Qing Wang, Tsinghua University; Fan Yang, Qiang Liu, and Geng Xiao, Huawei Cloud; Yongpeng Chen and Hao Lan, Tsinghua University; Leiming Chen, Bangzhu Chen, Chenrui Liu, Pingchang Bai, Bin Huang, Zigan Luo, Mingyu Xie, and Yu Wang, Huawei Cloud; Youyou Lu, Tsinghua University; Huatao Wu, Huawei Cloud; Jiwu Shu, Tsinghua University and Minjiang University

**摘要：** TapeOBS is an archive storage service offered by Huawei Cloud, which delivers high cost-efficiency by leveraging tape to store large volumes of archived data. Although tape boasts a low total cost of ownership, its inherent characteristics (e.g., a limited number of drives within a tape library) pose unique challenges when developing a large-scale distributed storage system. To address these challenges, we take a holistic approach in designing TapeOBS. At the high level, we introduce a fully asynchronous tape pool, which supports data scheduling and erasure coding in a batched manner, aligning with the features of tape hardware. Within a tape library, we design a tape-tailored local storage engine and incorporate techniques such as dedicated drives to optimize performance. TapeOBS began its gradual rollout at the end of 2022 and officially started serving customers in 2024. As of this writing, TapeOBS has stored hundreds of petabytes of raw user data.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### DMTree: Towards Efficient Tree Indexing on Disaggregated Memory via Compute-side Collaborative Design
**作者：** Guoli Wei, University of Science and Technology of China; Yongkun Li, University of Science and Technology of China and Anhui Provincial Key Laboratory of High Performance Computing, USTC; Haoze Song, The University of Hong Kong; Tao Li and Lulu Yao, University of Science and Technology of China; Yinlong Xu, University of Science and Technology of China and Anhui Provincial Key Laboratory of High Performance Computing, USTC; Heming Cui, The University of Hong Kong

**摘要：** Disaggregated memory (DM) separates computing and memory resources into distinct resource pools, enhancing resource utilization and scalability. However, this new architecture presents fundamental design challenges on range indexes. Existing works fail to achieve high performance: they either suffer from the network bandwidth bottleneck or are fragile due to high RDMA IOPS demands. The key reason is that they all follow a typical design paradigm that uses private compute-side caching, where each compute server holds a private cache space and aggressively consumes the bandwidth and IOPS between compute servers and memory servers. We propose a new compute-side collaborative design. It offloads data locating and locking operations from memory servers to compute servers and thus fully utilizes unsaturated RDMA resources between compute servers to mitigate bottlenecks on memory servers. We implement a prototype called DMTree. Experiments show that DMTree outperforms existing state-of-the-art range indexes on DM for both point operations (i.e., searches, inserts, and updates) and range operations (i.e., scans) under various workloads and parameter settings.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### An Efficient Cloud Storage Model with Compacted Metadata Management for Performance Monitoring Timeseries Systems
**作者：** Kai Zhang, The Chinese University of Hong Kong; Tianyu Wang, Shenzhen University; Zili Shao, The Chinese University of Hong Kong

**摘要：** Cloud-based performance monitoring timeseries systems are emerging due to their flexibility and pay-as-you-go capabilities. However, these systems encounter a major bottleneck in query performance, mainly attributed to the prolonged access latency of cloud storage and metadata redundancy of large number of timeseries. Thus, it is critical to optimize query performance within cloud environment and reduce metadata redundancy. In this paper, we propose CloudTS, which is a novel timeseries data storage model with query optimization for cloud storage. CloudTS separately manages metadata and data, and introduces an efficient global metadata management for both space saving and query speedup. CloudTS also transparently supports the time-partitioned tag-based query model in performance monitoring timeseries systems. For metadata, a global tag dictionary is built to reduce metadata redundancy and a novel timeseries-tag mapping technique with a two-dimension bitmap is designed so the mapping of timeseries and tags can be efficiently accomplished to support tag-based queries. For data, the compressed data chunks are put into objects by timeseries group. We have implemented a fully functional prototype of CloudTS and evaluated it with production timeseries data and synthetic workloads based on Amazon S3. In comparison, Cortex, a cloud-based timeseries system widely adopted by industries, and Apache Parquet and JSON Time Series, two representative cloud storage formats, are utilized in the evaluation. Experimental results show that CloudTS can improve query performance by 1.37x on average compared with Cortex, and outperforms Apache Parquet and JSON Time Series as well.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### Getting the MOST out of your Storage Hierarchy with Mirror-Optimized Storage Tiering
**作者：** Kaiwei Tu, University of Wisconsin–Madison; Kan Wu, Google; Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau, University of Wisconsin–Madison

**摘要：** We present Mirror-Optimized Storage Tiering (MOST), a novel tiering-based approach optimized for modern storage hierarchies. The key idea of MOST is to combine the load-balancing advantages of mirroring with the space-efficiency advantages of tiering. Specifically, MOST dynamically mirrors a small amount of hot data across storage tiers to efficiently balance load, avoiding costly migrations. As a result, MOST is as space-efficient as classic tiering while achieving better bandwidth utilization under I/O-intensive workloads. We implement MOST in Cerberus, a user-level storage management layer based on CacheLib. We show the efficacy of Cerberus through a comprehensive empirical study: across a range of static and dynamic workloads, Cerberus achieves better throughput than competing approaches on modern storage hierarchies especially under I/O-intensive and dynamic workloads.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### Rearchitecting Buffered I/O in the Era of High-Bandwidth SSDs
**作者：** Yekang Zhan, Tianze Wang, Zheng Peng, Haichuan Hu, Jiahao Wu, Xiangrui Yang, and Qiang Cao, Huazhong University of Science and Technology; Hong Jiang, University of Texas at Arlington; Jie Yao, Huazhong University of Science and Technology

**摘要：** Buffered I/O via page cache has been prevalently used by applications for decades due to its user-friendliness and high performance. However, the existing buffered I/O architecture fails to effectively utilize high-bandwidth Solid-State Drives (SSDs) caused by 1) costly page caching overused for buffering all incoming writes in the critical path, 2) the limited concurrency of page management, and 3) the high read-before-write penalty for partial-page writes.  This paper rearchitects buffered I/O and proposes a write-scrap buffering approach (WSBuffer) to remove the aforementioned shackles of buffered I/O on writes to proactively exploit fast SSDs while retaining all the advantages of buffered I/O on reads. WSBuffer first presents a novel memory-page buffering structure, scrap buffer, to efficiently buffer SSD-I/O unfriendly writes and expensive partial-page writes. WSBuffer further proposes a buffer-minimized data access mechanism to partially buffer small and unaligned parts of user writes via the scrap buffer while directly sending large and aligned parts to underlying SSDs. Finally, WSBuffer devises an opportunistic two-stage dirty-data flushing mechanism and a concurrent page management mechanism to achieve fluent and fast dirty-data flushing. The experimental results show that WSBuffer outperforms Linux file systems of EXT4, F2FS, BTRFS and XFS, as well as the state-of-the-art buffered I/O optimization of ScaleCache by up to 3.91X and 82.80X in throughput and latency respectively.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### LESS is More for I/O-Efficient Repairs in Erasure-Coded Storage
**作者：** Keyun Cheng, The Chinese University of Hong Kong; Guodong Li, Shandong University; Xiaolu Li, Huazhong University of Science and Technology; Sihuang Hu, Shandong University; Patrick P. C. Lee, The Chinese University of Hong Kong

**摘要：** I/O efficiency is critical for erasure-coded repair performance in modern distributed storage. We propose LESS, a family of repair-friendly erasure code constructions that reduces both the amount of data accessed and the number of I/O seeks in single-block repairs, while ensuring balanced reductions across blocks. LESS layers multiple extended sub-stripes formed by widely deployed Reed-Solomon coding, and is configurable to balance the trade-off between the amount of data accessed and I/O seeks. Evaluation shows that LESS on HDFS reduces both single-block repair and full-node recovery times compared to state-of-the-art I/O-optimal erasure codes.

--------------------------------------------------------------------------------

## Spring Accepted Papers

### Lockify: Understanding Linux Distributed Lock Management Overheads in Shared Storage
**作者：** Taeyoung Park, Yunjae Jo, Daegyu Han, Beomseok Nam, and Jaehyun Hwang, Sungkyunkwan University

**摘要：** This paper presents Lockify, a novel distributed lock manager (DLM) for shared-disk file systems. Our key observation in shared-storage scenarios is that, for file or directory creation, lock acquisition overhead in the Linux kernel DLM increases with the number of clients, even in low-contention scenarios. Lockify minimizes this lock acquisition latency by avoiding unnecessary communication with remote directory nodes through self-owner notifications and asynchronous ownership management. We implement Lockify in the Linux kernel and evaluate its performance on real-world workloads using two representative shared-disk file systems, GFS2 and OCFS2. Our experimental results demonstrate that Lockify improves overall throughput by ~6.4× compared to the kernel DLM and O2CB, consistently across different numbers of clients.

--------------------------------------------------------------------------------

