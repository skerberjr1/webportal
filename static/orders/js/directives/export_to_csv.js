app.directive('exportToCsv', function() {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var el = element[0];
            element.bind('click', function(e) {
                var table = $(this).closest('.panel, body, .modal-content').find('table')[0];
                var csvString = '';
                for (var i = 0; i < table.rows.length; i++) {
                    var rowData = table.rows[i].cells;
                    for (var j = 0; j < rowData.length; j++) {
                        if ($(rowData[j]).has("input").length) {
                            csvString = csvString + $(rowData[j]).children("input").attr("placeholder") + ',';
                        }
                        else {
                            csvString = csvString + '\"' + rowData[j].innerText + '\",';   
                        }
                    }
                    csvString = csvString.substring(0, csvString.length - 1);
                    csvString = csvString + "\n";
                }
                csvString = csvString.substring(0, csvString.length - 1);
                var a = $("<a/>", {
                    style: "display:none",
                    href: "data:application/octet-stream;base64," + btoa(csvString),
                    download: "tableExport.csv"
                }).appendTo('body')
                a[0].click()
                a.remove()
            });
        }
    }
});