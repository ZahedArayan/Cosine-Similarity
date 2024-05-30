#creatiing document
documents = {
    1: {'t1': 3,'t2':4},
    2: {'t1': 2,'t2':5},
    3: {'t1': 0,'t2':1},
    4: {'t1': 7,'t2':2}
}

#length of documents
lengths = {
    1: 3.0,
    2: 2.236,
    3: 4.0,
    4:2.0
}


#weight of queries
query_weights = {
    't1': 1,
    't2': 1
}


#function for comouting cosine similarity of documents

def compute_cosine_scores(documents, query_weights, lengths):
    scores = {doc_id: 0 for doc_id in documents} 

    for term, w_tq in query_weights.items():
        for doc_id, tf_td in [(doc_id, doc.get(term, 0)) for doc_id, doc in documents.items()]:
            scores[doc_id] += tf_td * w_tq


    for doc_id in scores:
        scores[doc_id] = scores[doc_id] /  lengths[doc_id]

    return scores



scores = compute_cosine_scores(documents, query_weights, lengths)


#number of documents that should be returned 
K = 3
top_k_documents = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:K]



print("Top K documents:", top_k_documents)
