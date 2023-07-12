<?php
  class JapaneseTextCutter {
    public static function cutText($text, $maxLength) {
      if (mb_strlen($text, 'UTF-8') <= $maxLength) {
        return $text;
      }

      $cutText = mb_substr($text, 0, $maxLength, 'UTF-8');
      $cutText = rtrim($cutText);

      if (mb_strlen($cutText, 'UTF-8') < mb_strlen($text, 'UTF-8')) {
        $cutText = mb_substr($cutText, 0, -1, 'UTF-8');
        $cutText .= '...';
      }

      return $cutText;
    }
  }
?>