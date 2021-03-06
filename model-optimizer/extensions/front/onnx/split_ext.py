"""
 Copyright (c) 2018 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import numpy as np

from extensions.ops.splitv import SplitV
from mo.front.common.partial_infer.utils import int64_array
from mo.front.extractor import FrontExtractorOp
from mo.front.onnx.extractors.utils import onnx_attr


class SplitFrontExtractor(FrontExtractorOp):
    op = 'Split'
    enabled = True

    @staticmethod
    def extract(node):
        attrs = {
            'size_splits': onnx_attr(node, 'split', 'ints', default=None, dst_type=int64_array),
            'axis': onnx_attr(node, 'axis', 'i', default=0, dst_type=np.int64)
        }
        # update the attributes of the node
        SplitV.update_node_stat(node, attrs)
        return __class__.enabled
