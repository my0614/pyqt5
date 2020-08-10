#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#include <stdio.h>
#include <string.h>
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>

volatile char speed = 0;
volatile char speed2 =0;
int state = 0;
char arr[10];
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

void DC_Motor(int speed)
{
	if(speed<  0) speed=  0;
	if(speed>100) speed=100;
	OCR1A=speed;
}

void DC_Motor2(int speed2)
{
	if(speed2 < 0) speed2 = 0;
	if(speed2 > 100) speed2 = 100;
	OCR3A = speed2;
}

int main(void)
{
	DDRA = 0xff;
	int i,value=0;
	DDRB=0x60;
	
	TCCR1B=0x1A;
	TCCR1A=0x82; // 모터1
	OCR1A=50; // 모터 1
	OCR1A=50; //모터1
	ICR1=100;
	
	DDRE = 0x08;
	OCR3A = 50; // 모터2
	OCR3B = 50; // 모터2
	TCCR3B = 0x1A;
	TCCR3A = 0x82; 
	ICR3 = 100;	

	uart_init(BAUDRATE(9600));
	sei();
	value = 40;
	while(1)
	{
		
		
		if(strcmp(arr,"LEFT") ==0)
		{
			PORTA  = 0x02;
			DC_Motor(0);
			DC_Motor2(value);
			_delay_ms(1000);
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"RIGHT") ==0)
		{
			PORTA  = 0x0F;
			DC_Motor(value);
			DC_Motor2(0);
			_delay_ms(1000);
			
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"FORWARD") ==0)
		{
			PORTA  = 0x00;
			DC_Motor(value);
			DC_Motor2(value);
			   _delay_ms(1000);
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"BACK") ==0)
		{
			PORTA  = 0xFF;
			DC_Motor(value);
			DC_Motor2(value);
			_delay_ms(1000);
			memset(arr,0,10);	
		}
		
		if(strcmp(arr,"UP") ==0) // 속도만 바꿔줌
		{
			value += 20;
			if(value >= 120) // 최대 speed
			{
				value = 100;
			}
			PORTA  = 0xFF;
			memset(arr,0,10);
		}
		if(strcmp(arr,"DOWN") ==0) // 속도만 바꿔줌
		{
			value -= 20;
			if(value <= 20) // 최대 speed
			{
				value = 20;
			}
			
			PORTA  = 0xFF;
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"STOP") ==0)
		{
			PORTA  = 0xFF;
			DC_Motor(0);
			DC_Motor2(0);
			_delay_ms(1000);
			memset(arr,0,10);
		}
		
		
		
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

