import helper
import gold

def parse_content(content):
    items = content.split('\n')
    ans = dict()
    for item in items:
        key_val = item.split(' ')
        ans.update({key_val[0]:key_val[1]})
    return ans

def make_tree(words):
    return {}

def predict(tree, numbers):
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = gold.parse_content(content)
    input('words: ' + str(words))

    # PART 2: Building a trie from a collection of words.
    tree = gold.make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = gold.predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
