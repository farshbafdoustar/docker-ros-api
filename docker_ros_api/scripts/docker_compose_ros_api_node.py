#!/usr/bin/env python

import docker
import rospy
import compose.cli.main as docker_compose_main
import compose.cli.signals
import sys

def _ignore_sigpipe():
    return
def _set_signal_handler(handler):
    return
def _set_signal_handler_to_hang_up():
    return

compose.cli.signals.ignore_sigpipe=_ignore_sigpipe
compose.cli.signals.set_signal_handler=_set_signal_handler
compose.cli.signals.set_signal_handler_to_hang_up=_set_signal_handler_to_hang_up


from docker_ros_api_msgs.srv import (RunComposeCommand,
                                     RunComposeCommandResponse)

def run_compose_command_callback(request):
    # client = docker.from_env()
    # container = client.containers.run(req.container_name, detach=req.detach)
    response=RunComposeCommandResponse()
    response.error_code=SUCCESSFULL
    
    sys.argv=["docker-compose","-f",request.compose_file,"--env-file",request.env_file]
    if request.command==request.UP_COMMAND:
        sys.argv.append("up")
        sys.argv.append("--detach")
        sys.argv.append(req.service_name)
    elif request.command==request.STOP_COMMAND:
        sys.argv.append("stop")
        sys.argv.append(request.service_name)
    else :
        request.error_code=response.COMMAND_NOT_SUPPORTED
        return response


    
    try:
        docker_compose_main.main()
    except SystemExit as e:
        print(e.code)
        if isinstance(e.code,int): 
            response.error_code=e.code
        else:
            response.error_code=response.COMMAND_ERROR
    #TODO: Later use docker compose file in param and get name of service from container and use docker api and get and return other info
    return response


def main(args=None):
    rospy.init_node('docker_compose_ros_api_node')
    s = rospy.Service('~compose', RunComposeCommand, run_compose_command_callback)
    print("Docker ROS API server started.")
    rospy.spin()

if __name__ == "__main__":
    main()
