from core.utils import filesystem
import os
from subprocess import (
    STDOUT, check_call, CalledProcessError
)


def run_cmd(cmd: str, shell=False) -> bool:
        """Runs a shell command.
        Runs a shell command using subprocess.
        
        Args:
            cmd (str): The shell command to run.
            shell (bool): Defines either shell should be set to True or False.
        
        Returns:
            bool: Returns True on success and False otherwise
        """
        try:
            if not shell:
                check_call(cmd.split(' '),
                           stdout=open(os.devnull, 'wb'), stderr=STDOUT, timeout=300)
            else:
                check_call(cmd, stdout=open(os.devnull, 'wb'),
                           stderr=STDOUT, shell=True, executable='bash', timeout=300)
            return True
        except CalledProcessError:
            return False

def setup_website(website: object):
    """Setup website.
    
    This function is responsible to setup the website when it's created and it
    restarts the services. Ideally, this function should be called soon after
    the website model is created.
    """
    
    # Create initial directories
    filesystem.create_website_dirs(website)
    
    # Create FPM pool conf
    filesystem.generate_fpm_conf(website)


def delete_website(website: object):
    """Delete website.
    
    This function cleans the website data and it should be called right before
    the website model is about to be deleted.
    """
    
    # Delete website directories
    filesystem.delete_website_dirs(website)
    
    # Delete PHP FPM pool conf
    filesystem.delete_fpm_conf(website)
    
    # Delete NGINX vhost files
    filesystem.delete_nginx_vhost(website)