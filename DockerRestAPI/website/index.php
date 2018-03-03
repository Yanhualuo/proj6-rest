<html>
    <head>
        <title>CIS 322 REST-api demo: Laptop list</title>
    </head>
    <style>
    ul {
        list-style-type:none;
    }
    </style>
    <body>
        <h2>List of All</h2>

         <ul >
            <?php
            $json = file_get_contents('http://laptop-service/listAll');
            $obj = json_decode($json);
            $space = "<br>";

            foreach ($obj as $l) {
                echo $space;
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }              
            }
            ?>  
            
        </ul>

        <h2>List of All Json</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAllJson');
            $obj = json_decode($json);
            $space = "<br>";
            foreach ($obj as $l) {
                echo $space;
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }               
            }
            ?>
        </ul>

        <h2>List of All Csv</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listAllCsv');
            $obj = json_decode($json);

            $space = "&nbsp";
            foreach ($obj as $l) {
                echo "<li>$l</li>";      
                     
            }
            ?>
        </ul>

        <h2>List Open Only</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnly');
            $obj = json_decode($json);
            foreach ($obj as $l) {     
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }      
            }
            ?>
        </ul>

        <h2>List Open Only Json</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnlyJson');
            $obj = json_decode($json);
            foreach ($obj as $l) {     
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }               
            }
            ?>
        </ul>

        <h2>List Open Only CSV</h2>
         <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listOpenOnlyCsv');
            $obj = json_decode($json);
            foreach ($obj as $l) {     
                echo "<li>$l</li>";
                             
            }
            ?>
        </ul>
        <h2>List Close Only</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnly');
            $obj = json_decode($json);
            $obj->All;
            $space = "<br>";
            foreach ($obj as $l) {     
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }               
            }
            ?>
        </ul>

        <h2>List Close Only Json</h2>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnlyJson');
            $obj = json_decode($json);
            foreach ($obj as $l) {     
                foreach ($l as $a){
                    echo "<li>$a</li>";
                }               
            }
            ?>

        </ul>
        <h2>List Close Only Csv</h2>
         <ul>           
            <?php
            $json = file_get_contents('http://laptop-service/listCloseOnlyCsv');
            $obj = json_decode($json);
            foreach ($obj as $l) {     
                
                echo "<li>$l</li>";                           
            }
            ?>
        </ul>
    </body>
</html>
