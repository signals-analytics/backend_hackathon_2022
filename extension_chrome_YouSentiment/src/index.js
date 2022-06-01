import axios from "axios";

const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const results = document.querySelector(".result-container");
const res = document.querySelector(".res");
//
const link = document.querySelector(".link");
const h = document.querySelector(".headers");

results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";

//rundeck job url
const jobURL = 'http://rundeck.signalsanalytics.co:4440/api/17/job/5249594e-5e9e-4698-917a-6ae9ee8d5e76/executions';

//headers
const post_headers = {
    "Content-Type": "application/json",
    "X-Rundeck-Auth-Token": "HJyzq9aBHPhxr2v9wXTGqBIzrKqIM12O",
    "Accept": "application/json"
}

const data = JSON.stringify({
    "argString": "-libpath /opt/signals/hadoop-processing/lib/ -video_url https://www.youtube.com/watch?v=wTXmkn6B7dI&lc=UgzyiS_48Q1Q6bdAMwt4AaABAg&ab_channel=Hyram -output_path /tmp/"
});

// grab the form
const form = document.querySelector(".form-data");

// grab the video URL
const videoUrl = document.querySelector(".video-url");

const config = {
    method: 'POST',
    url: jobURL,
    headers: post_headers,
    data: data
};

// declare a method to search
const searchForSentiment = async (config) => {
    loading.style.display = "block";
    errors.textContent = "";

    axios(config)
        .then((response) => {
            loading.style.display = "none";
            res.textContent = response.data.value;
            results.style.display = "block";
        })
        .catch((error) => {
            loading.style.display = "none";
            results.style.display = "none";
            errors.textContent = "error " + error;

            //TODO: (ls) -> remove
            link.textContent = jobURL;
            h.textContent = post_headers.Accept + "-" + post_headers["Content-Type"] + "-" + post_headers["X-Rundeck-Auth-Token"];

            console.log(error.stack)
        })
};

// declare a function to handle form submission
const handleSubmit = async e => {
    e.preventDefault();
    await searchForSentiment(config);
    console.log(videoUrl.value);
};

form.addEventListener("submit", e => handleSubmit(e));
