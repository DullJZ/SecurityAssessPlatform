package com.cyxxuan.serverdemo.controller;

import com.cyxxuan.serverdemo.mapper.TestMapper;
import com.cyxxuan.serverdemo.pojo.HttpPacket;
import com.cyxxuan.serverdemo.pojo.Result;
import com.cyxxuan.serverdemo.service.PacketService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;


@RestController
@RequestMapping("/packet/xhcms")
public class PacketController {
    @Autowired
    private PacketService packetService;
    @RequestMapping("/query")
    public Result<HttpPacket> queryById(Integer id){
        return Result.ok(packetService.queryById(id));
    }
    @RequestMapping("/queryLatest")
    @CrossOrigin("http://127.0.0.1:8080")
    public Result<List<HttpPacket>> queryLatest(@RequestParam Integer nums){
        return Result.ok(packetService.getLatest(nums));
    }
}
