import axios from 'axios';

const handleSubmit = (event) => {
  event.preventDefault();
  const data = new FormData(event.target);

  axios.post('/api/test', data)
    .then(response => {
      console.log(response);
    })
    .catch(error => {
      console.log(error);
    });
}