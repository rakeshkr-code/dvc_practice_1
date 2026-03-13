def main():
    # read txt file and print it
    with open('data/myfile.txt', 'r') as f:
        content = f.read()
        print(content)

if __name__ == '__main__':
    main()