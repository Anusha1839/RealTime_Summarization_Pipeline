const result =
JSON.parse(
localStorage.getItem(
"summaryResult"
)
);

if(result){

```
document.getElementById(
    "title"
).innerText =
result.title;

document.getElementById(
    "overview"
).innerText =
result.summary.overview;

document.getElementById(
    "problem"
).innerText =
result.summary.problem;

document.getElementById(
    "solution"
).innerText =
result.summary.solution;


const keyPoints =
document.getElementById(
    "keyPoints"
);

keyPoints.innerHTML = "";

result.key_points.forEach(
    item => {

        const li =
        document.createElement(
            "li"
        );

        li.innerText =
        item.point;

        keyPoints.appendChild(
            li
        );

    }
);


const actionItems =
document.getElementById(
    "actionItems"
);

actionItems.innerHTML = "";

result.action_items.forEach(
    item => {

        const li =
        document.createElement(
            "li"
        );

        li.innerText =
        item.action;

        actionItems.appendChild(
            li
        );

    }
);
```

}
else{

```
alert(
    "No summary found."
);

window.location.href =
"upload.html";
```

}
