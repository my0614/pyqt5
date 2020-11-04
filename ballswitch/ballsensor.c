/*
 * BALLSW.c
 *
 * Created: 2020-11-04 오전 9:23:57
 * Author : MY
 */ 

#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

void uart_init(unsigned int baud)
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) | (1<<RXCIE0);
} // 8bit, no parity, 1 stop bit, TX enable, RX ISR enable

void uart_write(unsigned char data)
{
	while (!(UCSR0A & (1 << UDRE0)));
	// wait for sending
	UDR0 = data; // send
}

void uart_string(char* str)
{
	while (*str)
	uart_write(*str++);
}

ISR(USART0_RX_vect)
{
	unsigned char buf = UDR0;
	uart_write(buf - 'a' + 'A');
}


int main(void)
{
    /* Replace with your application code */
	DDRD = 0xff;
	DDRE = 0xff;
	DDRB = 0x00;
	uart_init(BAUDRATE(9600));
	uart_string("start");
	char str[3] = {0,};
	unsigned int count = 0;
	sei();
	
    while (1) 
    {
		if(PINB & 0x01)
		{
			PORTD = 0x00;

		
		}
		else
		{
			PORTD = 0xff;
			count ++;
				

		}
		sprintf(str, "%0d",count);
		uart_string(str);
		_delay_ms(1500);
		
    }
}

