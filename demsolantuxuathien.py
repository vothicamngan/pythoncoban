def count_word_occurrences(text, word):
    count  = 0
    words = text.split()
    print(words)
    for item in words:
        item.split()
        for i in  item:
            if i ==word:
                count += 1
    return count

# Ví dụ văn bản
sample_text = "This is a sample text. The text may contain repeated words."
search_word = input("Nhập từ cần đếm: ")
occurrences = count_word_occurrences(sample_text, search_word)
print(f"Từ '{search_word}' xuất hiện {occurrences} lần trong văn bản.")