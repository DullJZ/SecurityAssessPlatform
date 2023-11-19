package com.cyxxuan.serverdemo.mapper;

import com.cyxxuan.serverdemo.pojo.HttpPacket;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface TestMapper {
    public HttpPacket selectPacketById(int id);

    /**
     * 指定开始和结束的包，按时间顺序倒序
     * @param start 开始的位置
     * @param length 获取的个数
     * @return
     */
    public HttpPacket[] selectPacketsByIndexes(int start, int length);
}
