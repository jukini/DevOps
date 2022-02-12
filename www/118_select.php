<!DOCTYPE html>
 
<html>
<head>
        <meta charset = 'utf-8'>
</head>
<style>
        table{
                border-top: 1px solid #444444;
                border-collapse: collapse;
        }
        tr{
                border-bottom: 1px solid #444444;
                padding: 10px;
        }
        td{
                border-bottom: 1px solid #efefef;
                padding: 10px;
        }
        table .even{
                background: #efefef;
        }
        .text{
                text-align:center;
                padding-top:20px;
                color:#000000
        }
        .text:hover{
                text-decoration: underline;
        }
        a:link {color : #57A0EE; text-decoration:none;}
        a:hover { text-decoration : underline;}
</style>
<body>


<?php
    $host = 'localhost';
    $user = 'root';
    $pw = 'rjdqb12!@';
    $dbName = 's_check';
    $conn = mysqli_connect($host, $user, $pw, $dbName);


    echo "<h2>NEW State Table</h2>";
    echo "<table>";
    $sql = "SELECT host_name, cpu, mem, date FROM db_new_state";
    $result = mysqli_query($conn, $sql);
    $fields = mysqli_num_fields($result);
    $num = 1;
    echo "<tr>";
    echo "<td>_id</td><td>host name</td><td>cpu(%)</td><td>mem(%)</td><td>date time</td>";
    echo "</tr>";
    while($row = mysqli_fetch_row($result)){
      echo "<tr>";
      echo "<td>$num</td>";
        for($i=0; $i<$fields;$i++){
        echo "<td>$row[$i]</td>";
        }
      echo "</tr>";
      $num++;
    }
    echo "</table>";
?>

<?php
    echo "<h2>OLD State Table</h2>";
    echo "<table>";
    $sql = "SELECT _id, host_name, cpu, mem, date FROM db_old_state ORDER BY date DESC";
    $result = mysqli_query($conn, $sql);
    $fields = mysqli_num_fields($result);
    $num = 1;
    echo "<tr>";
    echo "<td>No.</td><td>_id</td><td>host name</td><td>cpu(%)</td><td>mem(%)</td><td>date time</td>";
    echo "</tr>";
    while($row = mysqli_fetch_row($result)){
      echo "<tr>";
      echo "<td>$num</td>";
        for($i=0; $i<$fields;$i++){
        echo "<td>$row[$i]</td>";
        }
      echo "</tr>";
      $num++;
    }
    echo "</table>";

    
?>
</body>
</html>
