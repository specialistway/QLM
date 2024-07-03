import math
from collections import defaultdict
import json
# 示例词频字典
input_file = 'vector_dict.json'
with open(input_file, 'r', encoding='utf-8') as f:
    term_doc_dict = json.load(f)

# 文档长度字典
with open('length.json', 'r', encoding='utf-8') as f:
    doc_lengths = json.load(f)

# 词汇表大小
vocab_size = len(term_doc_dict)
# 平滑参数
mu = 2000

# 示例查询

#query_terms = ["韩国", "首尔"]

# 计算查询在每个文档下的似然概率（使用Dirichlet平滑）
def calculate_query_likelihood(term_freq_dict, query_terms, doc_lengths, vocab_size, mu):
    doc_likelihood = defaultdict(float)
    total_term_freq = sum([sum(term_data["term_freq"].values()) for term_data in term_freq_dict.values()])

    for doc_id in doc_lengths.keys():
        likelihood = 0.0#初始化当前文档的似然值
        doc_length = doc_lengths[doc_id]#获取当前文档的总词数
        for term in query_terms:
            term_freq = term_freq_dict.get(term, {}).get("term_freq", {}).get(doc_id, 0)#获取当前文档中该词的频率
            collection_term_freq = sum(term_freq_dict.get(term, {}).get("term_freq", {}).values())#语料库中该词的总频率
            term_prob = (term_freq + mu * (collection_term_freq / total_term_freq)) / (doc_length + mu)# 计算Dirichlet平滑后的概率
            #
            likelihood += math.log(term_prob)
        doc_likelihood[doc_id] = likelihood

    return doc_likelihood
while(True):



    print("Please enter the key words")
    query_terms = input().strip().split()
    # 获取查询似然概率，并进行排序
    query_likelihood = calculate_query_likelihood(term_doc_dict, query_terms, doc_lengths, vocab_size, mu)
    sorted_query_likelihood = sorted(query_likelihood.items(), key=lambda x: x[1], reverse=True)
    # 只输出前10个相关的文档
    top_10_likelihood = sorted_query_likelihood[:10]

    # 打印排序结果
    print("Query Likelihood Model Ranking:")
    for doc_id, likelihood in top_10_likelihood:
        print(f"Document ID: {doc_id}, Likelihood: {likelihood:.6f}")
