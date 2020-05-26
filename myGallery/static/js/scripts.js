
    function copy(ids) {
        var textCopied = document.getElementById(ids);
        text = textCopied.src;
        var elementary = document.createElement("input");
        document.body.appendChild(elementary);
        elementary.setAttribute('value', text);
        elementary.select();
        document.execCommand("copy");
        document.body.removeChild(elementary);
        alert("Copied: " + textCopied.src);
    }

      function myFunction() {
        var copyText = document.getElementById("link");
        copyText.select();
        document.execCommand("Copy");
        alert("Copied the text: " + copyText.value);
      }
