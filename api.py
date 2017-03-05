import hug
import datetime
import scrapper

@hug.cli()
@hug.get('/slots')
def get_slots():
    return scrapper.get_slots(startAtDate=datetime.date.today())

if __name__ == '__main__':
    add.interface.cli()
