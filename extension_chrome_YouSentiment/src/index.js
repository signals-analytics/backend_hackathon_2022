import axios from "axios";

// const api = "http://rundeck.signalsanalytics.co:4440/api/17/job/"+rundeck_job_uuid+"/executions";
const rundeckApi = "http://rundeck.signalsanalytics.co:4440/project/platform/job/show/5249594e-5e9e-4698-917a-6ae9ee8d5e76";

const errors = document.querySelector(".errors");
const loading = document.querySelector(".loading");
const results = document.querySelector(".result-container");
const res = document.querySelector(".res");

results.style.display = "none";
loading.style.display = "none";
errors.textContent = "";

//headers
const post_headers = {
    "Content-Type": "application/json",
    "X-Rundeck-Auth-Token": "HJyzq9aBHPhxr2v9wXTGqBIzrKqIM12O",
    "Accept": "application/json"
}

const data = {
    "argString" : "-libpath /opt/signals/hadoop-processing/lib/ -video_url https://www.youtube.com/watch?v=wTXmkn6B7dI&lc=UgzyiS_48Q1Q6bdAMwt4AaABAg&ab_channel=Hyram -output_path /tmp/"
}

// grab the form
const form = document.querySelector(".form-data");

// grab the video URL
const videoUrl = document.querySelector(".video-url");


// declare a method to search by country name
const searchForSentiment = async videoUrl => {
    loading.style.display = "block";
    errors.textContent = "";

    axios.post(
        rundeckApi,
        data,
        {
            headers: post_headers
        }
    )
        .then((response) => {
            loading.style.display = "none";
            res.textContent = response.data.value;
            results.style.display = "block";
        })
        .catch((error) => {
            loading.style.display = "none";
            results.style.display = "none";
            errors.textContent = "error " + error;

            console.log(error.stack)
        })


/*    try {
        console.log("ddddddd")
        const response = await axios.post(
            rundeckApi,
            {
                argString: argString
            },
            {
                headers: post_headers
            }
        );

        loading.style.display = "none";
        res.textContent = response.data.value;
        results.style.display = "block";

    } catch (error) {
        loading.style.display = "none";
        results.style.display = "none";
        errors.textContent = "error " + error;

    }*/
};

// declare a function to handle form submission
const handleSubmit = async e => {
    e.preventDefault();
    searchForSentiment(videoUrl.value);
    console.log(videoUrl.value);
};

form.addEventListener("submit", e => handleSubmit(e));
