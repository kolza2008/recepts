from typing import *

def callback(callback_func: Callable[..., None]) -> Callable[..., None]:
    def save_callback_decor(main_func):
        def save_callback_func(**args):
            average = main_func(**args)
            callback_func(average)
        return save_callback_func
    return save_callback_decor
        
