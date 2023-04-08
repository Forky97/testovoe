// Настройка Dropzone
Dropzone.autoDiscover = false; // Отключаем автоматическую инициализацию Dropzone

var imageDropzone = new Dropzone('#image-dropzone', {
  url: 'http://127.0.0.1:8000/api/add', // URL для загрузки файлов на сервер
  autoProcessQueue: false, // Отключаем автоматическую обработку очереди файлов
  paramName: 'image', // Имя параметра, который будет использоваться для отправки файла на сервер
  uploadMultiple: true, // Разрешаем загрузку нескольких файлов
  parallelUploads: 5, // Максимальное количество файлов, которые могут быть загружены одновременно
  maxFiles: 10, // Максимальное количество файлов, которые могут быть загружены в одной сессии
  acceptedFiles: 'image/*', // Ограничение на тип файлов, которые могут быть загружены (в данном случае - только изображения)
  previewsContainer: '#image-dropzone', // Контейнер, в котором будут отображаться превью изображений
  dictCancelUpload: 'Отменить', // Текст для кнопки "Отменить" на превью изображения
});




// Обработчик события добавления файла
imageDropzone.on('addedfile', function(file) {
  // Создаем кнопку "Отменить"
  var cancelButton = Dropzone.createElement('<button class="cancel-button">Отменить</button>');
  var _this = this;

  // Вставляем кнопку "Отменить" перед превью изображения
  file.previewElement.appendChild(cancelButton);

  // Обработчик события клика на кнопку "Отменить"
  cancelButton.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();

    // Удаляем файл из Dropzone
    _this.removeFile(file);
  });
});




// Событие, вызываемое при успешной загрузке файла на сервер
imageDropzone.on('success', function(file, response) {
  // Обработка успешной загрузки файла
  console.log('Файл успешно загружен на сервер', response);
});

// Событие, вызываемое при ошибке загрузки файла на сервер
imageDropzone.on('error', function(file, errorMessage) {
  // Обработка ошибки загрузки файла
  console.error('Ошибка загрузки файла на сервер:', errorMessage);
});










document.getElementById('add-attribute').addEventListener('click', function(event) {
  event.preventDefault(); // Предотвращаем стандартное действие формы
  var attributesDiv = document.getElementById('attributes');
  var attributeDiv = document.createElement('div');
  attributeDiv.className = 'attribute';
    console.log(1);

  attributeDiv.innerHTML = `
    <input type="text" name="key[]" placeholder="Ключ">
    <input type="text" name="value[]" placeholder="Значение">
    <button class="remove-attribute">Удалить</button>
  `;
  attributesDiv.appendChild(attributeDiv);
});

document.getElementById('remove-attribute').addEventListener('click', function(event) {
  event.preventDefault(); // Предотвращаем стандартное действие кнопки
  var attributesDiv = document.getElementById('attributes');
  var attributeDivs = attributesDiv.getElementsByClassName('attribute');
  if (attributeDivs.length > 1) {
    attributesDiv.removeChild(attributeDivs[attributeDivs.length - 1]);
  }
});

document.addEventListener('click', function(event) {
  if (event.target.classList.contains('remove-attribute')) {
    event.preventDefault(); // Предотвращаем стандартное действие кнопки
    var attributeDiv = event.target.parentNode;
    var attributesDiv = document.getElementById('attributes');
    attributesDiv.removeChild(attributeDiv);
  }
});








 document.getElementById('product-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем стандартное действие отправки формы







       var formData = new FormData();


    var imageDropzone = Dropzone.forElement('#image-dropzone');
    var imageFiles = imageDropzone.getQueuedFiles();
    for (var i = 0; i < imageFiles.length; i++) {
  formData.append('images', imageFiles[i]);
    }


// Получение значений полей формы
var name = document.getElementById('name').value;
var price = document.getElementById('price').value;
var attributeKeys = document.getElementsByName('key[]');
var attributeValues = document.getElementsByName('value[]');



var attributes = [];
for (var i = 0; i < attributeKeys.length; i++) {
  var key = attributeKeys[i].value;
  var value = attributeValues[i].value;
  var attribute = { key: key, value: value };
  attributes.push(attribute);
}


// Добавление данных в FormData
formData.append('name', name);
formData.append('price', price);
formData.append('attributes', JSON.stringify(attributes));






    const csrf_token = Cookies.get('csrftoken');

    // Отправляем данные на сервер с использованием Fetch API или другого способа
    fetch('http://localhost:8000/api/add', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrf_token

      },
      body: formData
    })
    .then(function(response) {
      if (response.ok) {
        // Если запрос успешен, можно выполнить дополнительную логику
        console.log('Данные успешно отправлены на сервер');
      } else {
        // Если запрос не успешен, можно выполнить обработку ошибки
        console.error('Ошибка при отправке данных на сервер');
      }
    })
    .catch(function(error) {
      // Если произошла ошибка при выполнении запроса, можно выполнить обработку ошибки
      console.error('Произошла ошибка при отправке данных на сервер:', error);
    });
  });

