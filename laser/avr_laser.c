/*
 * loser.c
 *
 * Created: 2020-11-09 오전 11:07:56
 * Author : MY
 */ 

#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

void int_adc();
unsigned short read_adc();
void show_adc_led(unsigned short data);

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

int init_adc(void)
{
	ADMUX = 0x40;
	ADCSRA = 0x87;    // ADC 동작표시, ADC 8은 enable, ADC 7은 prescaler 128
}

unsigned short read_adc()
{
	unsigned char adc_low, adc_high;
	unsigned short value;

	ADCSRA |= 0x40;    // ADC 시작
	// ADC Complete
	while((ADCSRA & 0x10) != 0x10);
	adc_low = ADCL;
	adc_high = ADCH;
	value = (adc_high << 8) | adc_low;
	
	return value;
}

void show_adc_led(unsigned short value)
{
	if(value<=20)
	{
		PORTA = 0x01;
		uart_string("1");
		_delay_ms(1000);
		
	}
	else
	{
		PORTA = 0x04;
		uart_string("0");
		_delay_ms(1000);
	
	}
}

int main(void)
{
	DDRE = 0xff;
	uart_init(BAUDRATE(9600));
	uart_string("start");
	_delay_ms(100);
	
	unsigned short value;
	DDRD = 0xff;
	DDRF = 0x00;
	DDRA = 0xff;
	init_adc();
	PORTA = 0x02;
	_delay_ms(3000);
	PORTA = 0x04;
	_delay_ms(500);
    /* Replace with your application code */
    while (1) 
    {
		value = read_adc();
		show_adc_led(value);
		_delay_ms(500); // delay
    }
}


