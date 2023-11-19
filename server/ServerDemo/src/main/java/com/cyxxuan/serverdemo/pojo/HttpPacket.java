package com.cyxxuan.serverdemo.pojo;

import com.alibaba.fastjson.JSONObject;
import lombok.Data;

import java.sql.Timestamp;

@Data
public class HttpPacket {
    private int id;
    private Timestamp timestamp;
    private String topLayer;
    private String srcIp;
    private String dstIp;
    private Object httpHeader;
}
