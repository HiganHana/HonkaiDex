from pprint import pprint

def check_upload_time_20_days_apart():
    import requests
    data =requests.get('https://pypi.python.org/pypi/honkaidex/json').json()
    
    upload_time = list(data["releases"].values())[-1][0]["upload_time"]
    from datetime import datetime
    upload_time = datetime.strptime(upload_time, "%Y-%m-%dT%H:%M:%S")
    now = datetime.now()
    delta = now - upload_time
    if delta.days > 20:
        print("Upload time is more than 20 days ago")
        return True
    else:
        print("Upload time is less than 20 days ago")
        return False

if __name__ == '__main__':
    if not check_upload_time_20_days_apart():
        exit(0)

    # perform scrap job
    import logging
    import sys
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    from hondex_scrap import ScrapJob
    had_changes = ScrapJob.run_all_scraps()


    