*************************
 Common Label Properties
*************************

Different types of labels contain different aspects of annotation information about the data.
Some are more general, and some are unique to a specific label type.

Three common properties of a label will be introduced first,
and the unique ones will be explained under the corresponding type of label.

Take a :ref:`2D box label <reference/label_format/Box2D:Box2D>` as an example:

    >>> from tensorbay.label import LabeledBox2D
    >>> box2d_label = LabeledBox2D(
    ... 10, 20, 30, 40,
    ... category="category",
    ... attributes={"attribute_name": "attribute_value"},
    ... instance="instance_ID"
    ... )
    >>> box2d_label
    LabeledBox2D(10, 20, 30, 40)(
      (category): 'category',
      (attributes): {...},
      (instance): 'instance_ID'
    )

category
========

Category is a string indicating the class of the labeled object.

    >>> box2d_label.category
    'data_category'

attributes
==========

Attributes are the additional information about this data,
and there is no limit on the number of attributes.

The attribute names and values are stored in key-value pairs.

   >>> box2d_label.attributes
   {'attribute_name': 'attribute_value'}


instance
========

Instance is the unique id for the object inside of the label,
which is mostly used for tracking tasks.

   >>> box2d_label.instance
   "instance_ID"
