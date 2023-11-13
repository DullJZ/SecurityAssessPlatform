<?php
// 等待数据库和apache启动
sleep(10);

function create_database($db_name) {
    $connection = new mysqli("db", "root", "root");

    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }

    $result = $connection->query("SHOW DATABASES");

    while ($row = $result->fetch_row()) {
        if ($db_name == $row[0]) {
            echo "数据库已存在";
            return;
        }
    }

    $connection->query("CREATE DATABASE $db_name");
    echo "数据库创建成功";
    $connection->close();
}

// 检测数据库中是否存在xhcms数据库
create_database("xhcms");

$url = "http://localhost/install/";

// 管理员账号密码admin/admin
$data = array('user' => 'admin', 'password' => 'admin', 'dbhost' => 'db', 'dbname' => 'xhcms', 'dbuser' => 'root', 'dbpwd' => 'root', 'save' => '确认正确并提交');
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);

$context  = stream_context_create($options);
$response = file_get_contents($url, false, $context);

if ($response === FALSE) { 
    die('Error occurred!');
}

echo $response;
?>
