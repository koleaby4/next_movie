console.log("profile_charts.js imported successfully")

function getWatchedMoviesGenreChartData(watched_genres){
    let items_count = (Object.keys(watched_genres)).length
    console.log(items_count)

    let labels = Object.keys(watched_genres)
    labels.unshift("Genres")

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
