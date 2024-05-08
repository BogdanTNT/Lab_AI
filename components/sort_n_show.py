def sort_n_show(input_texts, scores, threshold = 0.8):
    print(scores)

    # Print the original query for reference
    print("Query:", input_texts[0])

    # Create a list of (score, document) tuples
    score_document_pairs = [(score.item(), input_texts[i+1]) for i, score in enumerate(scores[0])]

    # Sort the list by similarity score in descending order
    sorted_score_document_pairs = sorted(score_document_pairs, key=lambda x: x[0], reverse=True)

    # Iterate through sorted scores and corresponding texts
    for score, document in sorted_score_document_pairs:
        if score > threshold:  # Assuming similarity threshold 
            print(f"Document: {document} \nSimilarity Score: {score:.2f}")