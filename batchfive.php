<?php
  require_once 'JapaneseTextCutter.php';
    
  $today = new DateTime();
  $yesterday = $today->sub(new DateInterval('P1D'));
  $formattedDate = $yesterday->format('Y-m-d');
  $databaseFile = 'batch5/datas/' . $formattedDate . '/scraped.sqlite';

  header('Content-Type: application/json');
  try {
    $pdo = new PDO('sqlite:' . $databaseFile);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  } catch (PDOException $e) {
    echo json_encode(array('status' => 'failed', 'message' => 'Connection failed: ' . $e->getMessage()));
  }

  $result = array();
  $index = 0;
  $scraped_datas = $pdo->query('SELECT * FROM scraped_datas;');

  while ($scraped_data = $scraped_datas->fetch(PDO::FETCH_ASSOC)) {
    $first_stanzas = explode("\n", str_replace(".\n", "", $scraped_data['body']))[0];
    $remaining_lines = implode("\n", array_slice(explode("\n", str_replace(".\n", "", $scraped_data['body'])), 1));
    $remaining_lines = JapaneseTextCutter::cutText($remaining_lines, 105);
    
    $result[] = array(
      "title" => $first_stanzas,
      "body" => $remaining_lines,
      "link" => $scraped_data['link'],
      // "complete_body" => $scraped_data['body'],
      "images" => array(),
      "stores" => array()
    );

    $image_links = $pdo->prepare('SELECT * FROM image_links WHERE scraped_data_id = :scraped_data_id');
    $image_links->bindValue(':scraped_data_id', $scraped_data['id']);
    $image_links->execute();

    while ($image_link = $image_links->fetch(PDO::FETCH_ASSOC)) {
      $result[$index]["images"][] = $image_link['image_link'];
    }


    $stores = $pdo->prepare('SELECT * FROM stores WHERE scraped_data_id = :scraped_data_id');
    $stores->bindValue(':scraped_data_id', $scraped_data['id']);
    $stores->execute();

    while ($store = $stores->fetch(PDO::FETCH_ASSOC)) {
      $result[$index]["stores"][] = array(
        "store_name" => $store['store_name'],
        "wls_id" => $store['wls_id']
      );
    }

    $index++;
  }

  $json = json_encode(array('status' => 'success', 'message' => '', 'data' => $result));
  echo $json;


