<?php

    $connection = mysqli_connect("localhost", "nandanunni", "9188750806", "dbms_lab");
    if (!$connection)
        die("<br /><h1 style='text-align: center;'>Database connection failure !</h1>");
    // CREATE TABLE candidate (rollNo INT(5) PRIMARY KEY, name VARCHAR(50), emailId VARCHAR(25), mobileNo VARCHAR(10), paid INT(1) DEFAULT 0, dateOfPay DATETIME);
    // CREATE TABLE payment (payId INT(5) PRIMARY KEY AUTO_INCREMENT, amount DOUBLE, dateOfPay DATETIME , transactionNo INT(10), bank VARCHAR(50), rollNo INT(5));

    if (isset($_POST['submit'])) {

        $rollNo = $_POST['rollNo'];
        $name = $_POST['name'];
        $emailId = $_POST['emailId'];
        $mobileNo = $_POST['mobileNo'];
        $amount = $_POST['amount'];
        $transactionNo = $_POST['transactionNo'];
        $bank = $_POST['bank'];

        $candidate_query = "INSERT INTO candidate (rollNo, name, emailId, mobileNo, paid) VALUES ('$rollNo', '$name', '$emailId', '$mobileNo', '1');";
        mysqli_query($connection, $candidate_query);
        $payment_query = "INSERT INTO payment (amount, transactionNo, bank, rollNo) VALUES ('$amount', '$transactionNo', '$bank' '$rollNo');";
        mysqli_query($connection, $payment_query);

    } else {
?>

<html>
    <head>
        <title>Bank</title>
        <style>
            body, .payment_form { display: flex; flex-direction: column; align-items: center; }
            .payment_form input[type="text"] { height: 25px; }
            .payment_submit { height: 40px; width: 100px; cursor: pointer; }
            table, td { border-collapse: collapse; padding: 8px; }
            .payment_details table, .payment_details td {border: 1px solid black; padding: 15px; }
        </style>
    </head>
    <body>
        <form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>" class="payment_form">
            <h1>Payment Portal</h1>
            <table>
                <tr>
                    <td><label for="rollNo">Roll Number &nbsp; </label></td>
                    <td><input type="text" name="rollNo" id="rollNo" /></td>
                </tr>
                <tr>
                    <td><label for="name">Name &nbsp; </label></td>
                    <td><input type="text" name="name" id="name" /></td>
                </tr>
                <tr>
                    <td><label for="emailId">Email Id &nbsp; </label></td>
                    <td><input type="text" name="emailId" id="emailId" /></td>
                </tr>
                <tr>
                    <td><label for="mobileNo">Mobile Number &nbsp; </label></td>
                    <td><input type="text" name="mobileNo" id="mobileNo" /></td>
                </tr>
                <tr>
                    <td><label for="amount">Amount &nbsp; </label></td>
                    <td><input type="text" name="amount" id="amount" /></td>
                </tr>
                <tr>
                    <td><label for="transactionNo">Transaction Number &nbsp; </label></td>
                    <td><input type="text" name="transactionNo" id="transactionNo" /></td>
                </tr>
                <tr>
                    <td><label for="bank">Bank &nbsp; </label></td>
                    <td><input type="text" name="bank" id="bank" /></td>
                </tr>
            </table>
            <br />
            <input class="payment_submit" type="submit" value="Pay" /><br />
            <!-- <a style="font-size: 18px;" href="createAccount.html">Create an account</a> -->
        </form>
        <br /><br />
        <div style='display: flex; align-items: center; justify-content: space-around; width: 75%;'>
            <div style='text-align: center;'>
                <h3>PAYMENTS</h3>
                <table class="payment_details">
                    <tr>
                        <td><b>Payment Id</b></td>
                        <td><b>Amount</b></td>
                        <td><b>Date of Pay</b></td>
                        <td><b>Transaction Number</b></td>
                        <td><b>Bank</b></td>
                        <td><b>Roll Number</b></td>
                    </tr>
                    <?php
                        $query = "SELECT * FROM payment;";
                        $payments = mysqli_query($connection, $query);
                        $paymentsCount = mysqli_num_rows($payments);
                        if ($paymentsCount != 0) {
                            while ($payment = mysqli_fetch_array($payments)) {
                                echo "<tr>";
                                    echo "<td>".$payment['payId']."</td>";
                                    echo "<td>".$payment['amount']."</td>";
                                    echo "<td>".$payment['dateOfPay']."</td>";
                                    echo "<td>".$payment['transactionNo']."</td>";
                                    echo "<td>".$payment['bank']."</td>";
                                    echo "<td>".$payment['rollNo']."</td>";
                                echo "</tr>";
                            }
                        } else {
                            echo "<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>";
                        }
                    ?>
                </table>
            </div>
            <div style='text-align: center;'>
                <h3>CANDIDATES</h3>
                <table class="payment_details">
                    <tr>
                        <td><b>Roll Number</b></td>
                        <td><b>Name</b></td>
                        <td><b>Email Id</b></td>
                        <td><b>Phone Number</b></td>
                        <td><b>Paid</b></td>
                    </tr>
                    <?php
                        $query = "SELECT * FROM candidate;";
                        $candidates = mysqli_query($connection, $query);
                        $candidatesCount = mysqli_num_rows($candidates);
                        if ($candidatesCount != 0) {
                            while ($candidate = mysqli_fetch_array($candidates)) {
                                echo "<tr>";
                                    echo "<td>".$candidate['rollNo']."</td>";
                                    echo "<td>".$candidate['name']."</td>";
                                    echo "<td>".$candidate['emailId']."</td>";
                                    echo "<td>".$candidate['phoneNo']."</td>";
                                    echo "<td>".$candidate['paid'] == 1 ? "Paid" : "Not Paid"."</td>";
                                echo "</tr>";
                            }
                        } else {
                            echo "<tr><td></td><td></td><td></td><td></td><td></td></tr>";
                        }
                    ?>
                </table>
        </div>
    </body>
</html>
<?php
    } 
?>