import argparse
import glob
import os, sys
from assignment1.main import mask_content
from assignment1.name_detector import detect_names
import warnings
warnings.filterwarnings("ignore")

def write_stats(stats, stats_path):
    '''This function takes the stats variable and write all its contents into given stats_path'''
    if stats_path == 'stderr':
        for key, value in stats.items():
            print(f"{key}: {value}", file=sys.stderr)
    elif stats_path == 'stdout':
        for key, value in stats.items():
            print(f"{key}: {value}", file=sys.stdout)
    else:
        if not os.path.exists(stats_path):
            os.makedirs(os.path.dirname(stats_path), exist_ok=True)
        with open(stats_path, 'w') as file:
            print(stats)
            file.write(str(stats))

def censor_docs(glob_pattern, **kwargs):
    '''This function processes all files that extend matching the glob , returns stats and .censored files'''
    files_list = glob.glob(glob_pattern)
    for file_name in files_list:
        with open(file_name, 'r') as file:
            file_content = file.read()
            stats = dict(file_name = file_name)
            masked_file_content, stats = mask_content(file_content, kwargs.get('concepts'), stats)
        # censored_file_name = file_name + 'censored' if file_name.endswith('.') else file_name + '.censored'
        censored_file_name = file_name + '.censored'
        output_path = kwargs.get('output_dir', '')
        output_path = output_path + '/' if not output_path.endswith('/') else output_path
        censored_file_name = output_path + censored_file_name
        if not os.path.exists(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(censored_file_name, 'w') as file:
            file.write(masked_file_content)
        write_stats(stats, kwargs.get('stats_path'))


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Input file(s) glob pattern', required=True)
    parser.add_argument('--output', type=str, help='Output directory for censored files', required=True)
    parser.add_argument('--names', action='store_true', help='Censor names')
    parser.add_argument('--dates', action='store_true', help='Censor dates')
    parser.add_argument('--phones', action='store_true', help='Censor phone numbers')
    # parser.add_argument('--address', action='store_true', help='Censor addresses')
    parser.add_argument('--concept', action='append', help='<Required> Set flag', required=True)
    parser.add_argument('--stats', type=str, help='File to write statistics', default='stderr')
    args = parser.parse_args()
    kwargs = dict(
                  output_dir = args.output,
                  names = args.names,
                  dates = args.dates,
                  phones = args.phones,
                  concepts = args.concept,
                  stats_path = args.stats)
    censor_docs(args.input, **kwargs)
