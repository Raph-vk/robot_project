;; Auto-generated. Do not edit!


(when (boundp 'transportsysteem_pkg::SystemControl)
  (if (not (find-package "TRANSPORTSYSTEEM_PKG"))
    (make-package "TRANSPORTSYSTEEM_PKG"))
  (shadow 'SystemControl (find-package "TRANSPORTSYSTEEM_PKG")))
(unless (find-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROL")
  (make-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROL"))
(unless (find-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROLREQUEST")
  (make-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROLREQUEST"))
(unless (find-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROLRESPONSE")
  (make-package "TRANSPORTSYSTEEM_PKG::SYSTEMCONTROLRESPONSE"))

(in-package "ROS")





(defclass transportsysteem_pkg::SystemControlRequest
  :super ros::object
  :slots (_instruction ))

(defmethod transportsysteem_pkg::SystemControlRequest
  (:init
   (&key
    ((:instruction __instruction) "")
    )
   (send-super :init)
   (setq _instruction (string __instruction))
   self)
  (:instruction
   (&optional __instruction)
   (if __instruction (setq _instruction __instruction)) _instruction)
  (:serialization-length
   ()
   (+
    ;; string _instruction
    4 (length _instruction)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _instruction
       (write-long (length _instruction) s) (princ _instruction s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _instruction
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _instruction (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass transportsysteem_pkg::SystemControlResponse
  :super ros::object
  :slots (_result ))

(defmethod transportsysteem_pkg::SystemControlResponse
  (:init
   (&key
    ((:result __result) nil)
    )
   (send-super :init)
   (setq _result __result)
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; bool _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _result
       (if _result (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _result
     (setq _result (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass transportsysteem_pkg::SystemControl
  :super ros::object
  :slots ())

(setf (get transportsysteem_pkg::SystemControl :md5sum-) "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(setf (get transportsysteem_pkg::SystemControl :datatype-) "transportsysteem_pkg/SystemControl")
(setf (get transportsysteem_pkg::SystemControl :request) transportsysteem_pkg::SystemControlRequest)
(setf (get transportsysteem_pkg::SystemControl :response) transportsysteem_pkg::SystemControlResponse)

(defmethod transportsysteem_pkg::SystemControlRequest
  (:response () (instance transportsysteem_pkg::SystemControlResponse :init)))

(setf (get transportsysteem_pkg::SystemControlRequest :md5sum-) "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(setf (get transportsysteem_pkg::SystemControlRequest :datatype-) "transportsysteem_pkg/SystemControlRequest")
(setf (get transportsysteem_pkg::SystemControlRequest :definition-)
      "# Request: The state the system should go to (\"start\", \"dump\")
string instruction
---
# Response: Whether the state transition was successfully executed
bool result

")

(setf (get transportsysteem_pkg::SystemControlResponse :md5sum-) "acc3bbca6f8e73aa0ef1136aa9bdba5b")
(setf (get transportsysteem_pkg::SystemControlResponse :datatype-) "transportsysteem_pkg/SystemControlResponse")
(setf (get transportsysteem_pkg::SystemControlResponse :definition-)
      "# Request: The state the system should go to (\"start\", \"dump\")
string instruction
---
# Response: Whether the state transition was successfully executed
bool result

")



(provide :transportsysteem_pkg/SystemControl "acc3bbca6f8e73aa0ef1136aa9bdba5b")


