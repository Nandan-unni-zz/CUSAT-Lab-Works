<?php

    $connection = mysqli_connect("localhost", "nandanunni", "9188750806", "dbms_lab");
    if (!$connection)
        die("<br /><h1 style='text-align: center;'>Database connection failure !</h1>");

    $branch = $_POST["branch"];
    $semester = $_POST["semester"];

    $query = "SELECT * FROM student WHERE branchcode='$branch' AND semester='$semester';";
    $students = mysqli_query($connection, $query);
    $studentsCount = mysqli_num_rows($students);
?>
<html>
    <head>
        <title>Bank</title>
        <style>
            body { display: flex; flex-direction: column; align-items: center; }
            table, td { border-collapse: collapse; padding: 8px; }
            .student_details table, .student_details td {border: 1px solid black; padding: 15px; }
            h3 a {text-decoration: none; background-color: dodgerblue; color: white; padding: 10px;}
        </style>
    </head>
    <body>
        <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
        <h3><a href="/exp">Back to Index Page</a></h3><br />
        <div style='width: 1000px;'>
            <h3>Bar Chart</h3>
            <?php
                $query = "SELECT * FROM subject WHERE branchcode='$branch' AND semester='$semester';";
                $subjects = mysqli_query($connection, $query);
                $data = [];
                while ($subject = mysqli_fetch_array($subjects)) {
                    $subcode = $subject['subcode'];
                    $results = mysqli_query($connection, "SELECT * FROM result WHERE sem='$semester' and sub_code='$subcode';");
                    $totalResults = 0;
                    $passedResults = 0;
                    while ($result = mysqli_fetch_array($results)) {
                        $totalResults += 1;
                        if ($result['mark'] >= 50)
                            $passedResults += 1;
                    }
                    array_push($data, array("label" => $subcode, "y" => ($passedResults/$totalResults)*100));
                }
            ?>
            <script>
                window.onload = function () {
                    var chart = new CanvasJS.Chart("barChart", {
                        animationEnabled: true,
                        theme: "light2", // "light1", "light2", "dark1", "dark2"
                        title:{
                            text: "Percenatge of students passed per subject"
                        },
                        axisY: {
                            title: "Percentage of students passed"
                        },
                        data: [{        
                            type: "column",  
                            showInLegend: true, 
                            legendMarkerColor: "grey",
                            legendText: "Minimum pass marks = 50",
                            dataPoints: <?php echo json_encode($data, JSON_NUMERIC_CHECK); ?>
                        }]
                    });
                    chart.render();
                }
            </script>
            <!-- <script src="./graph.js"></script> -->
            <div id="barChart" style="height: 400px; width: 100%;"></div>
        </div>
        <br /><br />
        <div style='margin-top: 50px; display: flex; justify-content: space-around; width: 90%;'>
            <div style='text-align: center;'>
                <h3>STUDENTS</h3>
                <table class="student_details">
                    <tr>
                        <td><b>Register Number</b></td>
                        <td><b>Name</b></td>
                        <?php
                            $query = "SELECT * FROM subject WHERE branchcode='$branch' AND semester='$semester';";
                            $subjects = mysqli_query($connection, $query);
                            while ($subject = mysqli_fetch_array($subjects)) {
                                echo "<td><b>".$subject['subjectname']."</b></td>";
                            }
                        ?>
                        <td><b>Total Marks</b></td>
                    </tr>
                    <?php
                        if ($students) {
                            if ($studentsCount != 0) {
                                while ($student = mysqli_fetch_array($students)) {
                                    echo "<tr>";
                                        echo "<td>".$student['registernumber']."</td>";
                                        echo "<td>".$student['name']."</td>";
                                        $regno = $student['registernumber'];
                                        $query = "SELECT * FROM subject WHERE branchcode='$branch' AND semester='$semester';";
                                        $subjects = mysqli_query($connection, $query);
                                        $total_mark = 0;
                                        while ($subject = mysqli_fetch_array($subjects)) {
                                            $subcode = $subject['subcode'];
                                            $query = "SELECT * FROM result WHERE regno=$regno AND sub_code='$subcode' AND sem=$semester;";
                                            $results = mysqli_query($connection, $query);
                                            $result = mysqli_fetch_array($results);
                                            echo "<td>".$result['mark']." (";
                                            echo ($result['mark'] > 50) ? "<span style='color: green;'>Pass</span>" : "<span style='color: red;'>Fail</span>";
                                            echo ")</td>";
                                            $total_mark += $result['mark'];
                                        }
                                        echo "<td>".$total_mark."</td>";
                                    echo "</tr>";
                                }
                            echo "</table>";
                            }
                        } else {
                            include "index.html";
                            echo "<p style='text-align: center; color: red; font-size: 20px;'>".mysqli_error()."</p>";
                        }
                    ?>
                </table>
            </div>
            <div style='text-align: center;'>
                <h3>TEACHERS</h3>
                <table class="student_details">
                    <tr>
                        <td><b>Subject Code</b></td>
                        <td><b>Subject Name</b></td>
                        <td><b>Branch Name</b></td>
                        <td><b>Semester</b></td>
                        <td><b>Teacher Name</b></td>
                    </tr>
                    <?php
                        $query = "SELECT * FROM subject WHERE branchcode='$branch' AND semester='$semester';";
                        $subjects = mysqli_query($connection, $query);
                        while ($subject = mysqli_fetch_array($subjects)) {
                            echo "<tr>";
                                echo "<td>".$subject['subcode']."</td>";
                                echo "<td>".$subject['subjectname']."</td>";
                                $subcode = $subject['subcode'];
                                $branchcode = $subject['branchcode'];
                                $branches = mysqli_query($connection, "SELECT * FROM branch WHERE branchcode='$branchcode';");
                                $branch = mysqli_fetch_array($branches);
                                echo "<td>".$branch['branchname']."</td>";
                                echo "<td>".$subject['semester']."</td>";
                                $teachers = mysqli_query($connection, "SELECT * FROM teacher WHERE subject_code='$subcode';");
                                $teacher = mysqli_fetch_array($teachers);
                                echo "<td>".$teacher['teacher_name']."</td>";
                            echo "</tr>";
                        }
                    ?>
                </table>
            </div>
        </div>
    </body>
</html>