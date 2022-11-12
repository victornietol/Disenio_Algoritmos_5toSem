class linea{
  punto a;
  punto b;
  linea(punto w,punto e){
    a=w;
    b=e;
  }
  void dibuja(){
    line(a.x,a.y,b.x,b.y);
  }
  float pendiente(){
    return (a.y-b.y)/(a.x-b.x);
  }
}
