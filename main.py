import math

def calculate_bit_rate():
    # First get all our recorded dBm measurements (i'll just make a list but we could also have a csv)
    angles = [0,90,45,50,60,30,15,-90,-45,-27]
    dbm_measurements = [-56,-66,-58,-59,-59.50,-57,-56,-76,-57,-56]

    # our noise floor in dBm
    noise_floor_dbm = -92
    # our bandwith in kHz
    bandwith_khz = 50
    bandwidth_hz = 1000 * bandwith_khz
    

    #list for our snr measurements in dB
    snr_measurements = []

    # calculate the SNR for every dBm measurement
    for dbm in dbm_measurements:
        # signal - noise floor
        snr_value = dbm - noise_floor_dbm
        snr_measurements.append(snr_value)

    # now we have to calculate the SNR ratio
    # power ratio = 10 ^ (db/10)
    snr_power_ratios = []

    for snr_db in snr_measurements:
        power_ratio = 10 ** (snr_db/10)
        snr_power_ratios.append(power_ratio)


    

    # use shannon theorem to find maximum rate
    #  bandwith * log2(1 + snr)

    max_data_speeds = []

    # Output
    print(f"Using a bandwith of {bandwidth_hz} Hz and a noise floor of {noise_floor_dbm} dBm\n")
    print("-------------------------")

    for angle,dbm,snr_ratio,snr_db in zip(angles,dbm_measurements,snr_power_ratios,snr_measurements):
        data_speed = bandwidth_hz * math.log2(1 + snr_ratio)
        max_data_speeds.append(data_speed)
        print(f"At the angle {angle} degrees:\nThe dBm was: {dbm} dbM")
        print(f"The SNR value is: {snr_db} dB")
        print(f"The signal to noise ratio: {snr_ratio}")
        print(f"Max data speed: {data_speed} bits per second")
        print("-------------------------")

    print(f"All angles we checked: {angles}")
    print(f"All the dBm measurements: {dbm_measurements}")
    print(f"Our SNR measurements are: {snr_measurements}")
    print(f"Our SNR power ratios are: {snr_power_ratios}")
    print(f"The maximum rates are: {max_data_speeds}")
    

def main():
    calculate_bit_rate()


if __name__ == "__main__":
    main()
