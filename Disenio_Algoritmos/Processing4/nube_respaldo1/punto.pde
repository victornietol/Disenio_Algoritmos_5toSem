class punto{
  float x;
  float y;
  color c;
  punto(float a,float b,color d){
    x=a;
    y=b;
    c=d;
  }
  void setColor(color k){
    c=k;
  }
  void dibuja(){
    fill(c);
    circle(x,y,15);
  }
}
