from sentence_splitter import SentenceSplitter, split_text_into_sentences


if __name__ == '__main__':

    #
    # Object interface
    #
    splitter = SentenceSplitter(language='en')
    print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
    # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']

    #
    # Functional interface
    #
    print(split_text_into_sentences(
        text='This is a paragraph. It contains several sentences. "But why," you ask?',
        language='en'
    ))
    # ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']