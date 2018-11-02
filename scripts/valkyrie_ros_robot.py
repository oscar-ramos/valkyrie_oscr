import numpy as np

import rospy
from oscr.ros_robot import RosRobot
from oscr.ros_kine_sim import RosKineSim


class ValkyrieRosRobot(RosRobot):
    """
    Helper class for the Valkyrie robot in ROS (and RViz)

    """

    def __init__(self, node_name, freq, fbase, backend):
        """
        Constructor. It sets the reduced Valkyrie model (32 dofs) and adds
        specific Valkyrie properties to the joint state publisher

        """
        pkg = 'valkyrie_oscr'
        # Reduced Valkyrie model with 32 dofs
        robot_model = '/urdf/valkyrie_sim_red.urdf'
        RosRobot.__init__(self, node_name, pkg, robot_model,
                          freq, fbase, backend)
        # Add joint names for the fingers
        finger_names = (
            'leftIndexFingerPitch1', 'leftIndexFingerPitch2',
            'leftIndexFingerPitch3', 'leftMiddleFingerPitch1',
            'leftMiddleFingerPitch2', 'leftMiddleFingerPitch3',
            'leftPinkyPitch1', 'leftPinkyPitch2', 'leftPinkyPitch3',
            'leftThumbRoll', 'leftThumbPitch1', 'leftThumbPitch2',
            'leftThumbPitch3', 'rightIndexFingerPitch1',
            'rightIndexFingerPitch2', 'rightIndexFingerPitch3',
            'rightMiddleFingerPitch1', 'rightMiddleFingerPitch2',
            'rightMiddleFingerPitch3', 'rightPinkyPitch1', 'rightPinkyPitch2',
            'rightPinkyPitch3', 'rightThumbRoll', 'rightThumbPitch1',
            'rightThumbPitch2', 'rightThumbPitch3',
            'hokuyo_joint')
        self.joint_pub.appendJointNames(finger_names)
        # Set finger values to zero
        self.qextras = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]])
        self.qextras = self.qextras.T


class ValkyrieRosKineSim(RosKineSim):

    def __init__(self, node_name, freq, fbase, backend, type_robot='rviz',
                 show_markers=True):

        pkg = 'valkyrie_oscr'
        # Reduced Valkyrie model with 32 dofs
        robot_model = '/urdf/valkyrie_sim_red.urdf'
        RosKineSim.__init__(self, node_name, pkg, robot_model, freq, fbase,
                            backend, type_robot, show_markers)
        
        # Add joint names for the fingers
        finger_names = (
            'leftIndexFingerPitch1', 'leftIndexFingerPitch2',
            'leftIndexFingerPitch3', 'leftMiddleFingerPitch1',
            'leftMiddleFingerPitch2', 'leftMiddleFingerPitch3',
            'leftPinkyPitch1', 'leftPinkyPitch2', 'leftPinkyPitch3',
            'leftThumbRoll', 'leftThumbPitch1', 'leftThumbPitch2',
            'leftThumbPitch3', 'rightIndexFingerPitch1',
            'rightIndexFingerPitch2', 'rightIndexFingerPitch3',
            'rightMiddleFingerPitch1', 'rightMiddleFingerPitch2',
            'rightMiddleFingerPitch3', 'rightPinkyPitch1', 'rightPinkyPitch2',
            'rightPinkyPitch3', 'rightThumbRoll', 'rightThumbPitch1',
            'rightThumbPitch2', 'rightThumbPitch3',
            'hokuyo_joint')
        self.robot.joint_pub.appendJointNames(finger_names)
        # Set finger values to zero
        self.qextras = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]])
        self.robot.qextras = self.qextras.T
       
