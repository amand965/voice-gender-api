from pydantic import BaseModel

class VoiceFeatures(BaseModel):
    meanfreq: float
    sd: float
    median: float
    Q25: float
    Q75: float
    IQR: float
    skew: float
    kurt: float
    sp_ent: float
    sfm: float
    mode: float
    centroid: float
    meanfun: float
    minfun: float
    maxfun: float
    meandom: float
    mindom: float
    maxdom: float
    dfrange: float
    modindx: float
