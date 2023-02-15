# Copyright (c) 2023 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

SHELL_WHITELIST = {
    "vendor/qcom/proprietary/commonsys/openclwrapper/Android.mk",
}

RM_WHITELIST = {
    "vendor/qcom/proprietary/common/scripts/Android.mk",
}

LOCAL_COPY_HEADERS_WHITELIST = {}

DATETIME_WHITELIST = {}

TARGET_PRODUCT_WHITELIST = {
    "vendor/qcom/opensource/core-utils/build/AndroidBoardCommon.mk",
    "vendor/qcom/opensource/core-utils/build/build.sh",
    "vendor/qcom/opensource/core-utils/build/build_image_standalone.py",
}

RECURSIVE_WHITELIST = {}

KERNEL_WHITELIST = {}
