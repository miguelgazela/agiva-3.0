<?php
    include_once('../../common/init.php');
    include_once($BASE_PATH . 'database/users.php');

    $username = $_POST['username'];
    $password = $_POST['password'];

    // Never store passwords in clear text!
    $user = getUser($username, sha1($password));

    var_dump($user);

    if($user) {
        /*
        $_SESSION['s_username'] = $username;
        $_SESSION['s_user_permission'] = $user['tipo'];
        $_SESSION['s_user_id'] = $user['id_utilizador'];
        header("Location: $BASE_URL" . "index.php");
        */
        exit();
    } else {
        /*
        $_SESSION['s_error']['login'] = "invalid_access";
        $_SESSION['s_values']['username_login'] = $username;
        header("Location: $BASE_URL" . "pages/login.php");
        */
        exit();
    }
?>