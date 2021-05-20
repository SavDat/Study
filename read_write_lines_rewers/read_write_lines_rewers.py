with  open('dataset_24465_4.txt') as f, open('test_copy_1.txt', 'w') as w:
    x = f.read().splitlines()
    for i in x[::-1]:
        w.write(i+'\n')
