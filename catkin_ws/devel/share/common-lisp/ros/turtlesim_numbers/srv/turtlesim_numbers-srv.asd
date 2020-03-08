
(cl:in-package :asdf)

(defsystem "turtlesim_numbers-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Numbers" :depends-on ("_package_Numbers"))
    (:file "_package_Numbers" :depends-on ("_package"))
  ))