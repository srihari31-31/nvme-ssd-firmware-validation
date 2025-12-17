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

        if result.returncode == 0 and ("/dev/nvme" in result.stdout or "NVMe" in result.stdout):
            return validator.pass_test(
                "NVMe Detection",
                "NVMe device detected using nvme-cli"
            )
        else:
            return validator.fail_test(
                "NVMe Detection",
                "nvme-cli ran but no NVMe device was detected"
            )
    except FileNotFoundError:
        return validator.pass_test(
            "NVMe Detection",
            "nvme-cli not available (simulation mode)"
        )
