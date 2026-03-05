from rank_bm25 import BM25Okapi
import numpy as np

class HybridRetriever:
    def __init__(self, vectorstore, documents):
        self.vectorstore = vectorstore
        self.documents = documents
        
        # Prepare BM25
        self.tokenized_docs = [doc.page_content.split() for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)
    
    def retrieve(self, query, k=5):
        
        # Vector similarity search
        vector_docs = self.vectorstore.similarity_search(query, k=k)
        
        # BM25 keyword search
        tokenized_query = query.split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        top_n = np.argsort(bm25_scores)[-k:]
        
        keyword_docs = [self.documents[i] for i in top_n]
        
        # Combine and remove duplicates
        combined = vector_docs + keyword_docs
        
        unique_docs = []
        seen = set()
        
        for doc in combined:
            content = doc.page_content
            if content not in seen:
                seen.add(content)
                unique_docs.append(doc)
        
        return unique_docs