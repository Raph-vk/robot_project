;; Auto-generated. Do not edit!


(when (boundp 'robotarm::manipulatorGoal)
  (if (not (find-package "ROBOTARM"))
    (make-package "ROBOTARM"))
  (shadow 'manipulatorGoal (find-package "ROBOTARM")))
(unless (find-package "ROBOTARM::MANIPULATORGOAL")
  (make-package "ROBOTARM::MANIPULATORGOAL"))

(in-package "ROS")
;;//! \htmlinclude manipulatorGoal.msg.html


(defclass robotarm::manipulatorGoal
  :super ros::object
  :slots (_manipulator_start ))

(defmethod robotarm::manipulatorGoal
  (:init
   (&key
    ((:manipulator_start __manipulator_start) nil)
    )
   (send-super :init)
   (setq _manipulator_start __manipulator_start)
   self)
  (:manipulator_start
   (&optional __manipulator_start)
   (if __manipulator_start (setq _manipulator_start __manipulator_start)) _manipulator_start)
  (:serialization-length
   ()
   (+
    ;; bool _manipulator_start
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _manipulator_start
       (if _manipulator_start (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _manipulator_start
     (setq _manipulator_start (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robotarm::manipulatorGoal :md5sum-) "3868a330ea8e060554882c30a838b6a7")
(setf (get robotarm::manipulatorGoal :datatype-) "robotarm/manipulatorGoal")
(setf (get robotarm::manipulatorGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Goal
bool manipulator_start

")



(provide :robotarm/manipulatorGoal "3868a330ea8e060554882c30a838b6a7")


