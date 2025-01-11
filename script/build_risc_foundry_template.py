import subprocess
import os
from utils.config import BASE_DIR

subprocess.run(
    [
        'cargo',
        'build',
        '--manifest-path',
        os.path.join(BASE_DIR, 'lib/risc0-foundry-template/Cargo.toml')
    ]
)
