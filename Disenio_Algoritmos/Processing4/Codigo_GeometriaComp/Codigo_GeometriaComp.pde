int np=100,auxPunto=1;
punto p[],MX,MY,mX,mY,ref,pCierre[],pTemp;
linea cierre[],pendiente;
float penm=0.0,penM=0.0,penTemp=0.0;

void setup(){
  size(1200,800);
  p=new punto[np];
  pCierre=new punto[np];  
  cierre=new linea[np];
  for (int i=0;i<np;i++){
    p[i]=new punto(10+random(1180),10+random(780),color(0));
  }

  MX=p[0];
  MY=p[0];
  mX=p[0];
  mY=p[0];
  
  for(int i=1;i<np;i++){
    if(MX.x<p[i].x){
      MX=p[i];
    }
    if(MY.y>p[i].y){  
      MY=p[i];
    }
    if(mX.x>p[i].x){
      mX=p[i];
    }
    if(mY.y<p[i].y){   
      mY=p[i];
    }
  }
  
  
  // 2.
  ref = mX;
  pCierre[0]=mX;
 
  do{ // 4.
    // 3.
    for(int i=0;i<np;i++){
      if(ref.x<p[i].x){
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        if(penM>penTemp){
          pTemp = p[i];
          penM = penTemp;
          cierre[auxPunto-1] = pendiente;
        }  
      }else{
        ;
      }
    }
    penTemp = 0.0;
    penM = 0.0;
    ref = pTemp;  
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   
    auxPunto++; 
  }while(ref.y != MY.y);
 

  // 5.
  ref = mX;
  
  do{ // 7.
    // 6.
    for(int i=0;i<np;i++){
      if( (ref.x<p[i].x) ){
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        if(penm<penTemp){
          pTemp = p[i];  
          penm = penTemp;
          cierre[auxPunto-1] = pendiente;
        }  
      }else{
        ;
      }
    }
    penTemp = 0.0;
    penm = 0.0;
    ref = pTemp;  
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   
    auxPunto++; 
  }while(ref.y != mY.y);  


  // 8.
  ref = MX;
 
  do{ // 10.
    //9.
    for(int i=0;i<np;i++){
      if(ref.x>p[i].x){
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        if(penm<penTemp){
          pTemp = p[i];  
          penm = penTemp;
          cierre[auxPunto-1] = pendiente;
        }  
      }else{
        ;
      }
    }
    penTemp = 0.0;
    penm = 0.0;
    ref = pTemp;  
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   
    auxPunto++; 
  }while(ref.y != MY.y);  


  // 11.
  ref = MX;
 
  do{ // 10.
    //9.
    for(int i=0;i<np;i++){
      if(ref.x>p[i].x){
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        if(penM>penTemp){
          pTemp = p[i];  
          penM = penTemp;
          cierre[auxPunto-1] = pendiente;
        }  
      }else{
        ;
      }
    }
    penTemp = 0.0;
    penM = 0.0;
    ref = pTemp;  
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   
    auxPunto++; 
  }while(ref.y != mY.y);   

  
}

void draw(){
  background(255);
  for (int i=0;i<np;i++){
    p[i].dibuja();
   
    if(cierre[i] != null){   // Dibujando las lineas de cierre
      cierre[i].dibuja();
    }   
    if((pCierre[i]!=null) && i>0 ){    // Dibujando los puntos de cierre
      pCierre[i].dibuja();
    }
  }
   
  MX.setColor(color(255,0,0));
  MY.setColor(color(255,0,0));
  mX.setColor(color(255,0,0));
  mY.setColor(color(255,0,0));

  MX.dibuja();
  MY.dibuja();
  mX.dibuja();
  mY.dibuja();
  
}
