
(cl:in-package :asdf)

(defsystem "transportsysteem_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SystemControl" :depends-on ("_package_SystemControl"))
    (:file "_package_SystemControl" :depends-on ("_package"))
  ))