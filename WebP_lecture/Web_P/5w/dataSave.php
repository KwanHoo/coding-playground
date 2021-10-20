
<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html>
<body>

<?php
// if($_SERVER["REQUEST_METHOD"] == "POST"){
//   $_SESSION["department"] = $_POST["department"];
//   $_SESSION["s_name"] = $_POST["s_name"];
//
//   echo "세션에 저장 되었습니다.";
// }
 ?>

 <?php
  session_start();
  $department = $_POST['department'];
  $name = $_POST['name'];

  $arr = array(
    'department' => $department,
    'name' => $name
  );
  $count = count($_SESSION['info']);
  $_SESSION['info'][$count] = $arr;

  print_r($_SESSION['info']);
/*
  foreach ($_SESSION['info'] as $department => $value) {
  }
  */
?>

 <!-- print_r($_SESSION); -->
</body>
</html>
