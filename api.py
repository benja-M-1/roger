import hug
import datetime
import scrapper

@hug.cli()
@hug.get('/slots')
def get_slots():
    return scrapper.get_slots(startAtDate=datetime.date(day=10, month=3, year=2017))

if __name__ == '__main__':
    add.interface.cli()
