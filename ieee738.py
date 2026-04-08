<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_87fdf8d4bf63de14c04a79108d2593c2 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>

            <style>html, body {
                width: 100%;
                height: 100%;
                margin: 0;
                padding: 0;
            }
            </style>

            <style>#map {
                position:absolute;
                top:0;
                bottom:0;
                right:0;
                left:0;
                }
            </style>

            <script>
                L_NO_TOUCH = false;
                L_DISABLE_3D = false;
            </script>

        
</head>
<body>
    
    
    <script>
        var countdown = 6;
        var countdownElement = document.createElement('div');
        
        function updateCountdown() {
            countdown--;
            countdownElement.innerHTML = '<strong> LIVE POWER SYSTEM MAP</strong><br>' +
                                        'Last updated: 13:58:28<br>' +
                                        'Next refresh: ' + countdown + ' seconds';
            
            // Change background color as countdown progresses
            if (countdown <= 2) {
                countdownElement.style.backgroundColor = '#ffcccc';
            } else if (countdown <= 4) {
                countdownElement.style.backgroundColor = '#ffffcc';
            } else {
                countdownElement.style.backgroundColor = '#ccffcc';
            }
            
            if (countdown <= 0) {
                location.reload();
            }
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            countdownElement.style.position = 'fixed';
            countdownElement.style.top = '10px';
            countdownElement.style.right = '10px';
            countdownElement.style.backgroundColor = '#ccffcc';
            countdownElement.style.padding = '10px';
            countdownElement.style.border = '2px solid #007cbf';
            countdownElement.style.borderRadius = '5px';
            countdownElement.style.zIndex = '9999';
            countdownElement.style.fontFamily = 'Arial, sans-serif';
            countdownElement.style.fontSize = '14px';
            countdownElement.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
            document.body.appendChild(countdownElement);
            
            setInterval(updateCountdown, 1000);
        });
    </script>
    
    
            <div class="folium-map" id="map_87fdf8d4bf63de14c04a79108d2593c2" ></div>
        
</body>
<script>
    
    
            var map_87fdf8d4bf63de14c04a79108d2593c2 = L.map(
                "map_87fdf8d4bf63de14c04a79108d2593c2",
                {
                    center: [21.47694, -157.85833],
                    crs: L.CRS.EPSG3857,
                    ...{
  "zoom": 11,
  "zoomControl": true,
  "preferCanvas": false,
}

                }
            );

            

        
    
            var tile_layer_5799a171b406e268ecf21429b252ce7c = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {
  "minZoom": 0,
  "maxZoom": 19,
  "maxNativeZoom": 19,
  "noWrap": false,
  "attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors",
  "subdomains": "abc",
  "detectRetina": false,
  "tms": false,
  "opacity": 1,
}

            );
        
    
            tile_layer_5799a171b406e268ecf21429b252ce7c.addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_b3b6b227ea8dac2e059b46e34136a7e7 = L.polyline(
                [[21.344246, -157.939889], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_ec258f659711c2ba16ccd70b75cb05e7 = L.polyline(
                [[21.344246, -157.939889], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_cdb85ea390adc42b0e4694a9a3d03781 = L.polyline(
                [[21.344246, -157.939889], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_60971dc813ab4d7fcf800a589cb7bcee = L.polyline(
                [[21.344246, -157.939889], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_535134587f4a2a4cae4223745ed82977 = L.polyline(
                [[21.344246, -157.939889], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_7d2880cf65ec9e8b587c1601514c3e9c = L.polyline(
                [[21.344246, -157.939889], [21.303419, -158.106528]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_193bee2f6b30f8aa3e6b95d000f72e3a = L.polyline(
                [[21.344246, -157.939889], [21.303419, -158.106528]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_bd6450310209a27180f664703d23ec5e = L.polyline(
                [[21.344246, -157.939889], [21.293143, -157.848767]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_e65a0c312bcf046c87fad7c03f53f848 = L.polyline(
                [[21.344246, -157.939889], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_3cf98acef5407dd075611e28d107b192 = L.polyline(
                [[21.344246, -157.939889], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_61aabdee667e3fc204f9f3ed10c7fe96 = L.polyline(
                [[21.344246, -157.939889], [21.291518, -157.826869]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_7da1e51d841725ba962726e8b0a26f90 = L.polyline(
                [[21.344246, -157.939889], [21.406053, -157.884952]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_9ff14ebd6a8f994a12ab6ce3764556ef = L.polyline(
                [[21.344246, -157.939889], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_9b1b693e22b64e1e519c17a9af5fe833 = L.polyline(
                [[21.344246, -157.939889], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_ceb96380ee67380a76557170c245f16f = L.polyline(
                [[21.344246, -157.939889], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_3de117aa63b5aac9e9e5b7a6abe3928e = L.polyline(
                [[21.344246, -157.939889], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_84977bc7d249b8c7db255e6ce26930e9 = L.polyline(
                [[21.344246, -157.939889], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_ce96615379500562e448f5f2fab523cf = L.polyline(
                [[21.347927, -157.876274], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_3c6cfe42a3602c7d8dde9d7c2274e5a3 = L.polyline(
                [[21.347927, -157.876274], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_7e6088817ae18b2a4654414cfa83896f = L.polyline(
                [[21.347927, -157.876274], [21.311063, -157.750269]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_db081932b105ec43c4e64688f75a4944 = L.polyline(
                [[21.347927, -157.876274], [21.417374, -157.936867]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_3767e3f3d7f5444804273071054de47f = L.polyline(
                [[21.347927, -157.876274], [21.417374, -157.936867]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_e4ca2704aa91deb5cbae8d9ed50014d6 = L.polyline(
                [[21.347927, -157.876274], [21.417374, -157.936867]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_07821e75d9a434658e30742075df3b56 = L.polyline(
                [[21.347927, -157.876274], [21.406053, -157.884952]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_2b70a4d2ab674ed652f8e4596c9b93c2 = L.polyline(
                [[21.293143, -157.848767], [21.290612, -157.788328]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_66249c761b85cf0d9b63b401903e0ec0 = L.polyline(
                [[21.316548, -157.845053], [21.273462, -157.822444]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_80d4713fecb97f13d11b5e83a6536d86 = L.polyline(
                [[21.316548, -157.845053], [21.395084, -157.758188]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_12e9e95b79e35870b60b7cf141560535 = L.polyline(
                [[21.291518, -157.826869], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_7d366042a1345f31d72183f5f1a5b094 = L.polyline(
                [[21.291518, -157.826869], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_00565d0b90de6fe8a1414cf3da48a935 = L.polyline(
                [[21.291518, -157.826869], [21.316548, -157.845053]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_855602f89a74e2294299d42bb1cb7fe2 = L.polyline(
                [[21.316548, -157.845053], [21.35548, -157.821663]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_0863c4d11341564274c782da9594e844 = L.polyline(
                [[21.316548, -157.845053], [21.32021, -157.810758]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_493243fce34f5b2d4c00924ac081445d = L.polyline(
                [[21.316548, -157.845053], [21.32021, -157.810758]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_f39ebc83253abe5c3a8427cbd7f33b93 = L.polyline(
                [[21.291518, -157.826869], [21.273462, -157.822444]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_fb2437bb37f0a37623758fed2b8e07ee = L.polyline(
                [[21.291518, -157.826869], [21.290612, -157.788328]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_411bb082e1dee3b17e80b4bf25804d9d = L.polyline(
                [[21.291518, -157.826869], [21.290612, -157.788328]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_34d77dfafc6a915293fd9059dc79f4c9 = L.polyline(
                [[21.291518, -157.826869], [21.290612, -157.788328]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_fe8bd0a37b196e8aec5000c1fc5fdbb6 = L.polyline(
                [[21.451733, -157.824227], [21.395084, -157.758188]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_237c9c6359f9b7f986afb49ceb20f14d = L.polyline(
                [[21.451733, -157.824227], [21.417374, -157.936867]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_e4ba2d92beac7cdd57ba19c81eeaf336 = L.polyline(
                [[21.451733, -157.824227], [21.417374, -157.936867]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_fd8c1b7453dba3992a5257c97d94fac6 = L.polyline(
                [[21.273462, -157.822444], [21.395084, -157.758188]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_0b09a1c9a04906fc8d2dfa65774860d9 = L.polyline(
                [[21.35548, -157.821663], [21.290612, -157.788328]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_7e3694413835c9f8c30b89947d08521d = L.polyline(
                [[21.35548, -157.821663], [21.395084, -157.758188]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_40fa293a1deece8029de5bfc4696b9e3 = L.polyline(
                [[21.32021, -157.810758], [21.395084, -157.758188]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_42e5041eefc0f88ba85a5d3f58dedc02 = L.polyline(
                [[21.32021, -157.810758], [21.335013, -157.710924]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_6e055ece6ee68c611df093816eacedf8 = L.polyline(
                [[21.290612, -157.788328], [21.311063, -157.750269]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_ea0a02edd32c4832996782e3d5bdf8c3 = L.polyline(
                [[21.311063, -157.750269], [21.294518, -157.688748]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_53539f02e032697841dffa35faed62f9 = L.polyline(
                [[21.335013, -157.710924], [21.294518, -157.688748]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_fc2006a3e407996d4b7152eae7d8565f = L.polyline(
                [[21.417374, -157.936867], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_0615dfedab21716253bc10884e53c101 = L.polyline(
                [[21.417374, -157.936867], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_942611d9407f63580e5e13cf51a1b4e2 = L.polyline(
                [[21.417374, -157.936867], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_693aa45538d60dd31ac7b2e8421274a3 = L.polyline(
                [[21.417374, -157.936867], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_3cc047981f1cc174aaed0aaf6e4f9976 = L.polyline(
                [[21.482531, -157.934221], [21.417469, -157.983838]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_1bf1de1cad69014f59632b9ab5ac5a88 = L.polyline(
                [[21.482531, -157.934221], [21.57139, -157.979384]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_a36247fa9e903898e347eda41b41e7fe = L.polyline(
                [[21.482531, -157.934221], [21.55775, -157.905396]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_23b9033901c7396dcf8a3c0ae399ac12 = L.polyline(
                [[21.417469, -157.983838], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_6af28daedac4cfb89fb4d025ae6e94ae = L.polyline(
                [[21.417469, -157.983838], [21.356395, -158.128853]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_ccfdfe1e07607dad89c8baff619e6077 = L.polyline(
                [[21.417469, -157.983838], [21.4785, -158.0581]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_55a41785083659fbe0458bb39bbde6b2 = L.polyline(
                [[21.417469, -157.983838], [21.4785, -158.0581]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_97d8c33e9671284cc496eb21bc02ed2a = L.polyline(
                [[21.363106, -158.082206], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_236043a8fa745546d678c8ea7ff3c600 = L.polyline(
                [[21.363106, -158.082206], [21.344756, -158.022282]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_dd69f00254e0e6f7f3a50e5ccae3c69b = L.polyline(
                [[21.363106, -158.082206], [21.468626, -158.166919]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_4207b6e54a2283bb7caed5450df5a887 = L.polyline(
                [[21.363106, -158.082206], [21.311667, -158.113889]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_19109eef0314d48ca4312fa31e5e4712 = L.polyline(
                [[21.344756, -158.022282], [21.303419, -158.106528]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_687804866cacefe0c0cf92cad1f7d52a = L.polyline(
                [[21.344756, -158.022282], [21.303419, -158.106528]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_684a1d5fadc7b3b630be2ae69143dd71 = L.polyline(
                [[21.344756, -158.022282], [21.356395, -158.128853]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_eba73e0f928bb7235ef60f54226c7292 = L.polyline(
                [[21.344756, -158.022282], [21.356395, -158.128853]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_a7cf6da72e29bb2fa6229503130233bd = L.polyline(
                [[21.658692, -157.978792], [21.618479, -157.943953]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_270f8c9c7d9da87bae7c75704d006dcf = L.polyline(
                [[21.621367, -158.048011], [21.57139, -157.979384]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_fbf7caf6e50a566f4875247d015e348d = L.polyline(
                [[21.621367, -158.048011], [21.57139, -157.979384]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_c78ebfbc997abffd3531b40206ed6d2b = L.polyline(
                [[21.621367, -158.048011], [21.56364, -158.185151]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_bc70d798b650b5d6cd706de107b18a93 = L.polyline(
                [[21.618479, -157.943953], [21.57139, -157.979384]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_d1eb4bba66b382f9c0ed8002b37faae4 = L.polyline(
                [[21.618479, -157.943953], [21.55775, -157.905396]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_f1755a3c89f3495cb265d5b21f1ffde2 = L.polyline(
                [[21.56364, -158.185151], [21.468626, -158.166919]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_f546efb89bbb26abe8a33bac90585399 = L.polyline(
                [[21.468626, -158.166919], [21.4785, -158.0581]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_aa4f9691ed1b166e68fd7803217a19ef = L.polyline(
                [[21.468626, -158.166919], [21.4785, -158.0581]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var poly_line_bdf7d27ed715b28285e0e817e7258cec = L.polyline(
                [[21.303419, -158.106528], [21.356395, -158.128853]],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": false, "fillColor": "black", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "noClip": false, "opacity": 0.7, "smoothFactor": 1.0, "stroke": true, "weight": 5}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
            var circle_a54fcd7651d2ef8227d0834f0a52f61f = L.circle(
                [21.344246, -157.939889],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_8548ddefb7bfb9717173f4c79c4351bc = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_c617532ffe7866186b02902ff222b602 = $(`<div id="html_c617532ffe7866186b02902ff222b602" style="width: 100.0%; height: 100.0%;">Bus 1: ALOHA138<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_8548ddefb7bfb9717173f4c79c4351bc.setContent(html_c617532ffe7866186b02902ff222b602);
            
        

        circle_a54fcd7651d2ef8227d0834f0a52f61f.bindPopup(popup_8548ddefb7bfb9717173f4c79c4351bc)
        ;

        
    
    
            circle_a54fcd7651d2ef8227d0834f0a52f61f.bindTooltip(
                `<div>
                     ALOHA138 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_92c750434606fbf3c6115f2acf4380e5 = L.circle(
                [21.344246, -157.939889],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_a785cad68ed7f877402a9499b6a559d9 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_9da48822cdc8e640dc710865c05991b4 = $(`<div id="html_9da48822cdc8e640dc710865c05991b4" style="width: 100.0%; height: 100.0%;">Bus 2: ALOHA69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_a785cad68ed7f877402a9499b6a559d9.setContent(html_9da48822cdc8e640dc710865c05991b4);
            
        

        circle_92c750434606fbf3c6115f2acf4380e5.bindPopup(popup_a785cad68ed7f877402a9499b6a559d9)
        ;

        
    
    
            circle_92c750434606fbf3c6115f2acf4380e5.bindTooltip(
                `<div>
                     ALOHA69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_55bc4746ff19e1a252ebc512e0234885 = L.circle(
                [21.347927, -157.876274],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_c5cdf3485fc3d36836fbd47ad92e92d3 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_f0bf4b892e5bec77174140a238ee0e6d = $(`<div id="html_f0bf4b892e5bec77174140a238ee0e6d" style="width: 100.0%; height: 100.0%;">Bus 3: FLOWER69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_c5cdf3485fc3d36836fbd47ad92e92d3.setContent(html_f0bf4b892e5bec77174140a238ee0e6d);
            
        

        circle_55bc4746ff19e1a252ebc512e0234885.bindPopup(popup_c5cdf3485fc3d36836fbd47ad92e92d3)
        ;

        
    
    
            circle_55bc4746ff19e1a252ebc512e0234885.bindTooltip(
                `<div>
                     FLOWER69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_1ea36bd1d29fb51c08c543859a640ef6 = L.circle(
                [21.293143, -157.848767],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_af4cdd48e0a82e2e2bce7692e6f07278 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_8c970e0cfeed30f209da2675ac6dfaca = $(`<div id="html_8c970e0cfeed30f209da2675ac6dfaca" style="width: 100.0%; height: 100.0%;">Bus 4: WAVE69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_af4cdd48e0a82e2e2bce7692e6f07278.setContent(html_8c970e0cfeed30f209da2675ac6dfaca);
            
        

        circle_1ea36bd1d29fb51c08c543859a640ef6.bindPopup(popup_af4cdd48e0a82e2e2bce7692e6f07278)
        ;

        
    
    
            circle_1ea36bd1d29fb51c08c543859a640ef6.bindTooltip(
                `<div>
                     WAVE69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_2201f08fc5665e9e1af4b45981372f80 = L.circle(
                [21.316548, -157.845053],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_676ef4f27fb6b6e1ad5e5602c687ca6d = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_34f968e5cbfd9f073a8a6074db0c48c8 = $(`<div id="html_34f968e5cbfd9f073a8a6074db0c48c8" style="width: 100.0%; height: 100.0%;">Bus 5: HONOLULU138<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_676ef4f27fb6b6e1ad5e5602c687ca6d.setContent(html_34f968e5cbfd9f073a8a6074db0c48c8);
            
        

        circle_2201f08fc5665e9e1af4b45981372f80.bindPopup(popup_676ef4f27fb6b6e1ad5e5602c687ca6d)
        ;

        
    
    
            circle_2201f08fc5665e9e1af4b45981372f80.bindTooltip(
                `<div>
                     HONOLULU138 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_55da4bd75b07d68d4094698a8bfd44ac = L.circle(
                [21.316548, -157.845053],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_97ba56ed537aad45d3102f3637433621 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_8e9b6b19f8619c995b16afbddbf1414e = $(`<div id="html_8e9b6b19f8619c995b16afbddbf1414e" style="width: 100.0%; height: 100.0%;">Bus 6: HONOLULU69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_97ba56ed537aad45d3102f3637433621.setContent(html_8e9b6b19f8619c995b16afbddbf1414e);
            
        

        circle_55da4bd75b07d68d4094698a8bfd44ac.bindPopup(popup_97ba56ed537aad45d3102f3637433621)
        ;

        
    
    
            circle_55da4bd75b07d68d4094698a8bfd44ac.bindTooltip(
                `<div>
                     HONOLULU69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_d45aca841429f10318b3aa505ae84400 = L.circle(
                [21.291518, -157.826869],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_3b5efffee7fc1d35e4d5b28febdf6f52 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_29e55a5e17155d1cc62240d09f23c05a = $(`<div id="html_29e55a5e17155d1cc62240d09f23c05a" style="width: 100.0%; height: 100.0%;">Bus 7: SURF69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_3b5efffee7fc1d35e4d5b28febdf6f52.setContent(html_29e55a5e17155d1cc62240d09f23c05a);
            
        

        circle_d45aca841429f10318b3aa505ae84400.bindPopup(popup_3b5efffee7fc1d35e4d5b28febdf6f52)
        ;

        
    
    
            circle_d45aca841429f10318b3aa505ae84400.bindTooltip(
                `<div>
                     SURF69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_b8065a5ef79bb9a4aed2d0995003ea43 = L.circle(
                [21.451733, -157.824227],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_13c29608f1ba96b519f1ad15368dd28e = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_c18ec0e653ea8a01a65f587e8cadc163 = $(`<div id="html_c18ec0e653ea8a01a65f587e8cadc163" style="width: 100.0%; height: 100.0%;">Bus 8: KANEOHE69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_13c29608f1ba96b519f1ad15368dd28e.setContent(html_c18ec0e653ea8a01a65f587e8cadc163);
            
        

        circle_b8065a5ef79bb9a4aed2d0995003ea43.bindPopup(popup_13c29608f1ba96b519f1ad15368dd28e)
        ;

        
    
    
            circle_b8065a5ef79bb9a4aed2d0995003ea43.bindTooltip(
                `<div>
                     KANEOHE69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_a2490139ca917db05f0c6c0af8693cee = L.circle(
                [21.273462, -157.822444],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_e5fed73ab35644f8eee6340114520129 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_8385182e28ee44f25b9a57eb4c4425f0 = $(`<div id="html_8385182e28ee44f25b9a57eb4c4425f0" style="width: 100.0%; height: 100.0%;">Bus 9: TURTLE138<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_e5fed73ab35644f8eee6340114520129.setContent(html_8385182e28ee44f25b9a57eb4c4425f0);
            
        

        circle_a2490139ca917db05f0c6c0af8693cee.bindPopup(popup_e5fed73ab35644f8eee6340114520129)
        ;

        
    
    
            circle_a2490139ca917db05f0c6c0af8693cee.bindTooltip(
                `<div>
                     TURTLE138 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_a174a2a42af20286aa3a6d7e00039a2c = L.circle(
                [21.273462, -157.822444],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_3b64fb37a368b3a9f602dc126164c93a = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_29d358793f592c881ceebf0b9ef51081 = $(`<div id="html_29d358793f592c881ceebf0b9ef51081" style="width: 100.0%; height: 100.0%;">Bus 10: TURTLE69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_3b64fb37a368b3a9f602dc126164c93a.setContent(html_29d358793f592c881ceebf0b9ef51081);
            
        

        circle_a174a2a42af20286aa3a6d7e00039a2c.bindPopup(popup_3b64fb37a368b3a9f602dc126164c93a)
        ;

        
    
    
            circle_a174a2a42af20286aa3a6d7e00039a2c.bindTooltip(
                `<div>
                     TURTLE69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_6d9bae9617fda14844bc4b11b2e75964 = L.circle(
                [21.35548, -157.821663],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_9ee0127964bec13ce3b64c5a4fdb208e = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_bc82840b101d7301ac2bebc55c64ed8d = $(`<div id="html_bc82840b101d7301ac2bebc55c64ed8d" style="width: 100.0%; height: 100.0%;">Bus 11: MAHALO69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_9ee0127964bec13ce3b64c5a4fdb208e.setContent(html_bc82840b101d7301ac2bebc55c64ed8d);
            
        

        circle_6d9bae9617fda14844bc4b11b2e75964.bindPopup(popup_9ee0127964bec13ce3b64c5a4fdb208e)
        ;

        
    
    
            circle_6d9bae9617fda14844bc4b11b2e75964.bindTooltip(
                `<div>
                     MAHALO69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_078b9ce7006abfa1cea8b907bc53b58b = L.circle(
                [21.32021, -157.810758],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_68b920ac52a188341481d192a8479b64 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_002fd9a800d7d57255b4c312cd9a5892 = $(`<div id="html_002fd9a800d7d57255b4c312cd9a5892" style="width: 100.0%; height: 100.0%;">Bus 12: LYCHEE69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_68b920ac52a188341481d192a8479b64.setContent(html_002fd9a800d7d57255b4c312cd9a5892);
            
        

        circle_078b9ce7006abfa1cea8b907bc53b58b.bindPopup(popup_68b920ac52a188341481d192a8479b64)
        ;

        
    
    
            circle_078b9ce7006abfa1cea8b907bc53b58b.bindTooltip(
                `<div>
                     LYCHEE69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_bf1ada83883a4878cc662705fb21804b = L.circle(
                [21.290612, -157.788328],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_b2b28fa2234089419a6bb048a4b5de42 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_51e1a93857aeb796ab21e1c212e69ba8 = $(`<div id="html_51e1a93857aeb796ab21e1c212e69ba8" style="width: 100.0%; height: 100.0%;">Bus 13: COCONUT69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_b2b28fa2234089419a6bb048a4b5de42.setContent(html_51e1a93857aeb796ab21e1c212e69ba8);
            
        

        circle_bf1ada83883a4878cc662705fb21804b.bindPopup(popup_b2b28fa2234089419a6bb048a4b5de42)
        ;

        
    
    
            circle_bf1ada83883a4878cc662705fb21804b.bindTooltip(
                `<div>
                     COCONUT69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_c0094fe4e07096c022e4b7c7ead07155 = L.circle(
                [21.395084, -157.758188],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_90ac30006013f1c16bb66e0767e417b7 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_029571251ce18429c7b396d66baec730 = $(`<div id="html_029571251ce18429c7b396d66baec730" style="width: 100.0%; height: 100.0%;">Bus 14: KAILUA138<br>Temp: nan°C<br>Wind: nan m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_90ac30006013f1c16bb66e0767e417b7.setContent(html_029571251ce18429c7b396d66baec730);
            
        

        circle_c0094fe4e07096c022e4b7c7ead07155.bindPopup(popup_90ac30006013f1c16bb66e0767e417b7)
        ;

        
    
    
            circle_c0094fe4e07096c022e4b7c7ead07155.bindTooltip(
                `<div>
                     KAILUA138 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_becd0b411e7edbef6c5b9e12ec39950a = L.circle(
                [21.395084, -157.758188],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_3592844ee621537a4a465c3e3aa41458 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_a8ec2a790c371b42edb1a8f4430581da = $(`<div id="html_a8ec2a790c371b42edb1a8f4430581da" style="width: 100.0%; height: 100.0%;">Bus 15: KAILUA69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_3592844ee621537a4a465c3e3aa41458.setContent(html_a8ec2a790c371b42edb1a8f4430581da);
            
        

        circle_becd0b411e7edbef6c5b9e12ec39950a.bindPopup(popup_3592844ee621537a4a465c3e3aa41458)
        ;

        
    
    
            circle_becd0b411e7edbef6c5b9e12ec39950a.bindTooltip(
                `<div>
                     KAILUA69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_f89ba6dad7a44a1aeb1c2fe17e5ca83c = L.circle(
                [21.311063, -157.750269],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_10027bf70bd0442c9426d212a8e3c712 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_36695aa7c56497a5132a89d7cf3a6b9a = $(`<div id="html_36695aa7c56497a5132a89d7cf3a6b9a" style="width: 100.0%; height: 100.0%;">Bus 16: PALM69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_10027bf70bd0442c9426d212a8e3c712.setContent(html_36695aa7c56497a5132a89d7cf3a6b9a);
            
        

        circle_f89ba6dad7a44a1aeb1c2fe17e5ca83c.bindPopup(popup_10027bf70bd0442c9426d212a8e3c712)
        ;

        
    
    
            circle_f89ba6dad7a44a1aeb1c2fe17e5ca83c.bindTooltip(
                `<div>
                     PALM69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_79acbd6d06a3b5cd0dfb43642989046c = L.circle(
                [21.335013, -157.710924],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_02d3cca79e7e65b5a5ab71e84a8a0876 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_8194e27c7d38508410b1a6adbed75226 = $(`<div id="html_8194e27c7d38508410b1a6adbed75226" style="width: 100.0%; height: 100.0%;">Bus 17: WAIMANALO69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_02d3cca79e7e65b5a5ab71e84a8a0876.setContent(html_8194e27c7d38508410b1a6adbed75226);
            
        

        circle_79acbd6d06a3b5cd0dfb43642989046c.bindPopup(popup_02d3cca79e7e65b5a5ab71e84a8a0876)
        ;

        
    
    
            circle_79acbd6d06a3b5cd0dfb43642989046c.bindTooltip(
                `<div>
                     WAIMANALO69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_9647bdb669a64f63732eee7908e84afe = L.circle(
                [21.294518, -157.688748],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_586a46f2acde36b08895a240367a7183 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_2f01d4a47e3e41acc0baa51058a6a071 = $(`<div id="html_2f01d4a47e3e41acc0baa51058a6a071" style="width: 100.0%; height: 100.0%;">Bus 18: VOLCANO69<br>Temp: nan°C<br>Wind: nan m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_586a46f2acde36b08895a240367a7183.setContent(html_2f01d4a47e3e41acc0baa51058a6a071);
            
        

        circle_9647bdb669a64f63732eee7908e84afe.bindPopup(popup_586a46f2acde36b08895a240367a7183)
        ;

        
    
    
            circle_9647bdb669a64f63732eee7908e84afe.bindTooltip(
                `<div>
                     VOLCANO69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_7be6a24c232be07de0939c9a3b5135d9 = L.circle(
                [21.417374, -157.936867],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_e1659a7faaaf725e2ac19d0a2dc038b5 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_e451c635a3ea51d6a56e698eaa58ccc6 = $(`<div id="html_e451c635a3ea51d6a56e698eaa58ccc6" style="width: 100.0%; height: 100.0%;">Bus 19: PEARL CITY69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_e1659a7faaaf725e2ac19d0a2dc038b5.setContent(html_e451c635a3ea51d6a56e698eaa58ccc6);
            
        

        circle_7be6a24c232be07de0939c9a3b5135d9.bindPopup(popup_e1659a7faaaf725e2ac19d0a2dc038b5)
        ;

        
    
    
            circle_7be6a24c232be07de0939c9a3b5135d9.bindTooltip(
                `<div>
                     PEARL CITY69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_783d22798b2d70d4dcc9020c0a3e2f45 = L.circle(
                [21.482531, -157.934221],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_794bbdc87f9839c3055d411ac978b2d0 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_79fc0404cd2b5ea08de767caeb4fd7eb = $(`<div id="html_79fc0404cd2b5ea08de767caeb4fd7eb" style="width: 100.0%; height: 100.0%;">Bus 20: MILILANI69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_794bbdc87f9839c3055d411ac978b2d0.setContent(html_79fc0404cd2b5ea08de767caeb4fd7eb);
            
        

        circle_783d22798b2d70d4dcc9020c0a3e2f45.bindPopup(popup_794bbdc87f9839c3055d411ac978b2d0)
        ;

        
    
    
            circle_783d22798b2d70d4dcc9020c0a3e2f45.bindTooltip(
                `<div>
                     MILILANI69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_2c64e31e2568d35df82116169133e449 = L.circle(
                [21.406053, -157.884952],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_283f7ba7f71515b3f22dc15ce40df09b = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_8b45c998822e840973b2b0d45dd94b95 = $(`<div id="html_8b45c998822e840973b2b0d45dd94b95" style="width: 100.0%; height: 100.0%;">Bus 21: AIEA69<br>Temp: 25.6°C<br>Wind: 29.52 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_283f7ba7f71515b3f22dc15ce40df09b.setContent(html_8b45c998822e840973b2b0d45dd94b95);
            
        

        circle_2c64e31e2568d35df82116169133e449.bindPopup(popup_283f7ba7f71515b3f22dc15ce40df09b)
        ;

        
    
    
            circle_2c64e31e2568d35df82116169133e449.bindTooltip(
                `<div>
                     AIEA69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_2eabaee95983e2b3526a285ec1f95541 = L.circle(
                [21.417469, -157.983838],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_26722a60f341fb383218526a826f478e = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_11f152b3147d2873fbee01bf54d057c2 = $(`<div id="html_11f152b3147d2873fbee01bf54d057c2" style="width: 100.0%; height: 100.0%;">Bus 22: WAIPAHU138<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_26722a60f341fb383218526a826f478e.setContent(html_11f152b3147d2873fbee01bf54d057c2);
            
        

        circle_2eabaee95983e2b3526a285ec1f95541.bindPopup(popup_26722a60f341fb383218526a826f478e)
        ;

        
    
    
            circle_2eabaee95983e2b3526a285ec1f95541.bindTooltip(
                `<div>
                     WAIPAHU138 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_a4448243964b28bef934539cea4c0fdb = L.circle(
                [21.417469, -157.983838],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_b7237f326b74bf6971c9011a45ebd8b9 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_05ce5be45c7f93e42000d5fbecabd4de = $(`<div id="html_05ce5be45c7f93e42000d5fbecabd4de" style="width: 100.0%; height: 100.0%;">Bus 23: WAIPAHU69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_b7237f326b74bf6971c9011a45ebd8b9.setContent(html_05ce5be45c7f93e42000d5fbecabd4de);
            
        

        circle_a4448243964b28bef934539cea4c0fdb.bindPopup(popup_b7237f326b74bf6971c9011a45ebd8b9)
        ;

        
    
    
            circle_a4448243964b28bef934539cea4c0fdb.bindTooltip(
                `<div>
                     WAIPAHU69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_6927d0c31c08a8e405a2856e304ab9f0 = L.circle(
                [21.363106, -158.082206],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_04dd2c854158cd4ea107e8dc0045ccb3 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_bffcbb6374bf4134ec80df4e5eec1058 = $(`<div id="html_bffcbb6374bf4134ec80df4e5eec1058" style="width: 100.0%; height: 100.0%;">Bus 24: KAPOLEI69<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_04dd2c854158cd4ea107e8dc0045ccb3.setContent(html_bffcbb6374bf4134ec80df4e5eec1058);
            
        

        circle_6927d0c31c08a8e405a2856e304ab9f0.bindPopup(popup_04dd2c854158cd4ea107e8dc0045ccb3)
        ;

        
    
    
            circle_6927d0c31c08a8e405a2856e304ab9f0.bindTooltip(
                `<div>
                     KAPOLEI69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_5bf13ce3c04f54ff03e51f8485a480e5 = L.circle(
                [21.344756, -158.022282],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_e9b5f0132a2a927ec3a9b053888ea4d9 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_98606b552e2b6b2b43e7e1ab35fd1e1d = $(`<div id="html_98606b552e2b6b2b43e7e1ab35fd1e1d" style="width: 100.0%; height: 100.0%;">Bus 25: EWA BEACH138<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_e9b5f0132a2a927ec3a9b053888ea4d9.setContent(html_98606b552e2b6b2b43e7e1ab35fd1e1d);
            
        

        circle_5bf13ce3c04f54ff03e51f8485a480e5.bindPopup(popup_e9b5f0132a2a927ec3a9b053888ea4d9)
        ;

        
    
    
            circle_5bf13ce3c04f54ff03e51f8485a480e5.bindTooltip(
                `<div>
                     EWA BEACH138 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_b53a2124da0fba451a77ad13b3a70e59 = L.circle(
                [21.344756, -158.022282],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_af96f515498a4f10ee58daf8e81fac00 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_e82f87a3a00d4fa641b2d65655b5c9aa = $(`<div id="html_e82f87a3a00d4fa641b2d65655b5c9aa" style="width: 100.0%; height: 100.0%;">Bus 26: EWA BEACH69<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_af96f515498a4f10ee58daf8e81fac00.setContent(html_e82f87a3a00d4fa641b2d65655b5c9aa);
            
        

        circle_b53a2124da0fba451a77ad13b3a70e59.bindPopup(popup_af96f515498a4f10ee58daf8e81fac00)
        ;

        
    
    
            circle_b53a2124da0fba451a77ad13b3a70e59.bindTooltip(
                `<div>
                     EWA BEACH69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_ac022421fae85b789f5288606dacd427 = L.circle(
                [21.658692, -157.978792],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_d09b6e583c18c8475ea5a8271eeb9402 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_0c9ffe60e7ab3ddf31731dbae591f05e = $(`<div id="html_0c9ffe60e7ab3ddf31731dbae591f05e" style="width: 100.0%; height: 100.0%;">Bus 27: KAHUKU69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_d09b6e583c18c8475ea5a8271eeb9402.setContent(html_0c9ffe60e7ab3ddf31731dbae591f05e);
            
        

        circle_ac022421fae85b789f5288606dacd427.bindPopup(popup_d09b6e583c18c8475ea5a8271eeb9402)
        ;

        
    
    
            circle_ac022421fae85b789f5288606dacd427.bindTooltip(
                `<div>
                     KAHUKU69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_859d13a641dce02935d61530ca9b760f = L.circle(
                [21.621367, -158.048011],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_12a366fb9d95a6cc13683bb34d306df9 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_79136b245eb120eaa955167522e25e53 = $(`<div id="html_79136b245eb120eaa955167522e25e53" style="width: 100.0%; height: 100.0%;">Bus 28: HALEIWA69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_12a366fb9d95a6cc13683bb34d306df9.setContent(html_79136b245eb120eaa955167522e25e53);
            
        

        circle_859d13a641dce02935d61530ca9b760f.bindPopup(popup_12a366fb9d95a6cc13683bb34d306df9)
        ;

        
    
    
            circle_859d13a641dce02935d61530ca9b760f.bindTooltip(
                `<div>
                     HALEIWA69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_c775a2936659b2d813a10bc6263a7dea = L.circle(
                [21.618479, -157.943953],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_772ad933f6c5f3d76a85aa732429f706 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_fdc67122d9b472eb16fbec0c9a23062c = $(`<div id="html_fdc67122d9b472eb16fbec0c9a23062c" style="width: 100.0%; height: 100.0%;">Bus 29: LAIE69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_772ad933f6c5f3d76a85aa732429f706.setContent(html_fdc67122d9b472eb16fbec0c9a23062c);
            
        

        circle_c775a2936659b2d813a10bc6263a7dea.bindPopup(popup_772ad933f6c5f3d76a85aa732429f706)
        ;

        
    
    
            circle_c775a2936659b2d813a10bc6263a7dea.bindTooltip(
                `<div>
                     LAIE69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_08502a982bfc2d5b2db07bf81f691976 = L.circle(
                [21.57139, -157.979384],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_588664ec9dedcde5c93576a0cc49a30a = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_5b8f8197695cb24c5424876a0ce64a1b = $(`<div id="html_5b8f8197695cb24c5424876a0ce64a1b" style="width: 100.0%; height: 100.0%;">Bus 30: WAHIAWA69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_588664ec9dedcde5c93576a0cc49a30a.setContent(html_5b8f8197695cb24c5424876a0ce64a1b);
            
        

        circle_08502a982bfc2d5b2db07bf81f691976.bindPopup(popup_588664ec9dedcde5c93576a0cc49a30a)
        ;

        
    
    
            circle_08502a982bfc2d5b2db07bf81f691976.bindTooltip(
                `<div>
                     WAHIAWA69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_ff43f3e302cc4687abdc67efdbc70b36 = L.circle(
                [21.56364, -158.185151],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "orange", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_975730a57cbd8a0dee2e7e05b13348f2 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_dbf52ca6cc7c772280716bddaf87093b = $(`<div id="html_dbf52ca6cc7c772280716bddaf87093b" style="width: 100.0%; height: 100.0%;">Bus 31: WAIALUA69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: orange<br>Updated: 13:58:28</div>`)[0];
                popup_975730a57cbd8a0dee2e7e05b13348f2.setContent(html_dbf52ca6cc7c772280716bddaf87093b);
            
        

        circle_ff43f3e302cc4687abdc67efdbc70b36.bindPopup(popup_975730a57cbd8a0dee2e7e05b13348f2)
        ;

        
    
    
            circle_ff43f3e302cc4687abdc67efdbc70b36.bindTooltip(
                `<div>
                     WAIALUA69 - orange
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_14dd9e2054a15435299fc1d11489ce06 = L.circle(
                [21.55775, -157.905396],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_dd9107fde4bd0d2f3951471825fc6d96 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_71f8aca4d9a16a8dc3907dea3c5fac7b = $(`<div id="html_71f8aca4d9a16a8dc3907dea3c5fac7b" style="width: 100.0%; height: 100.0%;">Bus 32: HAUULA69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_dd9107fde4bd0d2f3951471825fc6d96.setContent(html_71f8aca4d9a16a8dc3907dea3c5fac7b);
            
        

        circle_14dd9e2054a15435299fc1d11489ce06.bindPopup(popup_dd9107fde4bd0d2f3951471825fc6d96)
        ;

        
    
    
            circle_14dd9e2054a15435299fc1d11489ce06.bindTooltip(
                `<div>
                     HAUULA69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_941e83f340d7b759125daac12cc964e1 = L.circle(
                [21.468626, -158.166919],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_352a1596ebed910cc6f8bdb13ecfc024 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_6eba3599a541c5e7e660ebc4c1ba269b = $(`<div id="html_6eba3599a541c5e7e660ebc4c1ba269b" style="width: 100.0%; height: 100.0%;">Bus 33: WAIANAE69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_352a1596ebed910cc6f8bdb13ecfc024.setContent(html_6eba3599a541c5e7e660ebc4c1ba269b);
            
        

        circle_941e83f340d7b759125daac12cc964e1.bindPopup(popup_352a1596ebed910cc6f8bdb13ecfc024)
        ;

        
    
    
            circle_941e83f340d7b759125daac12cc964e1.bindTooltip(
                `<div>
                     WAIANAE69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_28098d43f0732a3ef7c3cb02b833504d = L.circle(
                [21.4785, -158.0581],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_2802c0797b6c9c7515448de29b4339b8 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_93173cb7316d39bcc9d1533862ceadc1 = $(`<div id="html_93173cb7316d39bcc9d1533862ceadc1" style="width: 100.0%; height: 100.0%;">Bus 34: SCHOFIELD69<br>Temp: 23.5°C<br>Wind: 11.16 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_2802c0797b6c9c7515448de29b4339b8.setContent(html_93173cb7316d39bcc9d1533862ceadc1);
            
        

        circle_28098d43f0732a3ef7c3cb02b833504d.bindPopup(popup_2802c0797b6c9c7515448de29b4339b8)
        ;

        
    
    
            circle_28098d43f0732a3ef7c3cb02b833504d.bindTooltip(
                `<div>
                     SCHOFIELD69 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_523344a7c636b02a996d0a24ee261e03 = L.circle(
                [21.303419, -158.106528],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_a60f83e12b9a0befdced2ab079569119 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_92063b042a44a1b71c052ef33d8e1d27 = $(`<div id="html_92063b042a44a1b71c052ef33d8e1d27" style="width: 100.0%; height: 100.0%;">Bus 35: KALAELOA138<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: red<br>Updated: 13:58:28</div>`)[0];
                popup_a60f83e12b9a0befdced2ab079569119.setContent(html_92063b042a44a1b71c052ef33d8e1d27);
            
        

        circle_523344a7c636b02a996d0a24ee261e03.bindPopup(popup_a60f83e12b9a0befdced2ab079569119)
        ;

        
    
    
            circle_523344a7c636b02a996d0a24ee261e03.bindTooltip(
                `<div>
                     KALAELOA138 - red
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_a1e84c41b9ebe8bccca37a6595e65363 = L.circle(
                [21.311667, -158.113889],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_c2a8b060d561cf416cd066035a1284a0 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_427f598242ef8ba10400b8d6ae544a28 = $(`<div id="html_427f598242ef8ba10400b8d6ae544a28" style="width: 100.0%; height: 100.0%;">Bus 36: COGEN69<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_c2a8b060d561cf416cd066035a1284a0.setContent(html_427f598242ef8ba10400b8d6ae544a28);
            
        

        circle_a1e84c41b9ebe8bccca37a6595e65363.bindPopup(popup_c2a8b060d561cf416cd066035a1284a0)
        ;

        
    
    
            circle_a1e84c41b9ebe8bccca37a6595e65363.bindTooltip(
                `<div>
                     COGEN69 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
    
            var circle_6b4b885093eace5d036bc70351713760 = L.circle(
                [21.356395, -158.128853],
                {"bubblingMouseEvents": true, "color": "black", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "green", "fillOpacity": 1, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 1000, "stroke": true, "weight": 1}
            ).addTo(map_87fdf8d4bf63de14c04a79108d2593c2);
        
    
        var popup_01218b7b9e9a90bc2a94351e92ff6029 = L.popup({
  "maxWidth": "100%",
});

        
            
                var html_77ed16caaaba7333a57148cb57a57fe8 = $(`<div id="html_77ed16caaaba7333a57148cb57a57fe8" style="width: 100.0%; height: 100.0%;">Bus 37: KAHE138<br>Temp: 24.4°C<br>Wind: 5.4 m/s<br>Color: green<br>Updated: 13:58:28</div>`)[0];
                popup_01218b7b9e9a90bc2a94351e92ff6029.setContent(html_77ed16caaaba7333a57148cb57a57fe8);
            
        

        circle_6b4b885093eace5d036bc70351713760.bindPopup(popup_01218b7b9e9a90bc2a94351e92ff6029)
        ;

        
    
    
            circle_6b4b885093eace5d036bc70351713760.bindTooltip(
                `<div>
                     KAHE138 - green
                 </div>`,
                {
  "sticky": true,
}
            );
        
</script>
</html>