;; Auto-generated. Do not edit!


(when (boundp 'robotarm::manipulatorFeedback)
  (if (not (find-package "ROBOTARM"))
    (make-package "ROBOTARM"))
  (shadow 'manipulatorFeedback (find-package "ROBOTARM")))
(unless (find-package "ROBOTARM::MANIPULATORFEEDBACK")
  (make-package "ROBOTARM::MANIPULATORFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude manipulatorFeedback.msg.html


(defclass robotarm::manipulatorFeedback
  :super ros::object
  :slots (_tandenborstel_opgepakt ))

(defmethod robotarm::manipulatorFeedback
  (:init
   (&key
    ((:tandenborstel_opgepakt __tandenborstel_opgepakt) nil)
    )
   (send-super :init)
   (setq _tandenborstel_opgepakt __tandenborstel_opgepakt)
   self)
  (:tandenborstel_opgepakt
   (&optional __tandenborstel_opgepakt)
   (if __tandenborstel_opgepakt (setq _tandenborstel_opgepakt __tandenborstel_opgepakt)) _tandenborstel_opgepakt)
  (:serialization-length
   ()
   (+
    ;; bool _tandenborstel_opgepakt
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _tandenborstel_opgepakt
       (if _tandenborstel_opgepakt (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _tandenborstel_opgepakt
     (setq _tandenborstel_opgepakt (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get robotarm::manipulatorFeedback :md5sum-) "13244125ac2eb6e745592ab638bae6b5")
(setf (get robotarm::manipulatorFeedback :datatype-) "robotarm/manipulatorFeedback")
(setf (get robotarm::manipulatorFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback
bool tandenborstel_opgepakt

")



(provide :robotarm/manipulatorFeedback "13244125ac2eb6e745592ab638bae6b5")


