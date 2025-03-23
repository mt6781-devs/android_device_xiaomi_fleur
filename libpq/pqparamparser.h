#ifndef PQPARAMPARSER_H
#define PQPARAMPARSER_H

struct mml_pq_param;
struct mml_pq_config;
struct MMLPQHDRMetaDataInfo;
struct MMLPQ2ndOutputInfo;

class MMLPQParamParser {
public:
    int getMMLPQParmaAndEnableConfig(
        mml_pq_param* param,
        mml_pq_config* config,
        const MMLPQHDRMetaDataInfo* hdrMetaDataInfo,
        unsigned int* val,
        MMLPQ2ndOutputInfo* outputInfo
    );
};

#endif // PQPARAMPARSER_H
