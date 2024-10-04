# desktop cleaner.

import datetime
import pathlib
import shutil
import tqdm

source_dir = pathlib.Path.home() / 'Desktop'

for x in tqdm.tqdm([x for x in source_dir.iterdir()]):
    if x.is_file():
        ctime = datetime.datetime.fromtimestamp(x.stat().st_ctime).strftime('%Y%m%d')
        new_path = pathlib.Path.home() / 'Documents' / ctime / x.name
        new_path.parents[0].mkdir(exist_ok=True)
        shutil.move(x, new_path)
    elif x.is_dir():
        sub_files = [f for f in x.rglob('*')]
        sub_files = [datetime.datetime.fromtimestamp(f.stat().st_ctime) for f in sub_files]
        if not len(sub_files):
            raise Exception(f'{x} is an empty directory.')
        ctime = min(sub_files).strftime('%Y%m%d')
        new_path = pathlib.Path.home() / 'Documents' / ctime / x.name
        shutil.move(x, new_path)
    else:
        raise Exception('This should not happen.')