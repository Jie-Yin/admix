import argparse
from admix_fraction import admix_fraction
import admix_models

def arguments():
    # argument parser
    parser = argparse.ArgumentParser()
    
    # specify models
    parser.add_argument('-m', '--models',
                        nargs = '+',
                        help = 'specify admixure models for calculation (default: all available models)')

    # save as a file (set the default file name when no argument provided)
    parser.add_argument('-f', '--file',
                        nargs = '?',
                        const = 'admixture_results.txt',
                        help = 'save results as a file')

    return parser.parse_args()

# print out admixure analysis results
def admix_results(models, output_filename, raw_data_format, raw_data_file=None):
    # write results to a file
    if (output_filename is not None):
        f = open(output_filename, 'w')

    for model in models:
        result = 'Model: ' + model + '\n'
        admix_frac = admix_fraction(model, raw_data_format, raw_data_file)
        populations = admix_models.populations(model)
        for (i, frac) in enumerate(admix_frac):
            result += '{:s}: {:.2f}%'.format(populations[i], 100*frac) + '\n'
        result += '\n'

        # print out results
        print(result)

        # write results to file
        if (output_filename is not None):
            f.write(result)

    # close file
    if (output_filename is not None):
        print('Results are written to ' + output_filename)
        f.close()

# arguments
args = arguments()

# set models for calculation
all_models = admix_models.models()
if (args.models is None):
    models = all_models
else:
    models = args.models
    for m in models:
        if not m in all_models:
            print('Cannot find model ' + m + '!')
            exit()

raw_data_format = '23andme'

admix_results(models, args.file, raw_data_format)
