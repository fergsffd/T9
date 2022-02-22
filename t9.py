
import sys
import helper
import gold

def parse_content(content):
    print('== My parse_content ==')
    items = content.split('\n')
    ans = dict()
    for item in items:
        key_idx = item.find(' ')
        value = item[key_idx:].strip()
        ans.update({item[:key_idx]:value})
    return ans

def make_tree(words):
    print('== My make_tree ==')
    ans = dict()
    for word, word_freq in words.items():
        for letter in word:
            if ans.has_key(letter):
    return {}

def predict(tree, numbers):
    print('== My parse_content ==')
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')
    my_run_level = len(sys.argv)
    if my_run_level > 1:
        words = gold.parse_content(content)
    else:
        words = parse_content(content)

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    #words = parse_content(content)
    #input('words: ' + str(words))

    # PART 2: Building a trie from a collection of words.
    tree = gold.make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        if my_run_level > 3:
            predictions = gold.predict(tree, numbers)
        else:
            predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
