package com.cyxxuan.serverdemo;

import com.alibaba.fastjson.JSONObject;
import com.cyxxuan.serverdemo.mapper.TestMapper;
import com.cyxxuan.serverdemo.pojo.HttpPacket;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ServerDemoApplicationTests {

    @Autowired
    private TestMapper mapper;
    @Test
    void contextLoads() {
    }

}
