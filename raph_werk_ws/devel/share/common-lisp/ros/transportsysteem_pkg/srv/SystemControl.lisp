; Auto-generated. Do not edit!


(cl:in-package transportsysteem_pkg-srv)


;//! \htmlinclude SystemControl-request.msg.html

(cl:defclass <SystemControl-request> (roslisp-msg-protocol:ros-message)
  ((instruction
    :reader instruction
    :initarg :instruction
    :type cl:string
    :initform ""))
)

(cl:defclass SystemControl-request (<SystemControl-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SystemControl-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SystemControl-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name transportsysteem_pkg-srv:<SystemControl-request> is deprecated: use transportsysteem_pkg-srv:SystemControl-request instead.")))

(cl:ensure-generic-function 'instruction-val :lambda-list '(m))
(cl:defmethod instruction-val ((m <SystemControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader transportsysteem_pkg-srv:instruction-val is deprecated.  Use transportsysteem_pkg-srv:instruction instead.")
  (instruction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SystemControl-request>) ostream)
  "Serializes a message object of type '<SystemControl-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'instruction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'instruction))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SystemControl-request>) istream)
  "Deserializes a message object of type '<SystemControl-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'instruction) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'instruction) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SystemControl-request>)))
  "Returns string type for a service object of type '<SystemControl-request>"
  "transportsysteem_pkg/SystemControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SystemControl-request)))
  "Returns string type for a service object of type 'SystemControl-request"
  "transportsysteem_pkg/SystemControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SystemControl-request>)))
  "Returns md5sum for a message object of type '<SystemControl-request>"
  "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SystemControl-request)))
  "Returns md5sum for a message object of type 'SystemControl-request"
  "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SystemControl-request>)))
  "Returns full string definition for message of type '<SystemControl-request>"
  (cl:format cl:nil "# Request: The state the system should go to (\"start\", \"dump\")~%string instruction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SystemControl-request)))
  "Returns full string definition for message of type 'SystemControl-request"
  (cl:format cl:nil "# Request: The state the system should go to (\"start\", \"dump\")~%string instruction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SystemControl-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'instruction))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SystemControl-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SystemControl-request
    (cl:cons ':instruction (instruction msg))
))
;//! \htmlinclude SystemControl-response.msg.html

(cl:defclass <SystemControl-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SystemControl-response (<SystemControl-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SystemControl-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SystemControl-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name transportsysteem_pkg-srv:<SystemControl-response> is deprecated: use transportsysteem_pkg-srv:SystemControl-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <SystemControl-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader transportsysteem_pkg-srv:result-val is deprecated.  Use transportsysteem_pkg-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SystemControl-response>) ostream)
  "Serializes a message object of type '<SystemControl-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SystemControl-response>) istream)
  "Deserializes a message object of type '<SystemControl-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SystemControl-response>)))
  "Returns string type for a service object of type '<SystemControl-response>"
  "transportsysteem_pkg/SystemControlResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SystemControl-response)))
  "Returns string type for a service object of type 'SystemControl-response"
  "transportsysteem_pkg/SystemControlResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SystemControl-response>)))
  "Returns md5sum for a message object of type '<SystemControl-response>"
  "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SystemControl-response)))
  "Returns md5sum for a message object of type 'SystemControl-response"
  "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SystemControl-response>)))
  "Returns full string definition for message of type '<SystemControl-response>"
  (cl:format cl:nil "# Response: Whether the state transition was successfully executed~%bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SystemControl-response)))
  "Returns full string definition for message of type 'SystemControl-response"
  (cl:format cl:nil "# Response: Whether the state transition was successfully executed~%bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SystemControl-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SystemControl-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SystemControl-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SystemControl)))
  'SystemControl-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SystemControl)))
  'SystemControl-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SystemControl)))
  "Returns string type for a service object of type '<SystemControl>"
  "transportsysteem_pkg/SystemControl")