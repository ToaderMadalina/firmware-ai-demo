CC=arm-none-eabi-gcc
OBJCOPY=arm-none-eabi-objcopy
CFLAGS=-mcpu=cortex-a76 -march=armv8-a -O2 -ffreestanding -nostdlib -nostartfiles
LDFLAGS=-T linker.ld -nostdlib -nostartfiles

all: build/main.elf build/main.bin

build/start.o: start.s
	mkdir -p build
	$(CC) $(CFLAGS) -c start.s -o build/start.o

build/main.o: src/main.c
	mkdir -p build
	$(CC) $(CFLAGS) -c src/main.c -o build/main.o

build/main.elf: build/start.o build/main.o linker.ld
	$(CC) $(LDFLAGS) build/start.o build/main.o -o build/main.elf

build/main.bin: build/main.elf
	$(OBJCOPY) -O binary build/main.elf build/main.bin

clean:
	rm -rf build
