import hug

@hug.cli()
@hug.get('/slots')
def get_slots():
    return open('./data/sample.json').read()

if __name__ == '__main__':
    add.interface.cli()
