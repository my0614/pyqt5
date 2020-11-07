/*
 * sensor_project.c
 *
 * Created: 2020-10-22 오전 9:13:08
 * Author : MY
 */ 



#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)
#include <stdio.h>
#include <string.h>
#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>

#define TRIG 6
#define ECHO 7
#define SOUND_VELOCITY 340UL

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



void seting()
{
	DDRC=0x00;      // PC0 : soundsensor
	PORTC=0xff;
	DDRA = 0x00;
	DDRD = 0xff; // LED
	PORTD = 0xff; 
	DDRG = 0x00; // 부저사용하기
	PORTG = 0xff; 
	DDRE = ((DDRE | (1<<TRIG)) & ~(1<<ECHO)); //초음파 센서
	
	
}

unsigned int sensor_count =0;
int toggle = 0;
unsigned int distance;

int main(void)
{
	seting(); // port설정함수	
	uart_init(BAUDRATE(9600));
	sei();
	uart_string("hello");
	
	while(1)
	{
		char str[5] = {0,};
		
		// 초음파 거리 센서	
		TCCR1B = 0x03;
		PORTE &= ~(1<<TRIG);
		_delay_us(10);
		PORTE |= (1<<TRIG);
		_delay_us(10);
		PORTE &= ~(1<<TRIG);
		while(!(PINE & (1<<ECHO)));
		TCNT1 = 0x0000;
		while(PINE & (1<<ECHO));
		TCCR1B = 0x00;
		distance = (unsigned int)(SOUND_VELOCITY * (TCNT1 * 4 / 2) / 1000);
		
		//부저 울리기
		if(sensor_count >= 3)
		{
			PORTG=0xff;
			_delay_ms(1000);
			PORTG=0x00;
			_delay_ms(1000);
			sprintf(str, "%s","yes"); // yes넣기
			uart_string(str);
			sensor_count=0;// 값초기화
			
		}
		if(distance <= 70)
		{
			 
			sprintf("sen1");// 초음파센서 감지 toggle 4번
			
		} 
		if(!(PINC & 0x01)) // PINC0번
		{
			sprintf("sen2"); // sound_sensor는 toggle 1번
		}
		
		
		if(!(PINC & 0x02))
		{
			sprintf("sen3"); // 노크모듈은 toggle 2번
		}
		
		_delay_ms(1500); // delay주기
		
		
		
		
	}
}

