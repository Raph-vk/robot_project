; Auto-generated. Do not edit!


(cl:in-package robotarm-msg)


;//! \htmlinclude manipulatorFeedback.msg.html

(cl:defclass <manipulatorFeedback> (roslisp-msg-protocol:ros-message)
  ((tandenborstel_opgepakt
    :reader tandenborstel_opgepakt
    :initarg :tandenborstel_opgepakt
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass manipulatorFeedback (<manipulatorFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <manipulatorFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'manipulatorFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robotarm-msg:<manipulatorFeedback> is deprecated: use robotarm-msg:manipulatorFeedback instead.")))

(cl:ensure-generic-function 'tandenborstel_opgepakt-val :lambda-list '(m))
(cl:defmethod tandenborstel_opgepakt-val ((m <manipulatorFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotarm-msg:tandenborstel_opgepakt-val is deprecated.  Use robotarm-msg:tandenborstel_opgepakt instead.")
  (tandenborstel_opgepakt m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <manipulatorFeedback>) ostream)
  "Serializes a message object of type '<manipulatorFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'tandenborstel_opgepakt) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <manipulatorFeedback>) istream)
  "Deserializes a message object of type '<manipulatorFeedback>"
    (cl:setf (cl:slot-value msg 'tandenborstel_opgepakt) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<manipulatorFeedback>)))
  "Returns string type for a message object of type '<manipulatorFeedback>"
  "robotarm/manipulatorFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'manipulatorFeedback)))
  "Returns string type for a message object of type 'manipulatorFeedback"
  "robotarm/manipulatorFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<manipulatorFeedback>)))
  "Returns md5sum for a message object of type '<manipulatorFeedback>"
  "13244125ac2eb6e745592ab638bae6b5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'manipulatorFeedback)))
  "Returns md5sum for a message object of type 'manipulatorFeedback"
  "13244125ac2eb6e745592ab638bae6b5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<manipulatorFeedback>)))
  "Returns full string definition for message of type '<manipulatorFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%bool tandenborstel_opgepakt~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'manipulatorFeedback)))
  "Returns full string definition for message of type 'manipulatorFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%bool tandenborstel_opgepakt~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <manipulatorFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <manipulatorFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'manipulatorFeedback
    (cl:cons ':tandenborstel_opgepakt (tandenborstel_opgepakt msg))
))
