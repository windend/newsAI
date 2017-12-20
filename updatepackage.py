
# 更新python包
import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip3.6 install --upgrade " + dist.project_name, shell=True)
