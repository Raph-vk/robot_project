; Auto-generated. Do not edit!


(cl:in-package transportsysteem_pkg-srv)


;//! \htmlinclude ControlState-request.msg.html

(cl:defclass <ControlState-request> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:string
    :initform ""))
)

(cl:defclass ControlState-request (<ControlState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name transportsysteem_pkg-srv:<ControlState-request> is deprecated: use transportsysteem_pkg-srv:ControlState-request instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <ControlState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader transportsysteem_pkg-srv:state-val is deprecated.  Use transportsysteem_pkg-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlState-request>) ostream)
  "Serializes a message object of type '<ControlState-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlState-request>) istream)
  "Deserializes a message object of type '<ControlState-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlState-request>)))
  "Returns string type for a service object of type '<ControlState-request>"
  "transportsysteem_pkg/ControlStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlState-request)))
  "Returns string type for a service object of type 'ControlState-request"
  "transportsysteem_pkg/ControlStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlState-request>)))
  "Returns md5sum for a message object of type '<ControlState-request>"
  "ba7d0f17aa81fce463f555ebbb18949e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlState-request)))
  "Returns md5sum for a message object of type 'ControlState-request"
  "ba7d0f17aa81fce463f555ebbb18949e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlState-request>)))
  "Returns full string definition for message of type '<ControlState-request>"
  (cl:format cl:nil "# Request: The state the system should go to (\"start\", \"wait\", \"dump\")~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlState-request)))
  "Returns full string definition for message of type 'ControlState-request"
  (cl:format cl:nil "# Request: The state the system should go to (\"start\", \"wait\", \"dump\")~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlState-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlState-request
    (cl:cons ':state (state msg))
))
;//! \htmlinclude ControlState-response.msg.html

(cl:defclass <ControlState-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ControlState-response (<ControlState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ControlState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ControlState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name transportsysteem_pkg-srv:<ControlState-response> is deprecated: use transportsysteem_pkg-srv:ControlState-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ControlState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader transportsysteem_pkg-srv:success-val is deprecated.  Use transportsysteem_pkg-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ControlState-response>) ostream)
  "Serializes a message object of type '<ControlState-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ControlState-response>) istream)
  "Deserializes a message object of type '<ControlState-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ControlState-response>)))
  "Returns string type for a service object of type '<ControlState-response>"
  "transportsysteem_pkg/ControlStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlState-response)))
  "Returns string type for a service object of type 'ControlState-response"
  "transportsysteem_pkg/ControlStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ControlState-response>)))
  "Returns md5sum for a message object of type '<ControlState-response>"
  "ba7d0f17aa81fce463f555ebbb18949e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ControlState-response)))
  "Returns md5sum for a message object of type 'ControlState-response"
  "ba7d0f17aa81fce463f555ebbb18949e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ControlState-response>)))
  "Returns full string definition for message of type '<ControlState-response>"
  (cl:format cl:nil "# Response: Whether the state transition was successfully executed~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ControlState-response)))
  "Returns full string definition for message of type 'ControlState-response"
  (cl:format cl:nil "# Response: Whether the state transition was successfully executed~%bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ControlState-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ControlState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ControlState-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ControlState)))
  'ControlState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ControlState)))
  'ControlState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ControlState)))
  "Returns string type for a service object of type '<ControlState>"
  "transportsysteem_pkg/ControlState")