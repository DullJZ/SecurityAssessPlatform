package com.cyxxuan.serverdemo.service;

import com.alibaba.fastjson.JSONObject;
import com.cyxxuan.serverdemo.mapper.TestMapper;
import com.cyxxuan.serverdemo.pojo.HttpPacket;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PacketService {
    @Autowired
    private TestMapper mapper;
    public HttpPacket queryById(Integer id){
        HttpPacket packet = mapper.selectPacketById(id);
        packet.setHttpHeader(JSONObject.parseObject((String) packet.getHttpHeader()));
        return packet;
    }

    public HttpPacket[] getLatest(Integer nums){
        HttpPacket[] packets = mapper.selectPacketsByIndexes(0,nums);
        for (HttpPacket packet : packets) {
            packet.setHttpHeader(JSONObject.parseObject((String) packet.getHttpHeader()));
        }
        return packets;
    }
}
