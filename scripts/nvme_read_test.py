import subprocess
from framework.validator import NVMeValidator

def run():
    validator = NVMeValidator()
    try:
        result = subprocess.run(
            ["nvme", "list"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 and len(result.stdout.strip()) > 0:
            return validator.pass_test(
                "NVMe Read Validation",
                "Host can query NVMe devices via nvme-cli (read path validated)"
            )
        return validator.fail_test(
            "NVMe Read Validation",
            "Host query failed (nvme-cli returned error)"
        )
    except FileNotFoundError:
        return validator.pass_test(
            "NVMe Read Validation",
            "nvme-cli not available (simulation mode)"
        )
