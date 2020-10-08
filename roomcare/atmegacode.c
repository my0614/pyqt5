
#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#include <stdio.h>
#include <string.h>
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>

int state = 0;
char arr[15];
char data2[10];
int i=0;
void uart_init(unsigned int baud)
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) |			(1<<RXCIE0);
}

void uart_write(unsigned char data)
{
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}
#define DHT11_PIN 6
uint8_t c=0,I_RH,D_RH,I_Temp,D_Temp,CheckSum;

void Request()				// ATMega128로 스타트 펄스 전달 & 응답 과정
{
	DDRD |= (1<<DHT11_PIN);
	PORTD &= ~(1<<DHT11_PIN);	// PD4 LOW
	_delay_ms(20);
	PORTD |= (1<<DHT11_PIN);	// PD4 HIGH
}

void Response()				// 온습도 센서로부터 응답
{
	DDRD &= ~(1<<DHT11_PIN);     // PD4 LOW
	while(PIND & (1<<DHT11_PIN));
	while((PIND & (1<<DHT11_PIN))==0);
	while(PIND & (1<<DHT11_PIN));
}

uint8_t Receive_data()
{
	for (int q=0; q<8; q++)
	{
		while((PIND & (1<<DHT11_PIN)) == 0);  //비트가 0인지 1인지 체크
		_delay_us(30);
		if(PIND & (1<<DHT11_PIN))    //HIGH가 30ms보다 크면
		c = (c<<1)|(0x01);	      //HIGH 상태
		else
		c = (c<<1);                    //LOW 상태
		while(PIND & (1<<DHT11_PIN));
	}
	return c;
}
void dht11()
{
	
	Request();		         //시작 펄스 신호 보냄
	Response();		         //센서로부터 응답 받음
	data2[0] = '0x02';
	I_RH=Receive_data();         //습도의 정수 부분
	data2[1] = I_RH;
	D_RH=Receive_data();	         //습도의 실수 부분
	data2[2] = D_RH;
	I_Temp=Receive_data();
	data2[3] = I_Temp;	         //온도의 정수 부분
	D_Temp=Receive_data();
	data2[4] = D_Temp;         //온도의 실수 부분
	CheckSum=Receive_data();       //모든 세그먼트의 체크섬
	data2[5] = CheckSum;
	data2[6] = '0x03';
	
	if ((I_RH + D_RH + I_Temp + D_Temp) != CheckSum)
	{
		//에러
		
	}
	
	else
	{
		//itoa(I_RH,data2[0],10);
		UDR0 = data2[0];
		
		//itoa(D_RH,data2[1],10);
		UDR0 = data2[1];

		//itoa(I_Temp,data2[2],10);
		UDR0 = data2[2];
		
		//itoa(D_Temp,data2[3],10);
		UDR0 = data2[3];
		
		//itoa(CheckSum,data2[4],10);
		UDR0 = data2[4];
		
	
	
	}
	
}
int main(void)
{
	DDRC = 0xff;
	DDRF = 0xff;
	DDRD = 0xff;
	
	uart_init(BAUDRATE(9600));
	sei();
	while(1)
	{
		
		if(strcmp(arr,"LIVINGN") ==0)
		{
			PORTF = 0x00;
			memset(arr,0,15);
		}
		
		if(strcmp(arr,"LIVINGF") ==0)
		{
			PORTF = 0xff;
			memset(arr,0,15);
		}
		
		if(strcmp(arr,"BATHN") ==0)
		{
			PORTC = 0x00;
			memset(arr,0,15);
		}
		
		if(strcmp(arr,"BATHF") ==0)
		{
			PORTC = 0xff;
			memset(arr,0,15);
			
		}
		
		if(strcmp(arr,"KITCHEN") ==0)
		{
			PORTD = 0x00;
			memset(arr,0,15);
			
		}
		
		if(strcmp(arr,"KITCHEF") ==0)
		{
			PORTD = 0xff;
			memset(arr,0,15);
		}
		
		_delay_ms(100);
		
	}
}


ISR(USART0_RX_vect)
{
	unsigned char buf = UDR0;
	switch(buf)
	{
		case 0x02 : state = 1; return;
		case 0x03 : state = 0; i = 0;break;
	}
	if(state == 1)
	{
		arr[i] = buf;
		i++;
	}
	
	
}

