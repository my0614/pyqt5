
#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#include <stdio.h>
#include <string.h>
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>

	int blue=0, red=0, green=0;
int state = 0;
char arr[15];
int i=0;
void uart_init(unsigned int baud)
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) |	(1<<RXCIE0);
}

void uart_write(unsigned char data)
{
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}


void init_timers(void)  {
	// red
	TCCR1A |= (1<<WGM10) | (1 << COM1A1) | (1 << COM1B1) | (1 << COM1C1) ;
	TCCR1B |= (1<<WGM12) | (1 << CS11);
	
	
	OCR1A = 255;
	OCR1B = 255;
	OCR1C = 255;
}
void pwm_color(char red, char green, char blue)
{
	DDRB |= 0xFF;
	
	OCR1A = red;
	OCR1B = green;
	OCR1C = blue;
	_delay_ms(1000);
}

int main(void)
{
	sei();
	DDRC = 0xff;
	DDRF = 0xff;
	DDRD = 0xff;
	init_timers();

	//int r=0,g=0,b=0;
	int cnt = 1;
	uart_init(BAUDRATE(9600));
	
	while(1)
	{
		
		red = (arr[0]-'0') * 100;
		red += (arr[1]-'0')*10;
		red += (arr[2]-'0')*1;
		green = (arr[3] -'0')*100;
		green += (arr[4]-'0')*10;
		green += (arr[5] - '0');
		blue = (arr[6]-'0')*100;
		blue += (arr[7]-'0')*10;
		blue += (arr[8]-'0');
		pwm_color(red,green,blue);
		_delay_ms(2000);
	
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



