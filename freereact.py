const axios = require('axios');

const apiUrl = "https://api.djliker.com";
const apiToken = "VOTRE_TOKEN";
const postToLikeId = "POST_ID";

const likePostRequest = {
  token: apiToken,
    post_id: postToLikeId
    };
axios.post(apiUrl + "/like", likePostRequest)
  .then(response => {
      console.log(response.data);
        })
          .catch(error => {
              console.error("Erreur lors de la requête:", error);
                });