import axios from "axios";

const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const results = document.querySelector(".result-container");
const res = document.querySelector(".res");

results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";

// grab the form
const form = document.querySelector(".form-data");

// grab the video URL
let videoUrl = document.querySelector(".video-url");
chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    videoUrl.value = tabs[0].url;
    // use `url` here inside the callback because it's asynchronous!
});


// declare a method to search
const searchForSentiment = async (videoUrl) => {
    loading.style.display = "block";
    errors.textContent = "";

    //rundeck job url
    const jobURL = 'http://rundeck.signalsanalytics.co:4440/api/17/job/5249594e-5e9e-4698-917a-6ae9ee8d5e76/executions';

    //headers
    const post_headers = {
        "Content-Type": "application/json",
        "X-Rundeck-Auth-Token": "HJyzq9aBHPhxr2v9wXTGqBIzrKqIM12O",
        "Accept": "application/json"
    }

    const argString = `-libpath /opt/signals/hadoop-processing/lib/ -video_url ${videoUrl} -output_path /tmp/`;
    const data = JSON.stringify({
        "argString": argString
    });

    const config = {
        method: 'POST',
        url: jobURL,
        headers: post_headers,
        data: data
    };

    axios(config)
        .then((response) => {
            loading.style.display = "none";
            res.textContent = response.data.permalink;
            results.style.display = "block";
        })
        .catch((error) => {
            loading.style.display = "none";
            results.style.display = "none";
            errors.textContent = "error " + error;

            console.log(error.stack)
        })
};

// declare a function to handle form submission
const handleSubmit = async e => {
    e.preventDefault();
    await searchForSentiment(videoUrl.value);
    console.log(videoUrl.value);
};

async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    // `tab` will either be a `tabs.Tab` instance or `undefined`.
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
}

form.addEventListener("submit", e => handleSubmit(e));
