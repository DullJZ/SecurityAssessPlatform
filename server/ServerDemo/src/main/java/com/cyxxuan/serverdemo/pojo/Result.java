package com.cyxxuan.serverdemo.pojo;

import lombok.Data;

/**
 * @author cyxxuan
 */
@Data
public class Result<T> {

    private Integer code;
    private String msg;
    private T data;

    private static final String DEFAULT_SUCCESS_MSG = "success";
    private static final Integer DEFAULT_SUCCESS_CODE = 200;
    private static final String DEFAULT_FAILED_MSG = "failed";
    private static final Integer DEFAULT_FAILED_CODE = 500;

    public Result() {
    }

    public Result(Integer code, String msg, T data) {
        this.code = code;
        this.msg = msg;
        this.data = data;
    }

    public Result(Integer code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    public static <T> Result<T> ok(){
        return ok(null);
    }

    public static <T> Result<T> ok(T data){
        return new Result<T>(DEFAULT_SUCCESS_CODE, DEFAULT_SUCCESS_MSG,data);
    }

    public static <T> Result<T> error(Integer code,String msg){
        return new Result<T>(code, msg);
    }

    public static <T> Result<T> notService(){
        return error(500,"服务暂未开放");
    }
}
