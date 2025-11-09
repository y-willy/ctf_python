<?php
    require("./lib.php"); // for FLAG

    $password = sha1(md5(rand().rand().rand()).rand());

    if (isset($_GET['view-source'])) {
        show_source(__FILE__);
        exit();
    }else if(isset($_POST['password'])){
        sleep(1); // do not brute force!
        if (strcmp($_POST['password'], $password) == 0) {      
// PHP 코드에서 strcmp는 느슨한 문자열 비교함수이다, 따라서 password[] 배열로 변경한다면 NULL값을 반환시켜 == 0은 ture값을 출력한다
// "===" 로 엄격한 비교로 변경하여 취약점 해결
            echo "Congratulations! Flag is <b>" . $FLAG ."</b>";
            exit();
        } else {
            echo "Wrong password..";
        }
    }

?>
