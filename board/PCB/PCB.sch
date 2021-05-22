EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Exiron_5-Way_Switch:Exiron_5-Way_Switch S1
U 1 1 609748B2
P 2850 2300
F 0 "S1" H 2800 1800 50  0000 L CNN
F 1 "Exiron_5-Way_Switch" H 2450 1900 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical" H 2600 2150 50  0001 C CNN
F 3 "http://cdn.sparkfun.com/datasheets/BreakoutBoards/5-Way_Tactile_Switch_BOB_v10.pdf" H 2600 2150 50  0001 C CNN
	1    2850 2300
	-1   0    0    1   
$EndComp
$Comp
L Device:LED D1
U 1 1 6098BDA1
P 2850 3650
F 0 "D1" H 2843 3867 50  0000 C CNN
F 1 "LED_Green_5mm" H 2843 3776 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm" H 2850 3650 50  0001 C CNN
F 3 "~" H 2850 3650 50  0001 C CNN
	1    2850 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D2
U 1 1 6098C65A
P 2850 4000
F 0 "D2" H 2843 4217 50  0000 C CNN
F 1 "LED_Yellow_5mm" H 2843 4126 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm" H 2850 4000 50  0001 C CNN
F 3 "~" H 2850 4000 50  0001 C CNN
	1    2850 4000
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D3
U 1 1 6098D3B6
P 2850 4350
F 0 "D3" H 2843 4567 50  0000 C CNN
F 1 "LED_Red_5mm" H 2843 4476 50  0000 C CNN
F 2 "LED_THT:LED_D5.0mm" H 2850 4350 50  0001 C CNN
F 3 "~" H 2850 4350 50  0001 C CNN
	1    2850 4350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 6098F8F1
P 2850 4650
F 0 "R1" V 2643 4650 50  0000 C CNN
F 1 "80 ohm" V 2734 4650 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" V 2780 4650 50  0001 C CNN
F 3 "~" H 2850 4650 50  0001 C CNN
	1    2850 4650
	0    1    1    0   
$EndComp
Text Notes 7050 6850 0    50   ~ 10
Achtung: Lolin und die andern Komponenten,\ndie auf die Rückseite sollen sind nicht spiegelverkehrt!\n->> Gelöst
$Comp
L 1.3_OLED_v.1.0:1.3"OLED_Display P2
U 1 1 60994766
P 8250 4400
F 0 "P2" V 8750 4400 50  0000 C CNN
F 1 "1.3\"OLED_Display" V 8650 4400 50  0000 C CNN
F 2 "SSH1106 OLED display:PinSocket_1x07_P2.54mm_Vertical" H 8400 4600 50  0001 C CNN
F 3 "" H 8400 4600 50  0001 C CNN
	1    8250 4400
	0    -1   -1   0   
$EndComp
$Comp
L Piezo_Buzzer_MH-FMD_YL-44:PiezoBuzzerMH-FMD_back P1
U 1 1 60991E47
P 2900 3050
F 0 "P1" H 2933 3375 50  0000 C CNN
F 1 "PiezoBuzzerMH-FMD_back" H 2933 3284 50  0000 C CNN
F 2 "Piezo Buzzer MH-FMD YL-44:Piezo_Buzzer_MH-FMD_back" H 2900 3050 50  0001 C CNN
F 3 "" H 2900 3050 50  0001 C CNN
	1    2900 3050
	1    0    0    -1  
$EndComp
$Comp
L SCD30:SCD30_back U1
U 1 1 6099312B
P 8250 5400
F 0 "U1" H 8022 5354 50  0000 R CNN
F 1 "SCD30_back" H 8022 5445 50  0000 R CNN
F 2 "MODULE_SCD30:MODULE_SCD30_back" H 8050 5450 50  0001 L BNN
F 3 "" H 8050 5450 50  0001 L BNN
F 4 "7.0mm" H 8050 5450 50  0001 L BNN "MAXIMUM_PACKAGE_HEIGHT"
F 5 "D1" H 8050 5450 50  0001 L BNN "PARTREV"
F 6 "Sensirion" H 8050 5450 50  0001 L BNN "MANUFACTURER"
F 7 "Manufacturer Recommendations" H 8050 5450 50  0001 L BNN "STANDARD"
	1    8250 5400
	-1   0    0    1   
$EndComp
Wire Wire Line
	6650 2800 6750 2800
Wire Wire Line
	6750 2800 6750 1150
Wire Wire Line
	6750 1150 3300 1150
Wire Wire Line
	3300 1150 3300 2100
Wire Wire Line
	3300 2100 3200 2100
Wire Wire Line
	6650 2900 6850 2900
Wire Wire Line
	6850 2900 6850 1250
Wire Wire Line
	6850 1250 3400 1250
Wire Wire Line
	3400 1250 3400 2200
Wire Wire Line
	3400 2200 3200 2200
Wire Wire Line
	6650 3000 6950 3000
Wire Wire Line
	6950 3000 6950 1350
Wire Wire Line
	6950 1350 3500 1350
Wire Wire Line
	3500 1350 3500 2300
Wire Wire Line
	3500 2300 3200 2300
Wire Wire Line
	6650 3100 7050 3100
Wire Wire Line
	7050 3100 7050 1450
Wire Wire Line
	7050 1450 3600 1450
Wire Wire Line
	3600 1450 3600 2400
Wire Wire Line
	3600 2400 3200 2400
Wire Wire Line
	6650 3200 7150 3200
Wire Wire Line
	7150 3200 7150 1550
Wire Wire Line
	7150 1550 3700 1550
Wire Wire Line
	3700 1550 3700 2500
Wire Wire Line
	3700 2500 3200 2500
Wire Wire Line
	6650 3400 7250 3400
Wire Wire Line
	7250 3400 7250 1650
Wire Wire Line
	7250 1650 3800 1650
Wire Wire Line
	3800 1650 3800 3050
Wire Wire Line
	3800 3050 3100 3050
Wire Wire Line
	6650 3500 7350 3500
Wire Wire Line
	7350 3500 7350 1750
Wire Wire Line
	7350 1750 3900 1750
Wire Wire Line
	3900 1750 3900 3650
Wire Wire Line
	3900 3650 3000 3650
Wire Wire Line
	6650 3600 7450 3600
Wire Wire Line
	7450 3600 7450 1850
Wire Wire Line
	7450 1850 4000 1850
Wire Wire Line
	4000 1850 4000 4000
Wire Wire Line
	4000 4000 3000 4000
Wire Wire Line
	6650 3800 7550 3800
Wire Wire Line
	7550 3800 7550 1950
Wire Wire Line
	7550 1950 4100 1950
Wire Wire Line
	4100 1950 4100 4350
Wire Wire Line
	4100 4350 3000 4350
Wire Wire Line
	5150 3800 5000 3800
Wire Wire Line
	5000 3800 5000 4400
Wire Wire Line
	5000 4400 6800 4400
Wire Wire Line
	6800 4400 6800 4100
Wire Wire Line
	6800 4100 7950 4100
Wire Wire Line
	5150 3700 4900 3700
Wire Wire Line
	4900 3700 4900 4500
Wire Wire Line
	4900 4500 6900 4500
Wire Wire Line
	6900 4500 6900 4200
Wire Wire Line
	6900 4200 7950 4200
Wire Wire Line
	5150 3400 4800 3400
Wire Wire Line
	4800 3400 4800 4600
Wire Wire Line
	4800 4600 7000 4600
Wire Wire Line
	7000 4600 7000 4300
Wire Wire Line
	7000 4300 7950 4300
Wire Wire Line
	5150 2700 4700 2700
Wire Wire Line
	4700 2700 4700 4700
Wire Wire Line
	4700 4700 7100 4700
Wire Wire Line
	7100 4700 7100 4400
Wire Wire Line
	7100 4400 7950 4400
Wire Wire Line
	5150 3300 4600 3300
Wire Wire Line
	4600 3300 4600 4800
Wire Wire Line
	4600 4800 7200 4800
Wire Wire Line
	7200 4800 7200 4500
Wire Wire Line
	7200 4500 7950 4500
Wire Wire Line
	5150 3100 4500 3100
Wire Wire Line
	4500 3100 4500 4900
Wire Wire Line
	4500 4900 7200 4900
Wire Wire Line
	7200 4900 7200 5400
Wire Wire Line
	7200 5400 7950 5400
Wire Wire Line
	5150 2800 4400 2800
Wire Wire Line
	4400 2800 4400 5000
Wire Wire Line
	4400 5000 7100 5000
Wire Wire Line
	7100 5000 7100 5300
Wire Wire Line
	7100 5300 7950 5300
Wire Wire Line
	2700 3650 2600 3650
Wire Wire Line
	2600 3650 2600 4000
Wire Wire Line
	2600 4650 2700 4650
Wire Wire Line
	2700 4350 2600 4350
Connection ~ 2600 4350
Wire Wire Line
	2600 4350 2600 4650
Wire Wire Line
	2700 4000 2600 4000
Connection ~ 2600 4000
Wire Wire Line
	2600 4000 2600 4350
Wire Wire Line
	3200 2000 3200 1700
Wire Wire Line
	3200 1700 2250 1700
Wire Wire Line
	2250 1700 2250 3300
Wire Wire Line
	2250 3300 3100 3300
Wire Wire Line
	3100 3300 3100 3150
Wire Wire Line
	3100 2950 3700 2950
Wire Wire Line
	3700 2950 3700 2600
Wire Wire Line
	3700 2600 3200 2600
Wire Wire Line
	3000 4650 3100 4650
Wire Wire Line
	3100 4650 3100 4800
Wire Wire Line
	3100 4800 2250 4800
Wire Wire Line
	2250 4800 2250 3300
Connection ~ 2250 3300
Wire Wire Line
	7950 4600 7300 4600
Wire Wire Line
	7300 4600 7300 5100
Wire Wire Line
	3700 5100 3700 2950
Connection ~ 3700 2950
Wire Wire Line
	7950 5100 7300 5100
Wire Wire Line
	7950 5200 7400 5200
Wire Wire Line
	3100 5200 3100 4800
Connection ~ 3100 4800
Wire Wire Line
	7950 4700 7400 4700
Wire Wire Line
	7400 4700 7400 5200
Connection ~ 7400 5200
Wire Wire Line
	7400 5200 3100 5200
Connection ~ 3100 3300
Wire Wire Line
	3700 2600 4200 2600
Wire Wire Line
	4200 2600 4200 2050
Connection ~ 3700 2600
Wire Wire Line
	3100 3300 4300 3300
Wire Wire Line
	4300 2600 4800 2600
Wire Wire Line
	4300 3300 4300 2600
Connection ~ 7300 5100
Wire Wire Line
	7300 5100 3700 5100
$Comp
L Lolin_D32_pro:LolinD32pro_back K1
U 1 1 60990E97
P 5900 3350
F 0 "K1" H 5900 4465 50  0000 C CNN
F 1 "LolinD32pro_back" H 5900 4374 50  0000 C CNN
F 2 "Lolin_d32_pro:Lolin_d32_pro_back" H 5900 2550 50  0001 C CNN
F 3 "https://www.wemos.cc/en/latest/_static/files/sch_d32_pro_v2.0.0.pdf" H 5900 2450 50  0001 C CNN
	1    5900 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 2600 6650 2050
Wire Wire Line
	6650 2050 4200 2050
$Comp
L Connector:Conn_01x02_Female J1
U 1 1 60A2DD2C
P 4800 2150
F 0 "J1" V 4738 1962 50  0000 R CNN
F 1 "Conn_01x02_Female" V 4647 1962 50  0000 R CNN
F 2 "" H 4800 2150 50  0001 C CNN
F 3 "~" H 4800 2150 50  0001 C CNN
	1    4800 2150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4900 2350 4900 2600
Connection ~ 4900 2600
Wire Wire Line
	4900 2600 5150 2600
Wire Wire Line
	4800 2350 4800 2600
Connection ~ 4800 2600
Wire Wire Line
	4800 2600 4900 2600
$EndSCHEMATC
