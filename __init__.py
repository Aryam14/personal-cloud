# __all__ = ["user_controller", "product_controller"]

# can also use this to automatically add the files to the __all__ list.

import os
import glob
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]