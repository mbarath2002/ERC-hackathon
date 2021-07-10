;; Auto-generated. Do not edit!


(when (boundp 'planning::array)
  (if (not (find-package "PLANNING"))
    (make-package "PLANNING"))
  (shadow 'array (find-package "PLANNING")))
(unless (find-package "PLANNING::ARRAY")
  (make-package "PLANNING::ARRAY"))

(in-package "ROS")
;;//! \htmlinclude array.msg.html


(defclass planning::array
  :super ros::object
  :slots ())

(defmethod planning::array
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get planning::array :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get planning::array :datatype-) "planning/array")
(setf (get planning::array :definition-)
      "

")



(provide :planning/array "d41d8cd98f00b204e9800998ecf8427e")


