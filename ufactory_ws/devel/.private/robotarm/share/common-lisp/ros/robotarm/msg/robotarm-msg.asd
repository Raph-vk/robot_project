
(cl:in-package :asdf)

(defsystem "robotarm-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "manipulatorAction" :depends-on ("_package_manipulatorAction"))
    (:file "_package_manipulatorAction" :depends-on ("_package"))
    (:file "manipulatorActionFeedback" :depends-on ("_package_manipulatorActionFeedback"))
    (:file "_package_manipulatorActionFeedback" :depends-on ("_package"))
    (:file "manipulatorActionGoal" :depends-on ("_package_manipulatorActionGoal"))
    (:file "_package_manipulatorActionGoal" :depends-on ("_package"))
    (:file "manipulatorActionResult" :depends-on ("_package_manipulatorActionResult"))
    (:file "_package_manipulatorActionResult" :depends-on ("_package"))
    (:file "manipulatorFeedback" :depends-on ("_package_manipulatorFeedback"))
    (:file "_package_manipulatorFeedback" :depends-on ("_package"))
    (:file "manipulatorGoal" :depends-on ("_package_manipulatorGoal"))
    (:file "_package_manipulatorGoal" :depends-on ("_package"))
    (:file "manipulatorResult" :depends-on ("_package_manipulatorResult"))
    (:file "_package_manipulatorResult" :depends-on ("_package"))
  ))