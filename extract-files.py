#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'

namespace_imports = [
	'device/xiaomi/fleur',
	'hardware/mediatek',
	'hardware/mediatek/libmtkperf_client',
	'hardware/xiaomi',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor.mediatek.hardware.videotelephony@1.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('blob-patches/ImsService.patch', '-r'),

    'system_ext/lib64/libsink.so': blob_fixup()
        .add_needed('libaudioclient_shim.so'),

    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),

    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),

    ('vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so', 'vendor/bin/hw/android.hardware.gnss-service.mediatek'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    ('vendor/bin/mnld', 'vendor/lib64/libaalservice.so', 'vendor/lib64/libcam.utils.sensorprovider.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/etc/init/android.hardware.media.c2@1.2-mediatek-64b.rc': blob_fixup()
        .regex_replace('mediatek', 'mediatek-64b'),

    'vendor/etc/init/android.hardware.neuralnetworks@1.3-service-mtk-neuron.rc': blob_fixup()
        .regex_replace('start', 'enable'),

    'vendor/etc/camera/camerabooster.json': blob_fixup()
        .regex_replace('"sea"', '"fleur"'),

    'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.15-impl.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    ('vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so', 'vendor/lib64/libmtkcam_stdutils.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),

    'vendor/lib64/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),
    (
        'vendor/lib/libteei_daemon_vfs.so',
        'vendor/lib64/libteei_daemon_vfs.so',
        'vendor/lib64/libSQLiteModule_VER_ALL.so',
        'vendor/lib64/lib3a.flash.so',
        'vendor/lib64/lib3a.ae.stat.so',
        'vendor/lib64/lib3a.sensors.color.so',
        'vendor/lib64/lib3a.sensors.flicker.so',
        'vendor/lib64/libaaa_ltm.so',
    ): blob_fixup()
        .add_needed('liblog.so'),

    ('vendor/lib64/libneuralnetworks_sl_driver_mtk_legacy_prebuilt.so', 'vendor/lib64/libneuron_adapter_mgvi.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
}

module = ExtractUtilsModule(
    'fleur',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
