package com.cyxxuan.serverdemo.mapper;

import com.cyxxuan.serverdemo.pojo.HttpPacket;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface TestMapper {
    /**
     * 根据包ID获得指定包
     * @param id 包ID
     * @return HttpPacket
     */
    public HttpPacket selectPacketById(int id);

    /**
     * 指定开始和结束的包，按时间顺序倒序
     * @param start 开始的位置
     * @param length 获取的个数
     * @return 包的集合
     */
    public List<HttpPacket> selectPacketsByIndexes(int start, int length);}
