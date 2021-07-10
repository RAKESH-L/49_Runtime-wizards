<?php

$Fname = $_POST['Fname'];
$Lname  = $_POST['Lname'];
$Email = $_POST['Email'];
$Username = $_POST['Username'];
$Gender = $_POST['Gender'];
$Age = $_POST['Age'];
$BloodGruop1 = $_POST['BloodGruop'];
$Number = $_POST['Number'];
$Password = $_POST['Password'];
$ConfirmPassword = $_POST['ConfirmPassword'];



if(!empty($Fname) || !empty($Lname) || !empty($Email) || !empty($Username)|| !empty($Gender) || !empty($Age) || !empty($BloodGruop) || !empty($Number) || !empty($Password) || !empty($ConfirmPasswordl) )
{

    $host ="localhost";
    $dbusername ="root";
    $dppassword ="";
    $dbname ="user_data";

    $conn = new mysqli($host,$dbuserame,$dbpassword,$dbname);

    if(mysqli_connect_error()){
        die('Connect Error ('.mysqli_connect_errno().')'
        .mysqli_connect_error());
    
    }

    
    else{
        $SELECT="SELECT Email From
        register Where Email=? Limit 1";
        $INSERT = "INSERT Into register (
            Fname,Lname,Email,Username,Gender,Age,BloodGruop,Number,Password,ConfirmPassword)
            values(?,?,?,?,?,?,?,?,?,?)";

            $stmt = $conn->prepare($SELECT);
            $stmt->bind_param("s",$Email);
            $stmt->execute();
            $stmt->bind_result($Email);
            $stmt->store_result();
            $rnum = $stmt->num_rows;

    if($rnum==0){
    $stmt->close();
    $stmt = $conn->prepare($INSERT);
    $stmt->bind_param("sssssisiss",$Fname1,$Lname,$Email,$Username,$Gender,$Age,$BloodGruop,$Number,$Password,$ConfirmPassword);
    $stmt->execute();
    echo "New record inserted sucessfully";
}
else{
    echo "Someone already register using this email";
    }
    $stmt->close();
    $conn->close();
    }
    }else {
        echo "All field are required";
        die();
    }
?>