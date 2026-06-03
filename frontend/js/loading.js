const fileInput =
document.getElementById("videoFile");

const fileName =
document.getElementById("fileName");

const summarizeBtn =
document.getElementById("summarizeBtn");

const clearBtn =
document.getElementById("clearBtn");


fileInput.addEventListener(
    "change",
    () => {

        if(
            fileInput.files.length > 0
        ){

            fileName.innerText =
            fileInput.files[0].name;
        }
    }
);


clearBtn.addEventListener(
    "click",
    () => {

        fileInput.value = "";

        fileName.innerText =
        "No file selected";
    }
);


summarizeBtn.addEventListener(
    "click",
    async () => {

        if(
            fileInput.files.length === 0
        ){

            alert(
                "Please select a video."
            );

            return;
        }

        const formData =
        new FormData();

        formData.append(
            "file",
            fileInput.files[0]
        );

        try{

            window.location.href =
            "loading.html";

            const response =
            await fetch(
                "http://127.0.0.1:8000/upload",
                {
                    method:"POST",
                    body:formData
                }
            );

            const data =
            await response.json();

            localStorage.setItem(
                "summaryResult",
                JSON.stringify(data)
            );

            window.location.href =
            "result.html";

        }

        catch(error){

            console.error(error);

            alert(
                "Error Processing Video"
            );
        }
    }
);