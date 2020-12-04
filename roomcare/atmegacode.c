#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU / 16 / x) - 1)

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define DHT 0
#define DHT_DDR DDRF
#define DHT_PORT PORTF
#define DHT_PIN PINF

int state = 0;
char arr[15];
char data2[10];
int i=0;

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

void Request()
{
	DHT_DDR |= (1<<DHT);
	DHT_PORT &= ~(1<<DHT);
	_delay_ms(20);
	DHT_PORT |= (1<<DHT);
	_delay_us(40);
	
	DHT_DDR &= ~(1<<DHT);
	while(DHT_PIN & (1<<DHT));
	while((DHT_PIN & (1<<DHT))==0);
	while(DHT_PIN & (1<<DHT));
}

uint8_t Receive_data()
{
	uint8_t c = 0;
	for (int i = 0; i < 8; i++)
	{
		while((DHT_PIN & (1<<DHT)) == 0);  	/* check received bit 0 or 1 */
		_delay_us(30);
		if(DHT_PIN & (1<<DHT)) 				/* if high pulse is greater than 30ms */
		{
			c = (c<<1)|(0x01);					/* then its logic HIGH */
		}
		else									/* otherwise its logic LOW */
		{
			c = (c<<1);
		}

		while(DHT_PIN & (1<<DHT));
	}
	return c;
}

int main(void)
{
	uint16_t I_Humi, D_Humi, I_Temp, D_Temp, check;
	DDRE = 0xff;
	DDRA = 0xFF;
	DDRC = 0xFF;
	uart_init(BAUDRATE(9600));
	
	sei();
	;
	while (1)
	{
		if(strcmp(arr,"LIVINGN") ==0)
		{
			PORTE = 0x00;
			memset(arr,0,15);
		}
		
		if(strcmp(arr,"LIVINGF") ==0)
		{
			PORTE = 0xff;
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
		//uart_string("start");
		Request();					// 데이터 전송 요청
		
		I_Humi = Receive_data();		// 습도 상위 8비트 전송
		
		D_Humi = Receive_data();		// 습도 하위 8비트 전송
		I_Temp = Receive_data();		// 온도 상위 8비트 전송
		D_Temp = Receive_data();		// 온도 하위 8비트 전송
		check = Receive_data();	// CheckSum 비트 = 습도 16비트 + 온도 16비트
		
		if ((I_Humi + D_Humi + I_Temp + D_Temp) != check)
		{
			
		}
		else
		{
			
			
			char str[16] = {0,};
			
			itoa(I_Temp, str, 10);
			itoa(D_Temp, str, 10);
			
			itoa(I_Humi, str, 10);
			itoa(D_Humi, str, 10);
			sprintf(str, "%3d%3d", I_Temp, I_Humi);
			uart_string(str);
		}
		_delay_ms(3000);
		
		

	}
}