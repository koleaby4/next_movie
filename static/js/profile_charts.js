
function getWatchedMoviesGenreChartData(watched_genres){
    let items_count = (Object.keys(watched_genres)).length

    let labels = Object.keys(watched_genres)
    labels.unshift("Genres")

    // dummy empty value for "Genres" central element
    let values = Object.values(watched_genres)
    values.unshift(null)
    let parents = Array(items_count).fill("Genres")
    parents.unshift("")

    var data = [
        {
            type: "sunburst",
            labels: labels,
            parents: parents,
            values: values,
            outsidetextfont: { size: 24, color: "#377eb8" },
            leaf: { opacity: 0.4 },
            marker: { line: { width: 2 } },
        }
    ];

    return data
}


function getWatchedMoviesYearsChartData(watchedMoviesYears){

    var data = {
        type: 'bar',
        x: Object.keys(watchedMoviesYears),
        y: Object.values(watchedMoviesYears),
        marker: {
            color: '#C8A2C8',
            line: {
                width: 2.5
            }
        }
    };

    return [ data ];
}



function renderWatchedMoviesGenreChart(data, divId){

    const layout = {
        title: "By genre",
        font: {size: 16, color: "dodgerblue" },
        // keeping these commented out - will need them for future improvements in charts' style
        // margin: { l: 30, r: 30, b: 30, t: 30 },
        // width: 500,
        // height: 500
    };

    const config = {responsive: true}
    Plotly.newPlot(divId, data, layout, config);
}


function renderWatchedMoviesYearsChart(data, divId){

    const layout = {
        title: 'By release year',
        font: {size: 16, color: "dodgerblue" },
        xaxis_tickformat : ',d'
    };

    const config = {responsive: true}
    Plotly.newPlot(divId, data, layout, config );

}

function javaScriptObjectFromDjangoJson(djangoPayload) {
    if (djangoPayload === "None") {
        return {}
    }
    try {
        return JSON.parse(djangoPayload.replaceAll(`&#x27;`, `"`))
    } catch (error) {
        console.error(error)
        return {}
    }
}
