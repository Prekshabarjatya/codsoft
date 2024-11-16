import secrets

def generate_passphrase(num_words, wordlist_path=r'diceware.wordlist.asc'):

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for _ in range(num_words)]
    return ' '.join(words)
n = int(input("Enter the number of words you want in the passphrase: "))
if __name__ == '__main__':
    print(f'Generated passphrase is: {generate_passphrase(n)} ')
