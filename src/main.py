from configuration.main import configuration
from stages.first import main as first_stage
from stages.second import main as second_stage
from stages.third import main as third_stage

def main():
    data = {
        'first_stage': 'not_completed',
        'second_stage': 'not_completed',
    }

    while True:
        # Runs a function that will setup the program
        configuration()

        # Checks if the first stage has been completed
        if data['first_stage'] != 'completed':
            # Execute Stage I
            status = first_stage()

            # Checks if the first stage has been completed
            if status == 'completed': 
                data['first_stage'] = 'completed'
                data['second_stage'] = 'completed'
                continue
            # Checks if the first stage has failed because there are no files detected in the directory
            elif status == 'not_found':
                data['first_stage'] = 'completed'
                data['second_stage'] = 'not_completed'
            
        
        # Checks if the second stage has been completed
        if data['second_stage'] != 'completed':
            # Execute Stage II
            status = second_stage()

            # Checks if the second stage has been completed
            if status == 'completed':
                data['second_stage'] = 'completed'
            continue

        # Execute Stage III - Will always run if the first and second stages are completed
        third_stage()

main()