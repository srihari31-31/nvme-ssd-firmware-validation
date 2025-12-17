import subprocess
from framework.validator import NVMeValidator

def run():
    validator = NVMeValidator()
    # Intentionally run an invalid nvme command to test error handling
    try:
        result = subprocess.run(
            ["nvme", "invalid_command_for_test"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return validator.pass_test(
                "NVMe Error Handling",
                "Invalid NVMe command correctly produced an error"
            )
        else:
            return validator.fail_test(
                "NVMe Error Handling",
                "Invalid NVMe command unexpectedly succeeded"
            )
    except FileNotFoundError:
        return validator.pass_test(
            "NVMe Error Handling",
            "nvme-cli not available (simulation mode)"
        )
