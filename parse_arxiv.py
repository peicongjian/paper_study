
import xml.etree.ElementTree as ET
import csv
import os

def parse_arxiv_results(xml_content, output_file):
    root = ET.fromstring(xml_content)
    
    papers = []
    
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        try:
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            
            # 查找 PDF 下载链接
            pdf_link = None
            for link in entry.findall("{http://www.w3.org/2005/Atom}link"):
                if link.get("title") == "pdf":
                    pdf_link = link.get("href")
            
            # 检查是否有有效的链接
            if pdf_link:
                papers.append({"Title": title, "Download Link": pdf_link})
        
        except Exception as e:
            print(f"Error parsing entry: {e}")
            continue
    
    # 保存到 CSV 文件
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Title", "Download Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)
    
    print(f"Found {len(papers)} papers. Saved to {output_file}")

if __name__ == "__main__":
    # 创建输出目录
    output_dir = "paper-2026-02"
    os.makedirs(output_dir, exist_ok=True)
    
    # 从文件中读取 XML 内容（如果文件不存在，使用上面的原始内容）
    xml_file = "arxiv_results.xml"
    if os.path.exists(xml_file):
        with open(xml_file, "r", encoding="utf-8") as f:
            xml_content = f.read()
    else:
        xml_content = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns="http://www.w3.org/2005/Atom">
  <id>https://arxiv.org/api/R0vm0jngxQs61T5C/VOxov0sjm0</id>
  <title>arXiv Query: search_query=all:SSD AND all:AI AND all:infrastructure&amp;id_list=&amp;start=0&amp;max_results=20</title>
  <updated>2026-02-13T07:18:21Z</updated>
  <link href="https://arxiv.org/api/query?search_query=all:SSD+AND+(all:AI+AND+all:infrastructure)&amp;start=0&amp;max_results=20&amp;id_list=" type="application/atom+xml"/>
  <opensearch:itemsPerPage>20</opensearch:itemsPerPage>
  <opensearch:totalResults>3</opensearch:totalResults>
  <opensearch:startIndex>0</opensearch:startIndex>
  <entry>
    <id>http://arxiv.org/abs/2602.08226v1</id>
    <title>ByteHouse: A Cloud-Native OLAP Engine with Incremental Computation and Multi-Modal Retrieval</title>
    <updated>2026-02-09T03:01:00Z</updated>
    <link href="https://arxiv.org/abs/2602.08226v1" rel="alternate" type="text/html"/>
    <link href="https://arxiv.org/pdf/2602.08226v1" rel="related" type="application/pdf" title="pdf"/>
    <summary>With the rapid rise of intelligent data services, modern enterprises increasingly require efficient, multimodal, and cost-effective data analytics infrastructures. However, in ByteDance's production environments, existing systems fall short due to limitations such as I/O-inefficient multimodal storage, inflexible query optimization (e.g., failing to optimize multimodal access patterns), and performance degradation caused by resource disaggregation (e.g., loss of data locality in remote storage). To address these challenges, we introduce ByteHouse (https://bytehouse.cloud), a cloud-native data warehouse designed for real-time multimodal data analytics. The storage layer integrates a unified table engine that provides a two-tier logical abstraction and physically consistent layout, SSD-backed cluster-scale cache (CrossCache) that supports shared caching across compute nodes, and virtual file system (NexusFS) that enable efficient local access on compute nodes. The compute layer supports analytical, batch, and incremental execution modes, with tailored optimizations for hybrid queries (e.g., runtime filtering over tiered vector indexes). The control layer coordinates global metadata and transactions, and features an effective optimizer enhanced by historical execution traces and AI-assisted plan selection. Evaluations on internal and standard workloads show that ByteHouse achieves significant efficiency improvement over existing systems.</summary>
    <category term="cs.DB" scheme="http://arxiv.org/schemas/atom"/>
    <published>2026-02-09T03:01:00Z</published>
    <arxiv:primary_category term="cs.DB"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2409.16576v1</id>
    <title>FusionANNS: An Efficient CPU/GPU Cooperative Processing Architecture for Billion-scale Approximate Nearest Neighbor Search</title>
    <updated>2024-09-25T03:14:01Z</updated>
    <link href="https://arxiv.org/abs/2409.16576v1" rel="alternate" type="text/html"/>
    <link href="https://arxiv.org/pdf/2409.16576v1" rel="related" type="application/pdf" title="pdf"/>
    <summary>Approximate nearest neighbor search (ANNS) has emerged as a crucial component of database and AI infrastructure. Ever-increasing vector datasets pose significant challenges in terms of performance, cost, and accuracy for ANNS services. None of modern ANNS systems can address these issues simultaneously. We present FusionANNS, a high-throughput, low-latency, cost-efficient, and high-accuracy ANNS system for billion-scale datasets using SSDs and only one entry-level GPU. The key idea of FusionANNS lies in CPU/GPU collaborative filtering and re-ranking mechanisms, which significantly reduce I/O operations across CPUs, GPU, and SSDs to break through the I/O performance bottleneck. Specifically, we propose three novel designs: (1) multi-tiered indexing to avoid data swapping between CPUs and GPU, (2) heuristic re-ranking to eliminate unnecessary I/Os and computations while guaranteeing high accuracy, and (3) redundant-aware I/O deduplication to further improve I/O efficiency. We implement FusionANNS and compare it with the state-of-the-art SSD-based ANNS system -- SPANN and GPU-accelerated in-memory ANNS system -- RUMMY. Experimental results show that FusionANNS achieves 1) 9.4-13.1X higher query per second (QPS) and 5.7-8.8X higher cost efficiency compared with SPANN; 2) and 2-4.9X higher QPS and 2.3-6.8X higher cost efficiency compared with RUMMY, while guaranteeing low latency and high accuracy.</summary>
    <category term="cs.IR" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.DB" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.OS" scheme="http://arxiv.org/schemas/atom"/>
    <published>2024-09-25T03:14:01Z</published>
    <arxiv:primary_category term="cs.IR"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2104.05158v7</id>
    <title>Software-Hardware Co-design for Fast and Scalable Training of Deep Learning Recommendation Models</title>
    <updated>2023-02-27T00:21:53Z</updated>
    <link href="https://arxiv.org/abs/2104.05158v7" rel="alternate" type="text/html"/>
    <link href="https://arxiv.org/pdf/2104.05158v7" rel="related" type="application/pdf" title="pdf"/>
    <summary>Deep learning recommendation models (DLRMs) are used across many business-critical services at Facebook and are the single largest AI application in terms of infrastructure demand in its data-centers. In this paper we discuss the SW/HW co-designed solution for high-performance distributed training of large-scale DLRMs. We introduce a high-performance scalable software stack based on PyTorch and pair it with the new evolution of Zion platform, namely ZionEX. We demonstrate the capability to train very large DLRMs with up to 12 Trillion parameters and show that we can attain 40X speedup in terms of time to solution over previous systems. We achieve this by (i) designing the ZionEX platform with dedicated scale-out network, provisioned with high bandwidth, optimal topology and efficient transport (ii) implementing an optimized PyTorch-based training stack supporting both model and data parallelism (iii) developing sharding algorithms capable of hierarchical partitioning of the embedding tables along row, column dimensions and load balancing them across multiple workers; (iv) adding high-performance core operators while retaining flexibility to support optimizers with fully deterministic updates (v) leveraging reduced precision communications, multi-level memory hierarchy (HBM+DDR+SSD) and pipelining. Furthermore, we develop and briefly comment on distributed data ingestion and other supporting services that are required for the robust and efficient end-to-end training in production environments.</summary>
    <category term="cs.DC" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.PF" scheme="http://arxiv.org/schemas/atom"/>
    <published>2021-04-12T02:15:55Z</published>
    <arxiv:primary_category term="cs.DC"/>
  </entry>
</feed>"""
    
    # 输出文件名
    output_file = os.path.join(output_dir, "papers.csv")
    
    # 解析并保存结果
    parse_arxiv_results(xml_content, output_file)
