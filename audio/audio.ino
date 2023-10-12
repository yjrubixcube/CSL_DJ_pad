#define button 7
#define volume A4
#define max_volume 800
#define min_volume 200

bool prev_b = 0;
bool music_state = 0;
int prev_v = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(volume, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  bool b = digitalRead(button);
  int v = analogRead(volume);
  if (music_state){
    digitalWrite(13, HIGH);
    analogWrite(11, prev_v/4);
  }
  else{
    digitalWrite(13, LOW);
     analogWrite(11, 0);
  }
  // if (music_state) digitalWrite(13, HIGH);
  // else digitalWrite(13, LOW);
  
  if(prev_b != b && b){
    music_state = !music_state;
    Serial.print(music_state);
    Serial.print("\n");
  }
  prev_b = b;
  
  if(abs(prev_v - v) > 60){
    Serial.print("v\n");
    Serial.println(v);
    
    if (v > max_volume && !music_state && prev_v <= max_volume){
      Serial.print("1\n");

      music_state = 1;
    }
    else if (v < min_volume && music_state && prev_v >= min_volume){
      Serial.print("0\n");

      music_state = 0;
    }
    prev_v = v;
    

  }
  
  delay(10);
}
