#Twelve Days of Christmas

verses = ['And partridge on a pear tree', 'Two turtle doves', 'Three French hens', 'Four calling birds', 'Five gold rings', 'Six geese a-laying', 'Seven swans a-swimming', 'Eight maid a-milking', 'Nine ladies dancing','Ten lords a-leaping','Eleven pipers piping','Twelve drummers drumming']
ordinal_nums = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
def verse(num):
    print(f'''
On the {ordinal_nums[num - 1]} day of Christmas
my true love sent to me:
''', end='')
    if num == 1:
        print('A partridge on a pear tree')
    else:
        print(verses[num - 1])#this is because the first index is 0, not 1
        for i in range(num - 1): #we are going to go up to verse -1 so we don't repeat the verse we already did.
            print(verses[num - i - 2]) #since we want to go down the the last verse. We want to subtract 2 otherwise it wouldn't include it, and instead just do the 1 and 2 which is actually meant to be 0 and 1 since we are using a list after all.

if __name__ == '__main__':
    def main():
        verse_num = int(input("Verse Number: "))
        verse(verse_num)
        for i in range(12):
            verse(i + 1)
    main()