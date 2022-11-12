int np=10,auxPunto=1;
punto p[],MX,MY,mX,mY,ref,pCierre[],pTemp;
linea cierre[],pendiente;
float penm=0.0,penM=0.0,penTemp=0.0;
void setup(){
  size(1200,800);
  p=new punto[np];
  for (int i=0;i<np;i++){
    p[i]=new punto(10+random(1180),10+random(780),color(0));
    pCierre=new punto[np]; //   <--- Puntos finales de cierre
  }
  //Su código o el algoritmo inicia aqui
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
  
  MX.setColor(color(255,0,0));
  MY.setColor(color(255,0,0));
  mX.setColor(color(255,0,0));
  mY.setColor(color(255,0,0));

  
  // Cierre apartir de los puntos finales en pCierre
  
  // 2.
  ref = mX;
  pCierre[0]=mX;
 
  do{ // 4.
    //3.
    for(int i=0;i<np;i++){
      System.out.println("auxPunto(PrimerBucle) "+auxPunto);
      if(ref.x<p[i].x){
        System.out.println("ref.x: "+ref.x+" p.x: "+p[i].x);
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        //System.out.println("penM: "+penM+"penTemp: "+penTemp);
        if(penM>penTemp){
          pTemp = p[i];  // Asignando el punto temporal para hacer validaciones en lo que se sale del for
          penM = penTemp;
          System.out.println("ENCONTRADO");
        }  
      }else{
        System.out.println("ES IGUAL\nref.x: "+ref.x+" p.x: "+p[i].x);
        System.out.println("ref.y: "+ref.y+" p.y: "+p[i].y);
      }
    }
    penTemp = 0.0;
    penM = 0.0;
    ref = pTemp;  // Asignando nueva referencia para siguiente iteración
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   // color del punto encontrado
    auxPunto++; // Se va aumentando el índice del punto para ir agregando los nuevos
    System.out.println("ref.y: "+ref.y+" MY.y: "+MY.y);
  }while(ref.y != MY.y);





  // 5.
  ref = mX;
  
  do{ // 7.
    //6.
    for(int i=0;i<np;i++){
      System.out.println("auxPunto(segundoBucle) "+auxPunto);
      if( (ref.x<p[i].x) ){
        System.out.println("ref.x: "+ref.x+" p.x: "+p[i].x);
        linea pendiente=new linea(ref,p[i]);
        penTemp = pendiente.pendiente();
        // System.out.println("penm: "+penm+"penTemp: "+penTemp);
        if(penm<penTemp){
          pTemp = p[i];  // Asignando el punto temporal para hacer validaciones en lo que se sale del for
          penm = penTemp;
          System.out.println("ENCONTRADO");
        }  
      }else{
        System.out.println("ES IGUAL\nref.x: "+ref.x+" p.x: "+p[i].x);
        System.out.println("ref.y: "+ref.y+" p.y: "+p[i].y);
      }
    }
    penTemp = 0.0;
    penm = 0.0;
    ref = pTemp;  // Asignando nueva referencia para siguiente iteración
    pCierre[auxPunto] = pTemp;
    pCierre[auxPunto].setColor(color(0,255,0));   // color del punto encontrado
    auxPunto++; // Se va aumentando el índice del punto para ir agregando los nuevos
    System.out.println("ref.y: "+ref.y+" mY.y: "+mY.y);
  }while(ref.y != mY.y);  

  
}

void draw(){
  background(255);
  for (int i=0;i<np;i++){
    p[i].dibuja();
    
    
    //linea l=new linea(pCierre[0],pCierre[1]);
    //l.dibuja();
    // <----- Dibujar los puntos del contorno de otro color
   
    if((pCierre[i]!=null) && i>0 ){    //    <---- Asi se dibujaria la linea del contorno final
/*      linea l=new linea(pCierre[i-1],pCierre[i]);
      l.dibuja();*/
      pCierre[i].dibuja();
    }
  }

  MX.dibuja();
  MY.dibuja();
  mX.dibuja();
  mY.dibuja();
  
}
