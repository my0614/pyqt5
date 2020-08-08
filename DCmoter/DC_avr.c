#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#include <stdio.h>
#include <string.h>
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>
volatile char speed=0;

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

int main(void)
{
	DDRA = 0xff;
	int i;
	DDRB=0x60;
	
	TCCR1B=0x1A;
	OCR1A=0;
	ICR1=100;
	uart_init(BAUDRATE(9600));
	sei();
	while(1)
	{
		
		if(strcmp(arr,"LEFT") ==0)
		{
			DC_Motor(0);
			_delay_ms(1000);
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"RIGHT") ==0)
		{
			DC_Motor(80);
			_delay_ms(1000);
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"FORWARD") ==0)
		{
			DC_Motor(20);
			_delay_ms(1000);
			memset(arr,0,10);
		}
		
		if(strcmp(arr,"BACK") ==0)
		{
			DC_Motor(60);
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
