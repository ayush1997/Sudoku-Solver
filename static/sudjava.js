var grid=[
       [['','','',5,'','',4,'',3],
       ['',7,6,'','','','','','']
 ,     ['','','','','',8,'','',2]
 ,     [2,'','',7,'','',3,1,''],
       ['','','','','',1,'','',6],
       [6,'','','',2,'','','','']
 ,     ['','',2,'',7,'','',6, '']
 ,     [5,'','','','','','',3,''],
       [1,'','','','',3,'',2,'']]  ,


      [ [1,2,3,4,5,6,7,8,9],
       ['',7,6,'','','','','','']
 ,     ['','','','','',8,'','',2]
 ,     [2,'','',7,'','',3,1,''],
       ['','','','','',1,'','',6],
       [6,'','','',2,'','','','']
 ,     ['','',2,'',7,'','',6, '']
 ,     [5,'','','','','','',3,''],
       [1,'','','','',3,'',2,''] ] ,

       [[2,'','',5,'','',7,'',3],
       ['',7,6,'','','','','','']
 ,     ['','','','','',8,'','',2]
 ,     [2,'','',7,'','',3,1,''],
       ['','','','','',1,'','',6],
       ['','','','',2,'','','','']
 ,     ['','',2,'',7,'','',6, '']
 ,     [5,'','','','','','',3,''],
       [1,'','','','',3,'',2,'']  ] 
      ];

var r,c;
var len  =grid.length;
var i=0;
function display()
{
	
	for(r=0;r<9;r++)
		{for(c=0;c<9;c++)
			{	var row = r.toString();
				var col = c.toString();
				var id = row+col;
				document.getElementById(id).innerHTML = grid[i][r][c];
			}
		}
	if(i!=len-1)
		{i++;}
	else
		{i=0;}
	

}


setInterval(display,1500);


 
