<html>  
  <head>  
    <title>K-means</title>
    <script type="text/javascript">  
	var k=1;
	var xr = 50;
	var yr = 50;
	var ax = [22,45,12,53,37,25,8,31,42,11,27,45];
	var ay = [72,54,48,83,96,67,46,82,58,66,74,86];
	var az = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	//
	var bx = [63,82,74,58,92,63,78,71,85,54,67,71];
	var by = [30,26,48,52,12,27,18,36,24,15,34,44];
	var bz = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
function doit1(rx) {
  xr = rx;
  draw();
}
//
function doit2(ry) {
  yr = ry;
  draw();
}
//

function drawLine(x1,y1,x2,y2) { 
	var canvas = document.getElementById('fry1');  
        	if (canvas.getContext){  
                       var gS2 = canvas.getContext('2d');  
            	}  
	gS2.lineWidth=1;
	gS2.beginPath();  
	gS2.moveTo(x1,y1);
	gS2.lineTo(x2,y2);
	gS2.closePath;
  	gS2.stroke();
}
//
function drawRect(x1,y1,x2,y2) {
	var canvas = document.getElementById('fry1');  
        	if (canvas.getContext){  
                        var gS2 = canvas.getContext('2d');  
            	}  
                    gS2.beginPath();
	gS2.moveTo(x1,y1);
	gS2.lineTo(x1+x2,y1);
	gS2.lineTo(x1+x2,y1+y2);
	gS2.lineTo(x1,y1+y2);
	gS2.closePath();
	gS2.stroke();
}
function round_1(dnr) {
temp = Math.round(dnr*100.0)/100.0;
			return(temp);
			}
//
          function draw() {  
            	var canvas = document.getElementById('fry1');  
            	if (canvas.getContext){  
               	    var gS2 = canvas.getContext('2d');  
            	}  
			//
			// Coordinate system
			// 
			gS2.fillStyle = "rgb(248,248,248)";
			gS2.fillRect(0,0,500,400);
			//
			gS2.fillStyle = "rgb(240,240,240)";
			gS2.fillRect(0,0,500,20);
			//
			gS2.strokeStyle = "rgb(164,164,164)";
			gS2.lineWidth=2;
			drawLine(0,21,500,21);
			//
			//  chart
			//
			gS2.strokeStyle = "rgb(100,150,220)";
			drawRect(80,100,200,200);
			gS2.fillStyle = "rgb(240,240,240)";
			gS2.fillRect(81,101,198,198);
			gS2.strokeStyle = "rgb(255,255,255)";
			//
			gS2.lineWidth=1;
			for (i=0;i<100;i=i+5) {
			    drawLine(81,100+i*2,279,100+i*2);
			}
			for (i=0;i<100;i=i+5) {
			    drawLine(80+i*2,101,80+i*2,299);
			}
			//
			gS2.fillStyle = "rgb(0,0,128)";
			gS2.font = "bold 10px Arial"; 
			for (i=0;i<110;i=i+10) {
			  width = gS2.measureText(i+"").width;
			  gS2.fillText(i+"",(85+i*2)-width,315);
			}
			//
			for (i=0;i<110;i=i+10) {
			  width = gS2.measureText(i+"").width;
			  gS2.fillText(i+"",75-width,305-i*2);
			}
			//
			var sum_ax = 0.0;
			var sum_ay = 0.0;
			var mean_ax = 0.0;
			var mean_ay = 0.0;
			gS2.fillStyle = "rgb(0,225,0)";
			for (i=0;i<10;i++) {
			  gS2.fillRect(80+ax[i]*2-1,300-ay[i]*2-1,5,5);
			  sum_ax = sum_ax + ax[i];
			  sum_ay = sum_ay + ay[i];
			}
			mean_ax = sum_ax/10;
			mean_ay = sum_ay/10;
			//
			// gS2.fillStyle = "rgb(0,0,225)";
			var sum_bx = 0.0;
			var sum_by = 0.0;
			var mean_bx = 0.0;
			var mean_by = 0.0;
			for (i=0;i<10;i++) {
			  gS2.fillRect(80+bx[i]*2-1,300-by[i]*2-1,5,5);
			  sum_bx = sum_bx + bx[i];
			  sum_by = sum_by + by[i];
			}
			mean_bx = sum_bx/10;
			mean_by = sum_by/10;
			//
			gS2.strokeStyle = "rgb(0,0,0)";
			gS2.lineWidth=1;
			drawLine(80+(xr*2),101,80+(xr*2),299);
			drawLine(81,300-(yr*2),279,300-(yr*2));
			gS2.fillStyle = "rgb(0,128,128)";
			gS2.fillRect(76+(xr*2),295-(yr*2),7,7);
			//
			var distance = 0.0;
			//
			//for (i=0;i< 10;i++) {
			// distance = distance + Math.pow((Math.pow((ax[i] - xr),2)+Math.pow((ay[i]-yr),2)),0.5);
			// distance = distance + Math.pow((Math.pow((bx[i] - xr),2)+Math.pow((by[i]-yr),2)),0.5);
			//}
			//
			if (xr != 50 || yr != 50) {
			//
			var distance_a = 0.0;
			var distance_b = 0.0;
			for (i=0;i<10;i++) {
			  distance_a = Math.pow((Math.pow((ax[i] - xr),2)+Math.pow((ay[i]-yr),2)),0.5);
			  for (j=0;j<10;j++) {
			    distance_b = Math.pow((Math.pow((bx[j] - xr),2)+Math.pow((by[j]-yr),2)),0.5);
				//	  
			    if (distance_a < distance_b) {
			       az[i] = -1;
			       bz[j] = 1;
			    }   
			    else {
			       az[i] = 1;
			       bz[j] = -1;
			    }   
			  }
			}
			//
			for (i=0;i<10;i++) {
			  if (az[i] > 0) {
			    gS2.fillStyle = "rgb(225,0,225)";
			  }
			  if (az[i] < 0) {
			    gS2.fillStyle = "rgb(0,225,225)";
			  }
			  gS2.fillRect(80+ax[i]*2-1,300-ay[i]*2-1,5,5);
			}
			//
			for (j=0;j<10;j++) {
			  if (bz[j] > 0) {
			    gS2.fillStyle = "rgb(225,0,225)";
			  }
			  if (bz[j] < 0) {
			    gS2.fillStyle = "rgb(0,225,225)";
			  }
			  gS2.fillRect(80+bx[j]*2-1,300-by[j]*2-1,5,5);
			}
			//
			sum_ax = 0.0;
			sum_ay = 0.0;
			var count_a = 0;
			sum_bx = 0.0;
			sum_by = 0.0;
			var count_b = 0;
			//
			for (i=0;i<10;i++) {
			  if (az[i] < 0) {
			     sum_ax = sum_ax + ax[i];
			     sum_ay = sum_ay + ay[i];
			     count_a = count_a+1;
			  }
			  if (az[i] > 0) {
			     sum_bx = sum_bx + ax[i];
			     sum_by = sum_by + ay[i];
			     count_b = count_b+1;
			  }
			  //
			  if (bz[i] < 0) {
			     sum_ax = sum_ax + ax[i];
			     sum_ay = sum_ay + ay[i];
			     count_a = count_a+1;
			  }
			  if (bz[i] > 0) {
			     sum_bx = sum_bx + bx[i];
			     sum_by = sum_by + by[i];
			     count_b = count_b+1;
			  }
			}
			mean_ax = sum_ax/count_a;
			mean_ay = sum_ay/count_a;
			mean_bx = sum_bx/count_b;
			mean_by = sum_by/count_b;
			//
			distance = 0.0;
			// problem when ax = mean_ax...
			for (i=0;i< count_a;i++) {
			  distance = distance + Math.pow((Math.pow((ax[i] - mean_ax),2)+Math.pow((ay[i]-mean_ay),2)),0.5);
			}
			for (i=0;i< count_b;i++) {  
			  distance = distance + Math.pow((Math.pow((bx[i] - mean_bx),2)+Math.pow((by[i]-mean_by),2)),0.5);
			}
			}
			//
			gS2.fillStyle = "rgb(0,0,128)";
			gS2.font = "bold 12px Arial";
			gS2.fillText("Group A",350,60);
			gS2.fillText("Group B",420,60);
			gS2.fillStyle = "rgb(0,0,0)";
			gS2.font = "12px Arial";
			for (i=0;i<10;i++) {
			  gS2.fillText(""+i,300,75+i*15);
			  gS2.fillText(""+az[i],360,75+i*15);
			  gS2.fillText(""+bz[i],430,75+i*15);
			}
			//
			mean_ax = round_1(mean_ax);
			mean_ay = round_1(mean_ay);
			mean_bx = round_1(mean_bx);
			mean_by = round_1(mean_by);
			//
			gS2.font = "bold 12px Arial";
			gS2.fillText("Means:",290,240);
			gS2.fillText("("+mean_ax+" , "+mean_ay+")",335,240);
			gS2.fillText("("+mean_bx+" , "+mean_by+")",405,255);
			gS2.fillText("[a: "+count_a+"]  [b: "+count_b+"]",340,300);
			//
			gS2.fillStyle = "rgb(0,0,255)";
			gS2.fillRect(80+mean_ax*2-2,300-mean_ay*2-2,5,5);
			gS2.fillStyle = "rgb(255,0,0)";
			gS2.fillRect(80+mean_bx*2-2,300-mean_by*2-2,5,5);
			temp = Math.round(distance*1000.0)/1000.0;
			distance = temp;
			gS2.font = "12px Arial";
			gS2.fillStyle = "rgb(128,0,0)";
			gS2.fillText("K-Means",200,15);
			gS2.fillText("Distance= "+distance,100,60);
			gS2.fillText("",100,55);
			gS2.font = "bold 12px Arial";
			gS2.fillText("X",300,310);
			gS2.fillText("Y",80,92);
			
	}  
      </script>  

      <style type="text/css">  
            canvas { border: 0px solid black; }  
      </style>  
</head>  

<body onload="draw();">
<form>

<table border = "0" >
  <tr>
    <td colspan="2">
      <canvas id="fry1" width="500" height="400" bgcolor="white">No support for the HTML5 object!</canvas>  
    </td>
  </tr>
  <tr>
    <td bgcolor="#dfdfdf" align="center" width="500" valign="top">
    <font color = "maroon" face="Arial" size = "-1">X: </font><input name="xr" type="range" onchange="doit1(this.form.xr.value)" min="1.0" max="99.0" value="50" step="1"/><br/>
    <font color = "maroon" face="Arial" size = "-1">Y: </font><input name="yr" type="range" onchange="doit2(this.form.yr.value)" min="1.0" max="99.0" value="50" step="1"/>
    </td>
  </tr>

 
</table>
</form>
</body>  
</html> 