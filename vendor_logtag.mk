ifeq (eng,$(TARGET_BUILD_VARIANT))
VENDOR_LOG_LEVEL=I
else
VENDOR_LOG_LEVEL=S
endif

PRODUCT_VENDOR_PROPERTIES += \
    persist.log.tag.BufferQueueDump=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.BufferQueueProducer=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.C2K_AT=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.C2K_RILC=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.C2K_ATConfig=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.DCT=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.FrameTracker=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.gralloc4=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.GraphicBuffer=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.hwcomposer=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.HWUI=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.LIBC2K_RIL=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.mipc_lib=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.SurfaceControl=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.UxUtility=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.RILC=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.RILMUXD=$(VENDOR_LOG_LEVEL) \
    persist.log.tag.WifiThroughputPredictor=$(VENDOR_LOG_LEVEL)
