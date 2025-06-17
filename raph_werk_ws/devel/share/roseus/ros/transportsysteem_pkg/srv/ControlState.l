;; Auto-generated. Do not edit!


(when (boundp 'transportsysteem_pkg::ControlState)
  (if (not (find-package "TRANSPORTSYSTEEM_PKG"))
    (make-package "TRANSPORTSYSTEEM_PKG"))
  (shadow 'ControlState (find-package "TRANSPORTSYSTEEM_PKG")))
(unless (find-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATE")
  (make-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATE"))
(unless (find-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATEREQUEST")
  (make-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATEREQUEST"))
(unless (find-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATERESPONSE")
  (make-package "TRANSPORTSYSTEEM_PKG::CONTROLSTATERESPONSE"))

(in-package "ROS")





(defclass transportsysteem_pkg::ControlStateRequest
  :super ros::object
  :slots (_state ))

(defmethod transportsysteem_pkg::ControlStateRequest
  (:init
   (&key
    ((:state __state) "")
    )
   (send-super :init)
   (setq _state (string __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass transportsysteem_pkg::ControlStateResponse
  :super ros::object
  :slots (_success ))

(defmethod transportsysteem_pkg::ControlStateResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass transportsysteem_pkg::ControlState
  :super ros::object
  :slots ())

(setf (get transportsysteem_pkg::ControlState :md5sum-) "ba7d0f17aa81fce463f555ebbb18949e")
(setf (get transportsysteem_pkg::ControlState :datatype-) "transportsysteem_pkg/ControlState")
(setf (get transportsysteem_pkg::ControlState :request) transportsysteem_pkg::ControlStateRequest)
(setf (get transportsysteem_pkg::ControlState :response) transportsysteem_pkg::ControlStateResponse)

(defmethod transportsysteem_pkg::ControlStateRequest
  (:response () (instance transportsysteem_pkg::ControlStateResponse :init)))

(setf (get transportsysteem_pkg::ControlStateRequest :md5sum-) "ba7d0f17aa81fce463f555ebbb18949e")
(setf (get transportsysteem_pkg::ControlStateRequest :datatype-) "transportsysteem_pkg/ControlStateRequest")
(setf (get transportsysteem_pkg::ControlStateRequest :definition-)
      "# Request: The state the system should go to (\"start\", \"wait\", \"dump\")
string state
---
# Response: Whether the state transition was successfully executed
bool success
")

(setf (get transportsysteem_pkg::ControlStateResponse :md5sum-) "ba7d0f17aa81fce463f555ebbb18949e")
(setf (get transportsysteem_pkg::ControlStateResponse :datatype-) "transportsysteem_pkg/ControlStateResponse")
(setf (get transportsysteem_pkg::ControlStateResponse :definition-)
      "# Request: The state the system should go to (\"start\", \"wait\", \"dump\")
string state
---
# Response: Whether the state transition was successfully executed
bool success
")



(provide :transportsysteem_pkg/ControlState "ba7d0f17aa81fce463f555ebbb18949e")


